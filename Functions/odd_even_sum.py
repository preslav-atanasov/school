def odd_even(defnumlist, defevensum, defoddsum):
    for i in defnumlist:
        if int(i) % 2 == 0:
            defevensum += int(i)
        else:
            defoddsum += int(i)
    print(f"Odd sum = {defoddsum}, Even sum = {defevensum}")


number = int(input())
numlist = list(str(number))
evensum = 0
oddsum = 0

odd_even(numlist, evensum, oddsum)
