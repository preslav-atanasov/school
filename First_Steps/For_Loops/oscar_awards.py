actorName = input("Ime na aktior: ")
academiaPoints = float(input("Tochki ot akademiqta: "))
judgeNum = int(input("Broi ocenqvashti: "))

for i in range(0, judgeNum):
    judgeName = input("Ime na ocenqvashtiq: ")
    judgePoints = float(input("Tochki ot ocenqvashtiq: "))
    recievedPoints = len(judgeName) * (judgePoints / 2)

    if recievedPoints >= 1250.5:
        print(f"Congratulations, {actorName} got a nominee for leading role with {recievedPoints}")
    elif recievedPoints < 1250.5:
        print(f"Sorry, {actorName} you need {1250.5 - recievedPoints} more!")
