# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120


merci = "milch, kaffee, praline"
gute_sorte = "milch" in merci and "dark" not in merci

print("ich mag nur etwas mit milch", gute_sorte)

product_name = "Almond Milk"
product_quantity = 30

correct_name_type = type(product_name) == str
correct_quantity_type = type(product_quantity) == int
print(correct_name_type, correct_quantity_type)
print(type(product_name) == type(merci))
print(type(correct_name_type) == type(correct_quantity_type))
print(type(correct_name_type))

What_type_is_merci = type(merci)
print(What_type_is_merci)