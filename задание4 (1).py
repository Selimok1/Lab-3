class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(('deposit', amount))
        else:
            print("Ошибка: сумма должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(('withdraw', amount))
        else:
            print("Ошибка: недостаточно средств или неправильная сумма.")

    @property
    def balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions


if __name__ == "__main__":
    account = BankAccount()
    account.deposit(100)
    account.withdraw(30)
    print(f"Баланс: {account.balance}")
    print("Транзакции:", account.get_transactions())
