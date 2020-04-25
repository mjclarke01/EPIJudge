from test_framework import generic_test


# This is (much) quicker if we replace the min and max stuff with if statements
# but let's go for readability
# def buy_and_sell_stock_twice(prices):
#     if len(prices) == 1:
#         return 0.0
#
#     min_price = float('inf')
#     profit1 = 0
#     total_profit = 0
#     increasing = False
#     for i, val1 in enumerate(prices):
#         min_price = min(val1, min_price)
#
#         if val1 - min_price > profit1:
#             profit1 = val1 - min_price
#             if profit1 > total_profit:
#                 total_profit = profit1
#             increasing = True
#         elif increasing:
#             # Only test 2nd buy-sell when we reach peak
#             increasing = False
#
#             min_price2 = val1
#             for val2 in prices[i:]:
#                 min_price2 = min(val2, min_price2)
#                 total_profit = max(total_profit, profit1 + val2 - min_price2)
#
#     return total_profit


# O(n) and constant space?
# def buy_and_sell_stock_twice(prices):
#     if len(prices) == 1:
#         return 0.0
#
#     prev = float('inf')
#     temp_min = None
#     ans = []
#     best_minima = float('inf')
#
#     for i, v in enumerate(prices):
#         if i == len(prices) - 1:
#             next = 0.0
#         else:
#             next = prices[i + 1]
#
#         if next == v:
#             continue
#
#         if prev > v <= next:
#             temp_min = v
#         elif prev <= v > next:
#             if len(ans) < 4:
#                 ans.append(temp_min)
#                 ans.append(v)
#             else:
#                 high = v
#                 front = ans[1] - ans[0]
#                 back = ans[3] - ans[2]
#
#                 best_minima = min(temp_min, best_minima)
#
#                 diff = high - best_minima
#
#                 if diff > back and back < front:
#                     if ans[2] < best_minima:
#                         ans[3] = high
#                         best_minima = float('inf')
#                         continue
#
#                     if ans[3] > ans[1] and ans[0] < ans[2]:
#                         ans[1] = ans[3]
#                         ans[2] = best_minima
#                     else:
#                         ans[2] = min(ans[2], best_minima)
#                     ans[3] = high
#                     best_minima = float('inf')
#                 elif high > ans[3] and high - ans[2] + ans[1] - ans[
#                     0] > diff + back:
#                     ans[3] = high
#                     best_minima = float('inf')
#                 elif diff > front or ans[3] - ans[0] + diff > front + back:
#                     if ans[0] > ans[2]:
#                         ans[0] = ans[2]
#                     ans[1] = ans[3]
#                     ans[2] = best_minima
#                     ans[3] = high
#                     best_minima = float('inf')
#
#         prev = v
#
#     if len(ans) == 0:
#         return 0.0
#
#     if len(ans) == 2:
#         return ans[1] - ans[0]
#
#     return ans[1] - ans[0] + ans[3] - ans[2]


# def buy_and_sell_stock_twice(prices):
#     min_prices, max_profits = [float('inf')] * 2, [0] * 2
#     for price in prices:
#         print(price)
#         for i in reversed(list(range(2))):
#             max_profits[i] = max(max_profits[i], price - min_prices[i])
#             min_prices[i] = min(min_prices[i],
#                                 price - (0 if i == 0 else max_profits[i - 1]))
#         print(max_profits, min_prices)
#
#     return max_profits[-1]

def buy_and_sell_stock_twice(prices):
    # Holds the absolute lowest price so far (global minima)
    lowest_price = float('inf')
    # Holds the biggest single profit so far (price - lowest_price)
    biggest_single_profit = 0
    # Holds the lowest value for price - biggest_single_profit
    # This is combined with the current price to get the total profit
    # This effectively resets when the biggest_single_profit increases
    tracker = float('inf')
    # Holds the maximum profit
    # The calculation of this is the only place where local maxima are considered
    max_profit = 0

    for price in prices:
        max_profit = max(max_profit, price - tracker)
        tracker = min(tracker, price - biggest_single_profit)
        biggest_single_profit = max(biggest_single_profit, price - lowest_price)
        lowest_price = min(lowest_price, price)

    return max_profit


if __name__ == '__main__':
    # print(buy_and_sell_stock_twice([0.2, 0.7, 0.9, 0.4, 0.1, 0.1, 0.5, 0.4, 0.9]))  # 1.5
    print(buy_and_sell_stock_twice([7, 10, 8, 10, 9, 13, 1]))  #
    # print(buy_and_sell_stock_twice([0.1, 0.2]))  # 0.1
    # print(buy_and_sell_stock_twice([7.7, 9.5, 5.2, 9.4, 4.7, 6.0, 2.3, 2.7, 2.4, 5.4, 6.3, 8.0, 6.1, 5.7, 0.5,
    #  10.0, 2.4, 3.0, 6.4, 4.9, 9.5, 4.8, 6.9, 8.8, 9.6, 2.7, 0.9, 7.4, 0.4, 4.6,
    #  9.1, 0.1, 3.3, 7.3, 9.9, 2.2, 0.8, 0.8, 1.0, 3.8, 8.0, 1.1, 0.4, 9.7, 6.2,
    #  0.6, 8.2, 4.1, 8.5, 2.0, 6.2, 9.8, 7.5, 5.9, 0.5, 8.6, 2.1, 8.4, 6.3, 9.2,
    #  8.0, 1.1, 3.6, 1.6, 9.4, 6.5, 7.4, 5.8, 6.3, 1.3, 1.1, 6.9, 9.7, 6.0, 9.6,
    #  5.3, 6.7, 4.3, 4.2, 0.6, 5.2, 7.1, 2.5, 10.0, 8.7, 1.5, 1.3, 4.2, 4.1, 3.4,
    #  1.5, 7.2, 8.8, 3.6, 9.8, 7.3, 4.4, 10.1, 2.3, 10.1, 2.5]))  # 19.5
    #
    # print(buy_and_sell_stock_twice([0.9, 0.8, 0.8, 0.8, 0.7, 0.2, 1.0, 0.5, 0.6, 1.1, 0.7, 0.3])) # 1.4
    #
    # print(buy_and_sell_stock_twice(
    #     [2.9, 5.1, 5.0, 0.6, 4.2, 1.4, 3.7, 1.9, 4.2, 1.4, 1.9, 1.8, 3.5, 0.6,
    #      0.8, 0.2, 1.2, 1.2, 2.2, 4.5, 0.9, 5.1, 0.6, 1.1, 2.0, 4.5, 1.7, 0.3,
    #      0.2, 2.1, 2.7, 3.6, 2.2, 1.6, 3.0, 3.7, 3.2, 1.4, 2.3, 4.0, 1.9, 3.5,
    #      4.3, 1.3, 0.1, 4.2, 2.4, 1.9, 3.5, 1.1, 0.5]
    # ))  # 9.0

    # print(buy_and_sell_stock_twice([0.8, 0.5, 3.0, 4.6, 3.4, 3.7, 3.7, 5.3, 0.7, 4.5, 1.0, 4.2, 3.3, 2.2, 3.9, 2.9, 4.1, 0.9, 5.2, 4.1, 4.9, 0.1, 3.6, 0.7, 5.2, 1.5, 2.2, 4.8, 3.4, 5.2, 2.4, 2.3, 4.2, 4.8, 0.7, 3.5, 1.6, 1.0, 2.6, 3.8, 2.2, 0.2, 2.5, 2.6, 2.5, 5.3, 0.4, 2.3, 5.8, 3.2, 3.6, 4.0, 1.4, 0.4, 2.2, 4.2, 1.8, 1.6, 0.8]))

    # print(buy_and_sell_stock_twice([0.1, 0.1]))

    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
