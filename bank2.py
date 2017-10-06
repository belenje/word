
























































import random
class Banking():
    balance = 0.0
    def __init__(self,bankname):
        self.bankname=bankname
    def generate_accn(self,prefix,length):
        acn=""
        for x in range (length-2):
            acn+=str(random.randrange(9))

        acn=str(prefix)+acn
        return acn

    def createaccount(self,name,phone,email):
        acn=self.generate_accn(self.bankname[:2],10)
        act_def={'name':name,'phone':phone,'email':email,'accn':acn}

        newfile=open("acc_rec.txt",'w')
        newfile.writelines(act_def)
        newfile.close()
        return act_def

    def deposit(self,accn,amount):
        #retrieve records.
        account_rec=open("acct_rec.txt",'r')
        records= account_rec.readline()
        print(records)
        self.balance +=amount
        return self.balance
    def withdraw(self,acn,amount):
        if self.balance<amount:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("you have withdrawn",amount,"and your balance,is",self.balance)
        return self.balance
#newaccount = Banking("Diamond")
#print(newaccount.createaccount ("onyeforo benjamin","08147616728","umezurikebelenje101@gmail.com"))    
    
