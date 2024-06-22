class HDFC:
    ROI = 9.5

    def __init__(self,Name,Amount):
        self.AccountHolder = Name
        self.Balance = Amount
        print("Welcome ",self.AccountHolder)
        print( self.AccountHolder + " Your Account gets successfully created with initial balance",self.Balance)

    def DisplayBalance(self):
        print("Hello ",self.AccountHolder)
        print("Your account balance is  : ",self.Balance)

    @classmethod
    def DisplayBankInfo(cls):
        print("Welcome to HDFC bank portal")
        print("Our bank is PVT LTD bank")
        print("We provide the Rate of Interest on saving account is : ",cls.ROI)

    @staticmethod
    def DisplayKYCInfo():
        print("According to the rules of RBI you should provide below documents for KYC")
        print("Your Aadhar card")
        print("Your PAN card")
        print("Your Passport size photo")

    def Withdraw(self,Amount):
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance = self.Balance-Amount
            print("Amount withdrawl successfully...")
    
    def Deposit(self,Amount):
        self.Balance = self.Balance + Amount
        print("Amount Deposited successfully...")

def main():
    print("Rate of HDFC back is : ",HDFC.ROI)

    HDFC.DisplayBankInfo()

    HDFC.DisplayKYCInfo()
    
    print("Creating new account..")
    Amit = HDFC("Amit",5000)

    print("Creating new account..")
    Sagar = HDFC("Sagar",3000)

    print("Performing opearations on obj1")
    Amit.Deposit(2000)
    Amit.DisplayBalance()
    
    Amit.Withdraw(1000)
    Amit.DisplayBalance()

    print("Performing opearations on Sagar's Account")
    Sagar.Deposit(4000)
    Sagar.DisplayBalance()

    Sagar.Withdraw(500)
    Sagar.DisplayBalance()

if __name__ == "__main__":
    main()