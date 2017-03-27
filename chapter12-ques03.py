class Account(object):
    def __init__(self,id):
        self.__id = id
        self.__balance = 100
        self.__annualInterestRate = 0
    def get_id(self):
        return self.__id
    def get_balance(self):
        return self.__balance 
    def get_annual_interest_rate(self):
        return self.__annualInterestRate 
    def set_id(self, ac_id):
        self.__id = ac_id
    def set_balance(self, balance):
        self.__balance = balance
    def set_annual_interest_rate(self, interestRate):
        self.__annualInterestRate = interestRate
    def withdraw(self, amount):
        self.__balance = self.__balance-amount
    def depost(self,amount):
        self.__balance = self.__balance+amount

def main():
    list1 = [0,1,2,3,4,5,6,7,8,9]
    while(True):
        id = eval(input("Enter an account id:"))
        num = 0
        for i in range(len(list1)):
            if (list1[i]==id):
                num=-1
        if (num==0):
            print("Wrong ID entered. Please enter correct ID.")
            continue
        else:
            accObj = Account(id)
            while(True):
                print("Main Menu")
                print("1: Check Balance")
                print("2: Withdraw")
                print("3: Deposit")
                print("4: Exit")
                selection = eval(input("Enter a Choice:"))
                if (selection==1):
                    print("The balance is",accObj.get_balance())
                elif (selection==2):
                    amount = eval(input("Enter an amount to withdraw: "))
                    accObj.withdraw(amount)
                elif (selection==3):
                    amount = eval(input("Enter an amount to deposit: "))
                    accObj.depost(amount)
                elif (selection==4):
                    break
                else:
                    print("Wrong selection.")
                    continue

main()