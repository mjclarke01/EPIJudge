import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def get_overlap_one_axis(pt1, pt2, pt3, pt4):
    start = -1
    end = -1

    if pt1 <= pt4 and pt2 >= pt3:
        start = max(pt1, pt3)
        end = min(pt2, pt4)

    return start, end


def intersect_rectangle(R1, R2):
    # Does x overlap?
    x_overlaps = get_overlap_one_axis(R1.x, R1.x + R1.width, R2.x, R2.x + R2.width)

    if x_overlaps[0] == -1:
        return Rectangle(0, 0, -1, -1)

    # Does y overlap?
    y_overlaps = get_overlap_one_axis(R1.y, R1.y + R1.height, R2.y, R2.y + R2.height)

    if y_overlaps[0] == -1:
        return Rectangle(0, 0, -1, -1)

    return Rectangle(x_overlaps[0],
                     y_overlaps[0],
                     x_overlaps[1] - x_overlaps[0],
                     y_overlaps[1] - y_overlaps[0]
                     )


def intersect_rectangle(R1, R2):
    def is_intersect(R1, R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)

    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1)  # No intersection.
    return Rectangle(
        max(R1.x, R2.x), max(R1.y, R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))

def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    print("================== no overlap")
    print(intersect_rectangle(Rectangle(0, 0, 10, 10), Rectangle(20, 20, 10, 10)))
    print("================== overlap in both")
    print(intersect_rectangle(Rectangle(0, 0, 10, 10), Rectangle(5, 5, 10, 10)))
    print("================== overlap in both")
    print(intersect_rectangle(Rectangle(5, 5, 10, 10), Rectangle(0, 0, 10, 10)))
    print("================== x only")
    print(intersect_rectangle(Rectangle(0, 0, 20, 10), Rectangle(0, 20, 10, 10)))
    print("================== x only")
    print(intersect_rectangle(Rectangle(5, 0, 10, 10), Rectangle(0, 20, 20, 10)))
    print("================== y only")
    print(intersect_rectangle(Rectangle(0, 0, 10, 10), Rectangle(20, 0, 10, 10)))
    print("==================")


    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
