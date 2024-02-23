def numberpalindrome(thisuserinput):
    numlist = [int(x) for x in thisuserinput.split(",")]
    wordlist = []
    for number in numlist:
        for i in list(str(number)):
            wordlist.append(i)
        wlreverse = wordlist.copy()
        wlreverse.reverse()
        if wordlist == wlreverse:
            print("True")
        else:
            print("False")


numberpalindrome(thisuserinput=input())
