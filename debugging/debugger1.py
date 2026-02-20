# Goal:
# Calculate the total price of items with a discount.
# Rule:
# - Items costing 50 or more get a 20% discount.
# - The original shopping list should NOT change.

prices = [20, 60, 30, 80, 50]

def total_price(items):
    total = 0

    for price in items:
        if price >= 50:
            price = price * 0.8     # apply discount
               # remove price from list
        total += price

    return total

result = total_price(prices)

print("Total:", result)
print("Prices after checkout:", prices)