from test_framework import generic_test


# If I had started to try to optimise this by reducing the number of index calls
# I would have ended up with an answer very similar to the textbook answer - D'OH!
def buy_and_sell_stock_once(prices):
    if len(prices) == 1:
        return 0.0

    low = 0
    high = 0
    new_low = 0
    for i in range(0, len(prices)):
        if prices[i] < prices[new_low]:
            new_low = i

        if prices[i] - prices[new_low] > prices[high] - prices[low]:
            low = new_low
            high = i

    return prices[high] - prices[low]


# Textbook - better!
# def buy_and_sell_stock_once(prices):
#     if len(prices) == 1:
#         return 0.0
#
#     min_price = float('inf')
#     profit = 0.0
#     for p in prices:
#         max_today = p - min_price
#         if max_today > profit:
#             profit = max_today
#         if p < min_price:
#             min_price = p
#
#     return profit


if __name__ == '__main__':
    print(buy_and_sell_stock_once([1.0, 2.0, 0.5, 3.0]))  # 2.5
    print(buy_and_sell_stock_once([1.0, 2.0, 0.5, 3.0, 0.1]))  # 2.5
    print(buy_and_sell_stock_once([1.0, 2.0, 0.5, 3.0, 0.1, 2.9]))  # 2.8
    print(buy_and_sell_stock_once([0.9, 0.2, 0.9, 1.2, 0.4, 0.8, 1.3, 1.2, 0.4, 0.7, 0.4, 0.9, 0.4]))  # 1.1
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
