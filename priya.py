classBankAccount:
  def_init_(self,account_number,account_holder_name,initial_balance):

self._account_number=account_number
self._account_holder_name=account_holder_name

self._account_balance=initial_balance
 defdeposit(self,amount):
  ifamount>0:
self._account_balance+=amount
  print("Deposited&{amount}.Newbalance:&{self._account_balance}.")
else:
   print("invalid deposit amount.please enter a positive amount.")
  defwithdraw(self,amount):
    ifamount>0andamount<=self._account_balance:
self._account_balance:
self.account_balance=amount
    print("withdraw&{amount}.Newbalance.&{self._account_balance}")elifamount<=0:
    print("invalid withdrawal amount.please enter a positive amount.")
else:
print("insufficient fund for withdrawal.")
  defdisplay_balance(self):
    print(f"account holder:{self._account_number}")
    print(f"account balance:&self{._account_balance}")
#creating an instance of the Bankaccound class account=bankaccount("1234567890","john doe",1000.0)

#Testing deposit and withdrawal functionality account.display_balance()account.deposit(500.0)account.withdraw(200.0)account.display_balance()
   print("withdraw&{amount
