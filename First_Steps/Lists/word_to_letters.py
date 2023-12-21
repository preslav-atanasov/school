word = input("duma: ")
word_list = []

for i in word:
    if i.lower() not in "аъоуеи":
        word_list.append(i)

print(word_list)

"""word_list_reversed = list(reversed(word_list))

if word_list == word_list_reversed:
    print("pallindrome!")
else:
    print("not pallindrome!")
"""
