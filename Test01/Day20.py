from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass
    

#     def A (self):
#         pass
    
    
    

# class Rectangle(Shape):
    
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    

# r = Rectangle(10, 5)

# print("Area :", r.area())



#Abstract class
class ATM(ABC):
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def check_b(self):
        pass
    
#concrete class
class BankATM(ATM):
    
    def __init__(self, balance):
        self.__balance = balance
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return F"Withdrawal Successful, remaining balance: {self.__balance}"
        else:
            return "Insufficient balance"
        
    
    def check_b(self):
        return F"Your balance: {self.__balance}"



atm = BankATM(10000)

print(atm.check_b())
print(atm.withdraw(5000))
print(atm.check_b())