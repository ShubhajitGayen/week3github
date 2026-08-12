class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account after checking the available balance."""
        if amount > self.balance:
            print("Withdrawal not possible: Insufficient funds")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        """Display the current account balance."""
        print(f"Account Holder: {self.name} | Current Balance: ${self.balance:.2f}")


def main():
    account_1 = BankAccount("Sudip", 800.0)
    account_1.display_balance()

    account_1.deposit(900.0)
    account_1.display_balance()
    account_1.withdraw(200.0)
    account_1.display_balance()

    print("-" * 40)

    account_2 = BankAccount("Suman", 700.0)
    account_2.display_balance()
    
    account_2.withdraw(1000.0) 
    
    print("-" * 40)

    account_3 = account_1
    account_3.display_balance()

    account_3.deposit(900.0)
    account_1.display_balance()

    account_3.withdraw(200.0)
    account_3.display_balance()


if __name__ == '__main__':
    main()
