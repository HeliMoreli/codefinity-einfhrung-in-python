grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8), 
    "Eggs": ("Dairy", 5.50, 30), 
    "Bread": ("Bakery", 2.99, 15), 
    "Apples": ("Produce", 1.50, 50)
}
print(grocery_inventory.get("Eggs"))
eggs_entry = grocery_inventory["Eggs"]
eggs_price = eggs_entry[1]
if(eggs_price>5):
    print("Eggs are too expensive, reducing the price by $1.") 
    grocery_inventory.update({"Eggs": ("Dairy", 4.50, 30)})
else:
    print("The price of Eggs is reasonable")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
print(grocery_inventory.get("Milk"))
how_much_milk = grocery_inventory["Milk"]
milk_quantity = how_much_milk[2]
if(milk_quantity<10):
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": ("Dairy", 3.50, 28)})
else:
    print("Milk has sufficient stock.")

apple_details = grocery_inventory["Apples"]
apple_price = apple_details[1]
if(apple_price>2):
    grocery_inventory.pop("Apples")
if(apple_price>2):
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)