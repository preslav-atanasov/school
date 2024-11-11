class CreditCard:
    def __init__(self, number:int, holder_name:str, cvv:int, exp_date:str, pin:int):
        self.number = number
        self.holder_name = holder_name
        self.cvv = cvv
        self.exp_date = exp_date
        self.__pin = pin    # __ defines the attribute as private


visa = CreditCard(1829374027492834, "Lorem Ipsum", 343, "11/11/2024", 3483)
print(visa.number)
print(visa._CreditCard__pin)

