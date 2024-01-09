from random import randint

inumber = randint(1, 200)
guess = 0
count = 0

print("Namislil sum si edno chislo !")
print("Mojesh li da go poznaesh? Imash 5 opita!")

while count < 5:
    guess = int(input("Molq vuvedete chislo: "))
    if inumber == guess:
        print(f"Bravo! Chisloto, koeto si bqh namislil beshe {inumber}. Pozna v {count + 1} opita")
        break
    count += 1

    if guess > inumber and count != 5:
        print("Chisloto, koeto si mislq e po-malko!")
    if guess < inumber and count != 5:
        print("Chisloto, koeto si mislq e po-golqmo!")

if inumber != guess:
    print(f"Womp womp. Ne pozna. Chisloto koeto si bqh namislil beshe {inumber}")

