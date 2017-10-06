from bank2 import Banking
class BankingExpress(Banking):
    def in_transfer(self,sender,receiver,amount):
        #get withdraw record

        if self.withdraw(sender,amount):
            self.deposit(receiver,amount)







newaccount=BankingExpress("diamond")
newaccount.in_transfer('daniel','tayo' ,40000)
