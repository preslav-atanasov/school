n = int(input())
names = set()
for i in range(0, n):
    name = input("Name?: ")
    names.add(name)

for name in names:
    print(name)


names = set(input() for name in range(int(input())))
print(*names, sep="\n"  )