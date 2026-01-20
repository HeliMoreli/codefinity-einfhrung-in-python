prices = [12.99, 8.50, 15.75, 23.00, 7.25]

# Write your code here

productStock = {
    "milk": 120, 
    "eggs": 200, 
    "bread": 80
}

for products in productStock:
    print(products)

for quantity in productStock.values():
    print(quantity)