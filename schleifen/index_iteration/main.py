prices = [29.99, 45.50, 12.75, 38.20]

discount_factor = 0.10

for cost in range(len(prices)):
    prices[cost] -= prices[cost]*discount_factor
    print(f"New price of item {cost + 1}: $ {prices[cost]}")

print("Updated prices:", prices)

