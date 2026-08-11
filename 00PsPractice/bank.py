class bank:
    balance = 0
    def __init__(self, balance = 0 , name="" , pin=0):
         self.name = name
         self.pin = pin
         
    def initialBal(self , balance):
        self.balance = balance
        
    def show(self):
        print("your name in bank is ::" , self.name)
        print("your  current Balance is ::" , self.balance)    
         
    def deposit(self,deposit):
        self.balance = self.balance + deposit
        print("sucess")
        print("your  current Balance is ::" , self.balance)  
    
    def withdraw(self , withdraw):

        if amt <= self.balance:
            self.balance = self.balance - withdraw
            print("succes")
            print("your  current Balance is ::" , self.balance)  
        else:
            print("invalid amt")
    
acchold1 = bank(name="raj" ,pin= 1234)
acchold2 = bank(name="raman" ,pin= 9862)
acchold3 = bank(name="charan" ,pin= 8726)



act_holder = [
   acchold1 , acchold2 , acchold3
]
name = input("enter your name:")
pin = int(input("enter your pin:"))
    
allow = False
user = None
for account in act_holder:
    if account.name == name and account.pin == pin:
      print("verified")
      user = account
      allow=True
      break;
    else:
      print("not verified")


if(allow):
    
  while True:
    print("press 1 for deposit")
    print("press 2 for withdraw")
    print("press 3 for show")
    print("press 0 for exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        amt = int(input("enter your deposit amt:"))

        user.deposit(amt)

    elif choice == 2:
        amt = int(input("enter your withdraw amt:"))

        user.withdraw(amt)

    elif choice == 3:
        user.show()

    elif choice == 0:
        break

    else:
        print("wrong choice")
        
else:
    print("not allowed");