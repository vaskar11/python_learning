import sys
class Customer:
    '''this is Bank system'''
    bankname='ACEM'
    def __init__(self,name, balance=0.0):
        self.name= name
        self.balance= balance
        
    def deposit(self, amt):
        self.balance= self.balance+ amt
        print('New balance after deposit is: ', self.balance)
        
    def withdraw(self,amt):
        if amt>self.balance:
            print('Insuffient balance. Please deposit first')
            sys.exit()
        else:
            self.balance= self.balance-amt
            print('New balance after withdrawl is: ', self.balance)
print()
print('#'*50)
print("Welcome to ACEM Bank")
print('#'*50)
name= input('Enter your name: ')
c= Customer(name)
while True:
    print('d- Deposit \n w- Withdrawal \n e- Exit')
    option = input('Enter your option: ')
    if option.lower() == 'd':
        amt= int(input('Enter the amount that you want to deposit: '))
        c.deposit(amt)
    elif option.lower() == 'w':
        amt= int(input('Enter the amount that you want to withdraw: '))
        c.withdraw(amt)
    elif option.lower() == 'e':
        print('Thank you for using our service.')
        sys.exit()
    else:
        print('Invalid option. Please select correct option')
