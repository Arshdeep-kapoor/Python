class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=0):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
        
    def getid(self):
        return self.__id
    
    def setid(self,id):
        self.__id=id
    
    def getbalance(self):
        return self.__balance
    
    def setbalance(self,balance):
        set.__balance=balance
    
    def getannualInterestRate(self):
        return self.__annualInterestRate
    
    def setannualInterestRate(self,annualInterestRate):
        self.__annualInterestRate=annualInterestRate
    
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate/1200)
    
    def getMonthlyInterest(self):
        return (self.__annualInterestRate/1200)*self.__balance
    
    def withdraw(self,amount):
        self.__balance-=amount
        return (self.__balance)
    
    def deposit(self,amount):
        self.__balance+=amount
        return (self.__balance+amount)

Account=Account(1122,20000,4.5)

Account.withdraw(2500)
Account.deposit(3000)

print("the id of the account is",Account.getid())
print("the balance of the account is ", Account.getbalance())
print("the monthly rate is", Account.getMonthlyInterestRate())
print("the monthly interest is", Account.getMonthlyInterest())