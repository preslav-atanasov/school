def asciirange(definput1, definput2):
    for character in range(ord(input1) + 1, ord(input2)):
        print(chr(character), end=" ")


input1 = input()
input2 = input()


asciirange(input1, input2)
