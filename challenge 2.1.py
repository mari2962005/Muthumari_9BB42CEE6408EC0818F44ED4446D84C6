class Bankaccount:
 def  __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name 
    self.__account_balance = initial_balance

 def deposit(self, amount):
   if amount>0:
    self.__account_balance += amount
    print("Deposit â‚¹{}. New balance â‚¹{}".format(amount,self.__account_balance))
   else:
    print("Invaild deposit amount.")

 def withdraw(self, amount):
  if amount>0 and amount<=self.__account_balance:
    self.__account_balance -= amount
    print("Withdraw â‚¹{}. New balance â‚¹{}".format(amount,self.__account_balance))
  else:
    print("Invaild withdrawl amount or insufficient account balance.")

 def display_balance(self):
  print("Account balance for {} (account #{}):â‚¹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))


account = Bankaccount(account_number="123455678",account_holder_name="Hajira",initial_balance=5000.0)

account.display_balance()
account.deposit(1000)
account.withdraw(200)
account.withdraw(10000)
account.display_balance()