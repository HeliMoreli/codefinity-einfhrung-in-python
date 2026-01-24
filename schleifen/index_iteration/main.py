prices = [29.99, 45.50, 12.75, 38.20]

for cost in range(len(prices)):
    if cost ==0:
        prices[cost] = prices[cost]-prices[cost]*0.10

    if cost == 1:
        prices[cost]-= prices[cost]*0.20

    if cost == 2:
        prices[cost] = prices[cost]-prices[cost]*0.15

    if cost == 3: 
        prices[cost] = prices[cost]-prices[cost]*0.05

    print(f"Updated price for item {cost+1}: ${prices[cost]:.2f}")


