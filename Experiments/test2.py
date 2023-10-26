import string

userInput = str(input("please enter a word/phrase: "))
userInputRemovedPunctuation = userInput.translate(str.maketrans('', '', string.punctuation))
userInput = userInputRemovedPunctuation.lower()
userInputWithoutSpaces = userInput.replace(" ", "")

if userInputWithoutSpaces == userInputWithoutSpaces[::-1]:
    print("pallindrome!")
else:
    print("not a pallindrome.")
