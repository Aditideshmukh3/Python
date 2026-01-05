# class Bank:
#     def __init__(self, name, account_number, balance):
#         self.name = name                
#         self.account_number = account_number  
#         self.balance = balance
#     def display(self):
#         print("Account Holder Name : ", self.name)
#         print("Account Number is : ", self.account_number)
#         print("Account Balance is : ", self.balance)

# b = Bank("John", "12345", 50000)
# b.display()
# b.account_number = 34567
# b.display() - This will change the account number

# b.balance = 0
# b.display() - This will change the balance which is not desired
# To prevent this we use encapsulation .

# Encapsulation Example in Python :

class Bank:
    def __init__(self, name, account_number, balance):
        self.name = name                
        self.account_number = account_number  
        self.__balance = balance
    def display(self):
        print("Account Holder Name : ", self.name)
        print("Account Number is : ", self.account_number)
        print("Account Balance is : ", self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdrawal(self, amount):
        self.__balance -= amount

    def updated(self):
        print("Updated Balance is : ", self.__balance)

            
b = Bank("John", "12345", 50000)
b.display()
# b.__balance = 0
# b.display() - This will not change the balance as it is private now
b.deposit(3000)
b.updated()
b.withdrawal(2000)
b.updated()