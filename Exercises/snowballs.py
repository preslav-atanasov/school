number = int(input("number of snowballs"))
snowball_value = snowball_maxweight = snowball_maxtime = snowball_maxquality = []

for snowball in range(1, number + 1):
    snowball_weight = int(input("snowball weight: "))
    snowball_time = int(input("time needed for the snowball to hit its target:"))
    snowball_quality = int(input("quality of snowball: "))

    snowball_value.append((snowball_weight / snowball_time) ** snowball_quality)
    snowball_maxweight.append(snowball_weight)
    snowball_maxtime.append(snowball_time)
    snowball_maxquality.append(snowball_quality)


sort = sorted(snowball_value, reverse=True)
print()
