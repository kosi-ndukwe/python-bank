import pickle
import os
import pathlib

#bank account class
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def create_account(self):
        self.accNo= int(input("Enter the new account number: "))
        self.name = input("Enter the new account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current: $"))
        print("\n\n\nAccount Created")
    
    def show_account(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modify_account(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance : $"))
        
    def deposit_amount(self,amount):
        self.deposit += amount
    
    def withdraw_amount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def get_accNo(self):
        return self.accNo
    def get_accName(self):
        return self.name
    def get_accType(self):
        return self.type
    def get_deposit(self):
        return self.deposit
    
#function to display an intro screen
def start(): 
    print("*"*80)
    print("BANK MANAGEMENT SYSTEM".center(80))
    print("*"*80)

    print("Press the Enter key to continue.".center(80))
    input()


#these functions manipulate the data inside the 'accounts.data' file
def write_account():
    account = Account()
    account.create_account()
    write_accounts_file(account)

def display_all():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " $",item.deposit )
        infile.close()
    else :
        print("No records to display")
        

def display_sp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account balance is = $",item.deposit)
                found = True
    else :
        print("No records to search.")
    if not found :
        print("There is no existing account with this number.")

def deposit_and_withdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("\tEnter the amount to deposit: $"))
                    item.deposit += amount
                    print("\nYour account is updated.")
                elif num2 == 2 :
                    amount = int(input("\tEnter the amount to withdraw: $"))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("\nYou don't have enough funds.")
                
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def delete_account(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modify_account(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : $"))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def write_accounts_file(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# start of the program
ch=''
num=0
start()

while ch != 8:
    print("*"*80)
    print("MAIN MENU".center(80))
    print("1. NEW ACCOUNT".center(80))
    print("2. DEPOSIT AMOUNT".center(80))
    print("3. WITHDRAW AMOUNT".center(80))
    print("4. BALANCE ENQUIRY".center(80))
    print("5. ALL ACCOUNT HOLDER LIST".center(80))
    print("6. CLOSE AN ACCOUNT".center(80))
    print("7. MODIFY AN ACCOUNT".center(80))
    print("8. EXIT".center(80))
    print("Select Your Option (1-8)".center(80))
    ch = input()
  
    
    if ch == '1':
        write_account()
    elif ch =='2':
        num = int(input("\tEnter the account no. : "))
        deposit_and_withdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter the account no. : "))
        deposit_and_withdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter the account no. : "))
        display_sp(num)
    elif ch == '5':
        display_all();
    elif ch == '6':
        num =int(input("\tEnter the account no. : "))
        delete_account(num)
        print("The account has been deleted.")
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modify_account(num)
    elif ch == '8':
        print("\tThanks for using the Bank Management System!".center(80))
        print("Goodbye!".center(80))
        break
    else :
        print("Invalid choice.")
    
    ch = input("\nPress the Enter key to continue.\n")
    


    
    
    
    
    
    
    
    
    
    
