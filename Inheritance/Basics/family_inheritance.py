class Grandfather:
    def inheritance(self):
        return f"a pagani zonda"


class Father(Grandfather):

    def inheritance1(self):
        return f"an apartment in sofia"


class Son(Father):
    def property(self):
        return f"10 leva v djoba"

son = Son()
print(son.inheritance())
print(son.inheritance1())
print(son.property())