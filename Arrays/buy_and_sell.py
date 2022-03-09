# O(n)
def buy_sell(a:list):
    min_price , max_profit = float('inf'), 0.0

    for price in a:
        profit_today = price - min_price
        max_profit = max(max_profit, profit_today)
        min_price = min(min_price, price)

    return max_profit


print(buy_sell([310,315, 275, 295, 260, 270, 290, 230, 255, 250]))




def buy_sell_twice(a:list):
    t1_price, t1_profit = float('inf'), 0.0
    t2_price, t2_profit = float('inf'), 0.0

    for price in a:
        t1_price = min(price, t1_price)
        t1_profit = max(t1_profit, price-t1_price)
        t2_price = min(t2_price, price-t1_profit)
        t2_profit = max(t2_profit, price-t2_price)


    return t2_profit