import random

names=["We", "I", "They", "He", "She", "Jack", "Jim"]
verbs=["was", "is", "are", "were"]
nouns=["playing a game", "watching television", "talking", "dancing", "speaking"]

while True:
    a = (random.choice(names))
    b = (random.choice(verbs))
    c = (random.choice(nouns))
    print(a + " ", b + " ", c)
    break
