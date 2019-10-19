class Account:
    __balance = 0
    def __init__(self, balance):
        self.__balance = balance
        
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amt):
        if amt > 0:
            self.__balance = self.__balance + amt
            return True
        else:
            return False
        
    def withdraw(self, amt):
        if amt < self.__balance:
            self.__balance = self.__balance - amt
            return True
        else:
            return False
 
class Customer:
    __fname = ""
    __lname = ""
    __account = Account(5000)
    
    def __init__(self, fn, ln):
        self.__fname = fn
        self.__lname = ln
    
    def getFirstName(self):
        return self.__fname
        
    def getLastName(self):
        return self.__lname
        
    def getAccount(self):
        return self.__account
        
    def setAccount(self, acct):
        self.__account = acct

class Bank:
    customer = Customer("","")
    index = ""
    bankName = ""
    
    def __init__(self, bankName):
        self.bname = bankName
        self.customer_list = []
    
    def addCustomer(self, customer):
        self.customer_list.append(self.customer)
        print(self.customer_list)
        
    def getNumOfCustomers(self):
        self.total_cust = len(self.customer_list)
        return self.total_cust
        
    def getCustomer(self, index):
        self.customer_index = self.customer_list[index]
        return self.customer_index


def MainMenu():
    bn = input("Enter bank name: ")
    print("Welcome to ", bn)    
    print("1. Admin Menu")
    print("2. Customer Menu")
    
    option = int(input("Which Menu would you like to acess? "))
    
    if option == 1:
        adminMenu()
    elif option == 2:
        customerMenu()
    else:
        print("Invalid choice. Enter 1 or 2.")
        MainMenu()
        
print("Thank you, See you next time!!")


def adminMenu(): 
    fn = str(input("Enter customer's first name: "))
    ln = str(input("Enter customer's last name: "))    
    customer = Customer(fn, ln)
    bank = Bank(customer)
    
    print("1. Add Customer")
    print("2. Display number of customers")
    print("3. Check Customer's info")
    print("4. Quit")
    
    admn_option = int(input("What would you like to? "))
    
    while True:
        if admn_option == 1:
            bank.addCustomer(customer)
            admn_option = int(input("What would you like to next? "))
            
        elif admn_option == 2:
            bank.getNumOfCustomers()
            print(bank.getNumOfCustomers())
            admn_option = int(input("What would you like to next? "))
        
        elif admn_option == 3:
            index = int(input("Enter customer's id: "))
            bank.getCustomer(index)
            admn_option = int(input("What would you like to next? "))
        
        elif admn_option >= 5:
            print("Invalid choice. Enter 1-4.")
            adminMenu()
        
        elif admn_option == 4:
            break
    print("Goodbye!")
    
                
def customerMenu():
    fn = str(input("Enter customer's first name: "))
    ln = str(input("Enter customer's last name: "))    
    customer = Customer(fn, ln)
    bank = Bank(customer)
    
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Quit")
    
    account = Account()
    cust_option = int(input("What would you like to do? "))
    
    while True:
        if cust_option == 1:
            deposit = int(input("Enter the amount you wish to withdraw: "))
            bank.Account(account + deposit).getBalance()
            
        elif cust_option == 2:
            withdraw = int(input("Enter the amount you wish to withdraw: "))
            bank.Account(account - withdraw).getBalance()
            
        elif cust_option == 3:
            bank.getCustomer(customer)
        
        elif cust_option >= 5:
            print("Invalid choice. Enter 1-4.")
            customerMenu()
        
        elif cust_option == 4:
            break
    print("Goodbye!")
 
MainMenu()

c1 = Customer("John", "Wick")
c2 = Customer("Mother", "Nature")
c3 = Customer("Help", "Me")
bank = Bank("BCA")
bank.addCustomer(c3)
         
    


    
    