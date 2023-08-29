from typing import final


def percentdiscount(price, percentoff):
    final_price = price * (1 - percentoff / 100)

    return final_price

price = 200
percentoff = 20

final_price = percentdiscount(price, percentoff)
print(final_price)