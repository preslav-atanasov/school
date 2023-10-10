# Price per square meter & % discount
ppsqm = 7.61
discount = 18 / 100

# Square meters landscaped
sqml = int(input("Kvadratnite metri, koito shte budat ozeleneni: "))

# Final price and discount
fpr = ppsqm * sqml
fdiscount = discount * fpr

print(f"The final price is {fpr - fdiscount} lv.")
print(f"The discount is {fdiscount} lv.")