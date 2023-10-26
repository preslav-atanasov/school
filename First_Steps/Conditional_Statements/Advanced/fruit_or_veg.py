product = str(input("molq vuvedete produkt : "))

if product.lower() in ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]:
    print("fruit")
elif product.lower() in ["tomato", "cucumber", "pepper", "carrot"]:
    print("vegetable")
else:
    print("unknown")
