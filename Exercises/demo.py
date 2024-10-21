account_holders = []
balances = []
transactions = {}

MAX_LOAD_AMOUNT = 10000
INTEREST_RATE = 0.03


def create_account():
    name = input("Въведете името на титуляра на сметката (създаване на акаунт): ")
    if name not in account_holders:
        account_holders.append(name)
        balances.append(0)
        print(f"Сметката, създадена за {name}.")
    else:
        print("Сметката вече съществува.")


def deposit():
    name = input("Въведете името на титуляра на сметката (внасяне на пари): ")
    if name in account_holders:
        index = account_holders.index(name)
        amount = float(input("Сума за внасяне: "))
        balances[index] += amount
        transactions[index].append(f"+{str(amount)} лв.")
        print(f"Новият баланс за {name}: {balances[index]:.2f}")
    else:
        print("Сметката не съществува.")


def withdraw():
    name = input("Въведете името на титуляра на сметката (изнасяне на пари): ")
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


def checkbal():
    name = input("Въведете името на титуляра на сметката (проверка на баланс): ")
    if name in account_holders:
        index = account_holders.index(name)
        print(f"Текущият баланс за {name}: {balances[index]:.2f}")
    else:
        print("Сметката не съществува.")


def listaccounts():
    for name in account_holders:
        print(name)


def transfer():
    name1 = input("Въведете името на титуляра на сметката от която да се прехвърлят пари: ")
    name2 = input("Въведете името на титуляра на сметката към която да се прехвърлят пари: ")
    if name1 and name2 in account_holders:
        index = account_holders.index(name1)
        index2 = account_holders.index(name2)
        print(f"Текущият баланс за {name1}: {balances[index]:.2f}")
        amount = float(input("Колко ше прехвърляме: "))
        if 0 < amount <= balances[index]:
            balances[index] -= amount
            transactions[index] = f"-{str(amount)} лв."
            index += 1
            balances[index] += amount
            transactions[index] = f"+{str(amount)} лв."
            index -= 1
            print(f"Парите бяха успешно прехвърлени")
            print(f"Новият баланс за {name1}: {balances[index]:.2f}")
            index += 1
            print(f"Новият баланс за {name2}: {balances[index]:.2f}")
        else:
            print("Не са налични достатъчно средства.")
    else:
        print("Една от двете сметки не съществува.")


def transactionhistory():
    name = input("Въведете името на титуляра на сметката (проверка на баланс): ")
    if name in account_holders:
        index = account_holders.index(name)
        for transaction in transactions[index]:
            print(transaction)
    else:
        print("Сметката не съществува.")


create_account()
deposit()
withdraw()
transfer()
transactionhistory()

