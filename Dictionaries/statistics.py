products = {}

while True:
    command = input()
    if command == "statistics":
        break

    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
