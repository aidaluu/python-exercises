class Customer:
    """Customer class with basic customer info"""
    name = ""
    
    def __init__(self):
        self.name = input("Customer name: ")
        
    def info(self):
        print("I am parent class.")
        
class Account(Customer):
    """Customer's account class, with account info"""
    
    accountNumber = ""
    bonusPoints = 0
    
    def __init__(self):
        self.accountNumber = input("Account number: ")
        
    def newBonus(self):
        self.bonusPoints += 1
    
    def info(self):
        print("I am child class.")

def main():
    newCustomer = Customer()
    customerAccount = Account()
    
    newCustomer.info()
    customerAccount.info()
    
    print(newCustomer.name)
    
    print(customerAccount.accountNumber)
    customerAccount.newBonus()
    print(customerAccount.bonusPoints)
    
    print(newCustomer.__doc__)
    print(customerAccount.__doc__)
    
if __name__ == "__main__":
    main()