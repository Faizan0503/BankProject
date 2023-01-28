class BankAccount:
    account_number = 1001

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = BankAccount.account_number
        BankAccount.account_number += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Insufficient balance")

def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    return BankAccount(name, balance)

def main():
    accounts = {}
    bank_name = "NextGen Bank"
    print("\n**************** Welcome to", bank_name,"***************")
    while True:
        print("\n===============================")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        print("===============================")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            account = create_account()
            accounts[account.account_number] = account
            print("\n********************************")
            print(f"Account created successfully!!")
            print(f"Account number: {account.account_number}")
            print("********************************")
        elif choice == 2:
            if accounts:
                account_number = int(input("Enter account number: "))
                if account_number in accounts:
                    amount = float(input("Enter the amount to deposit: "))
                    accounts[account_number].deposit(amount)
                    print("\n********************************")
                    print(f"Amount deposited in account number {account_number}")
                    print("********************************")
                else:
                    print("\nNo such account found.")
            else:
                print("\nNo accounts found. Please create an account first.")
        elif choice == 3:
            if accounts:
                account_number = int(input("Enter account number: "))
                if account_number in accounts:
                    amount = float(input("Enter the amount to withdraw: "))
                    accounts[account_number].withdraw(amount)
                    print("\n********************************")
                    print(f"Amount withdrawn from account number {account_number}")
                    print("********************************")
                else:
                    print("\nNo such account found.")
            else:
                print("\nNo accounts found. Please create an account first.")
        elif choice == 4:
            if accounts:
                account_number = int(input("Enter account number: "))
                if account_number in accounts:
                    account = accounts[account_number]
                    print(f"\nAccount holder name: {account.name}")
                    print(f"Account number: {account.account_number}")
                    print("\n********************************")
                    print(f"Current balance: {account.balance}")
                    print("********************************")
                else:
                    print("\nNo such account found.")
            else:
                print("\nNo accounts found. Please create an account first.")
        elif choice == 5:
            break
        else:
            print("\nInvalid choice. Please try again.")
    print("\n********************************")        
    print("Thank you for using", bank_name)
    print("********************************")
main()
