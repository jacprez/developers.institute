class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount

    def withdraw(self, withdrawal_amount):
        if self.balance > withdrawal_amount:
            self.balance -= withdrawal_amount
        else:
            print("Insufficient funds.")


class Owner(BankAccount):
    def __init__(self, owner, balance, credit_card_number, password):
        super().__init__(owner, balance)
        self.credit_card_number = credit_card_number
        self.password = password

    def check_owner_info(self):
        for i in range(2):
            ccn = int(input("Credit card number: "))
            passw = input("Password: ")
            if self.password == passw:
                answer = input("Do you want to deposit or withdraw? ")
                if answer == 'deposit':
                    money = int(input("Money: "))
                    self.deposit(money)
                    return
                elif answer == 'withdraw':
                    money = int(input("Money: "))
                    self.withdraw(money)
                    return
                else:
                    print("I don't understand.")
            else:
                print("wrong password.")

