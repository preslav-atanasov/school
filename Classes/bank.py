account_holders = []
balances = []
transactions = {}

MAX_LOAD_AMOUNT = 10000
INTEREST_RATE = 0.03

class Bank:

    def __init__(self):
        self.name = input("Въведете името на титуляра на сметката (създаване на акаунт): ")

    def create_account(self):
        name = self.name
        if name not in account_holders:
            account_holders.append(name)
            balances.append(0)
            transactions[account_holders.index(name)] = []  # Initialize an empty transaction list for the new account
            print(f"Сметката е създадена за {name}.")
        else:
            print("Сметката вече съществува.")
        return account_holders, balances, transactions  # Added transactions to return statement

    def deposit(self):
        name = self.name
        if name in account_holders:
            index = account_holders.index(name)
            amount = float(input("Сума за внасяне: "))
            if amount <= 0:
                print("Грешка. Моля въведете положително число.")
                exit()
            balances[index] += amount
            transactions[index].append(f"+{str(amount)} лв.")
            print(f"Новият баланс за {name}: {balances[index]:.2f}")
        else:
            print("Сметката не съществува.")
        return balances, transactions

    def withdraw(self):
        name = self.name
        if name in account_holders:
            index = account_holders.index(name)
            amount = float(input("Сума за изнасяне: "))
            if 0 < amount <= balances[index]:
                balances[index] -= amount
                transactions[index].append(f"-{str(amount)} лв.")
                print(f"Новият баланс за {name}: {balances[index]:.2f}")
            else:
                print("Не са налични достатъчно средства.")
        else:
            print("Сметката не съществува.")
        return transactions

    def checkbal(self):
        name = self.name
        if name in account_holders:
            index = account_holders.index(name)
            print(f"Текущият баланс за {name}: {balances[index]:.2f}")
        else:
            print("Сметката не съществува.")
        return

    def transactionhistory(self):
        name = self.name
        if name in account_holders:
            index = account_holders.index(name)
            if transactions[index]:  # Check if there are any transactions
                for transaction in transactions[index]:
                    print(transaction)
            else:
                print("Няма транзакции.")
        else:
            print("Сметката не съществува.")


bank = Bank()
bank.create_account()
bank.deposit()
bank.withdraw()
bank.transactionhistory()
