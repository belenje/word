import random
class Banking():
    balance = 0.0
    def __init__(self, username, phone, email):
        self.username = username
        self.phone = phone
        self.email = email
        self.accN = ""
        
    def randomAccount(self):
        return random.randint(1000000000,9999999999)
               
    def createAccount(self):
        accountnumber = self.randomAccount()
        self.accN = accountnumber
        return self.accN

    def checkbalance(self, accN):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("you have withdrawn ", amount)
            print("your balance is ", self.balance)
        return  self.balance

cust_obj = Banking("frank","08063391178","abc@mail.com")
new = cust_obj.createAccount()
print(new)
cust_obj.withdraw(25000)
cust_obj.deposit(50000)
cust_obj.withdraw(15000)
