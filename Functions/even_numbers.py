def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


userinput = input()
numlist = [int(x) for x in userinput.split()]
even_numbers = filter(is_even, numlist)
evenlist = []

for x in even_numbers:
    evenlist.append(x)

print(evenlist)
