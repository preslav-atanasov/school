animal = str(input("Please enter an animal: "))

if animal == "dog":
    print("mammal")
elif animal in ["crocodile", "tortoise", "snake"]:
    print("reptile")
else:
    print("unknown")