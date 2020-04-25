#include <vector>
#include <algorithm>
#include <cstdlib>
#include <iterator>
#include "test_framework/generic_test.h"

using std::abs;
using std::vector;
using std::empty;
using std::size;


//vector<int> Multiply(vector<int> num1, vector<int> num2) {
//  bool first = true;
//  bool neg = false;
//
//  if (num2[0] < 0) {
//    neg = ! neg;
//    num2[0] *= -1;
//  }
//
//  if (num1[0] < 0) {
//    neg = ! neg;
//    num1[0] *= -1;
//  }
//
//  if ((num1.size() == 1 and num1[0] == 0) || (num2.size() == 1 and num2[0] == 0)) {
//    return {0};
//  }
//
//  vector<int> ans(num1.size() + num2.size());
//
//  for (int i = size(num1) - 1; i >= 0; --i) {
//    for (int j = size(num2) - 1; j >= 0; --j) {
//      ans[i + j + 1] += num1[i] * num2[j];
//      ans[i + j] += ans[i + j + 1] / 10;
//      ans[i + j + 1] %= 10;
//    }
//  }
//
////  for (auto i = num2.rbegin(); i!= num2.rend(); ++i) {
////    if (first) {
////      first = false;
////    } else {
////      num1.push_back(0);
////    }
////
////    if ((*i) == 0) {
////      continue;
////    }
////
////    auto index = ans.size() - 1;
////
////    for (auto j = num1.rbegin(); j != num1.rend(); ++j) {
////      ans[index] += (*j) * (*i);
////      --index;
////    }
////  }
////
////  for (auto i = ans.rbegin(); i!= ans.rend(); ++i) {
////    if (*i > 9)
////    {
////      *(i + 1) += *i / 10;
////      *i %= 10;
////    }
////  }
//
//
//  if (ans[0] == 0)
//  {
//    ans.erase(ans.begin());
//  }
//
//  if (neg) {
//    ans[0] *= -1;
//  }
//
//  return ans;
//}

vector<int> Multiply(vector<int> num1, vector<int> num2) {
  const int sign = (num1.front() < 0) ^ (num2.front() < 0) ? -1 : 1;
  num1.front() = abs(num1.front()), num2.front() = abs(num2.front());

  vector<int> result(size(num1) + size(num2), 0);
  for (int i = size(num1) - 1; i >= 0; --i) {
    for (int j = size(num2) - 1; j >= 0; --j) {
      result[i + j + 1] += num1[i] * num2[j];
      result[i + j] += result[i + j + 1] / 10;
      result[i + j + 1] %= 10;
    }
  }

  // Remove the leading zeroes.
  result = {
      find_if_not(begin(result), end(result), [](int a) { return a == 0; }),
      end(result)};
  if (empty(result)) {
    return {0};
  }
  result.front() *= sign;
  return result;
}


int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"num1", "num2"};
  return GenericTestMain(args, "int_as_array_multiply.cc",
                         "int_as_array_multiply.tsv", &Multiply,
                         DefaultComparator{}, param_names);
}
