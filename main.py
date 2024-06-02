class Bank_Account():
    def __init__(self, Name, key, balance):
        self.account_name = Name
        self.account_number = key
        self.balance = float(balance)
    def deposit(self):
        amount = float(input("Enter The amount you want to deposit: "))
        if amount > 0:
            self.balance  +=  amount
            print(f"You Deposited {amount} , The Total balance now is {self.balance}")
        else:
            print("Amount should be greater than zero")
    def withdrawl(self):
        amount_1 = input("Enter The amount you wnat to withdraw:")
        if int(amount_1) > 0:
            self.balance -= int(amount_1)
            print(f"You withdraw {amount_1}, The balance now is {self.balance}")
        else:
            print("Withdrawl amount should be sufficent balance")
    def check_balance(self):
        print(f"Your balance is {self.balance}")
    
def display_menu():
    print("1.DEPOSIT")
    print("2.WITHDRAWL")
    print("3.CHECK BALANCE")
    print("4.Quit")
display_menu()
accounts = {}
while True:
    choice = input("Enter Your Choice {1} {2} {3} {4}: []")
    account_name = input("Enter Your Name: ")
    account_number = input("Enter Account Number: ")
    account_balance = float(input("Enter Your Balance: "))
    obj1 = Bank_Account(account_name, account_number, account_balance)
    if choice == "1":
        obj1.deposit()
    elif choice == "2":
        obj1.withdrawl()
    elif choice == "3":
        obj1.check_balance()
    else:
        quit
