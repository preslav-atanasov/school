smallest = float("inf")
entered = ""

while entered != "Stop":
    entered = input()
    if entered == "Stop":
        break
    num = int(entered)
    if num < smallest:
        smallest = num
print(smallest)