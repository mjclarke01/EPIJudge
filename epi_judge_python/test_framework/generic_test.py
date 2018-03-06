# @library
import sys

from os import path

from test_framework.generic_test_handler import GenericTestHandler
from test_framework.test_config import TestConfig
from test_framework.test_failure import TestFailure, PropertyName
from test_framework.test_result import TestResult
from test_framework.test_utils import split_tsv_file
from test_framework.test_utils_console import print_test_info, print_failed_test, print_post_run_stats
from test_framework.timeout_exception import TimeoutException


def generic_test_main(timeous_seconds,
                      test_data_file,
                      test_func,
                      comparator=None,
                      res_printer=None):
    """
    The main test starter.
    :param test_data_file - file with test data
    :param test_func - function to be tested
    :param comparator - custom comparator. A function that accepts
        (expected, computed result) and returns a boolean value
    :param res_printer - function for customized printing
    """
    try:
        commandline_args = sys.argv[1:]
        config = TestConfig.from_command_line(
            test_data_file, timeous_seconds * 1000, commandline_args)

        test_handler = GenericTestHandler(test_func, comparator=comparator)
        return run_tests(test_handler, config, res_printer)
    except RuntimeError as e:
        print(
            '\nCritical error({}): {}'.format(e.__class__.__name__, e),
            file=sys.stderr)
        return TestResult.RUNTIME_ERROR


def run_tests(handler, config, res_printer):
    test_data = split_tsv_file(
        path.join(config.test_data_dir, config.test_data_file))
    handler.parse_signature(test_data[0])

    test_nr = 0
    tests_passed = 0
    total_tests = len(test_data) - 1
    durations = []
    result = TestResult.FAILED

    for test_case in test_data[1:]:
        test_nr += 1

        # Since the last field of test_data is test_explanation, which is not
        # used for running test, we extract that here.
        test_explanation = test_case.pop()

        test_timer = None
        test_failure = None

        try:
            test_timer = handler.run_test(config.timeout, test_case)
            result = TestResult.PASSED
            tests_passed += 1
            durations.append(test_timer.get_microseconds())

        except TestFailure as exc:
            result = TestResult.FAILED
            test_failure = exc
        except TimeoutException:
            result = TestResult.TIMEOUT
        except RecursionError:
            result = TestResult.STACK_OVERFLOW
        except RuntimeError:
            raise
        except Exception as exc:
            result = TestResult.UNKNOWN_EXCEPTION
            test_failure = TestFailure(exc.__class__.__name__)\
                .with_property(PropertyName.EXCEPTION_MESSAGE, str(exc))

        print_test_info(result, test_nr, total_tests,
                        test_failure.get_description()
                        if test_failure else '', test_timer)

        if result != TestResult.PASSED and config.stop_on_error:
            if not handler.expected_is_void():
                test_case.pop()
            if test_failure is None:
                test_failure = TestFailure()
            if test_explanation not in {'', 'TODO'}:
                test_failure\
                    .with_property(PropertyName.EXPLANATION, test_explanation)
            print_failed_test(handler.param_names(), test_case, test_failure,
                              res_printer)
            break

    print()

    if config.stop_on_error:
        print_post_run_stats(tests_passed, total_tests, durations)
    return result