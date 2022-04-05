class User:
    def __init__(self,name,int_rate,start_bal):
        self.username=name
        self.account=BankAccount(int_rate,start_bal)

    def deposit(self,amount):
        self.account.deposit(amount)
        return self

    def withdraw(self,amount):
        self.account.withdraw(amount)
        return self

    def transfer(self,other_user,amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self
    def display_user(self):
        print(f"Name:{self.username}")
        self.account.display_account_info()
        return self


class BankAccount:
    all_accounts=[]
    def __init__(self, int_rate, balance=0): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}  Interest Rate:{self.int_rate}")
        return self
    def yield_interest(self):
        self.balance*=(self.int_rate+1)
        self.balance=int(self.balance)
        return self
    @classmethod
    def display_all(cls):
        for i in BankAccount.all_accounts:
            print(f"Balance:{i.balance}  Interest Rate:{i.int_rate}")
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


dan=User("Dan",0.1,100)
timmy=User("Timmy",0.2,200)

dan.deposit(100).withdraw(100).transfer(timmy,50)
dan.account.yield_interest()
dan.display_user()
timmy.display_user()
