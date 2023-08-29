from typing import final


def discount(price, markdown):
    final_price = price - markdown
    
    return final_price

price = 100
markdown = 20

final_price = discount(price, markdown)
print(final_price)