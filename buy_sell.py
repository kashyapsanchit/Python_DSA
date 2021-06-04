def buy_sell(A):

    max_profit = 0
    min_price = A[0]

    for price in A:
        min_price = min(min_price, price)

        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit

A = [310, 315, 290, 260, 275, 630]

print(buy_sell(A))