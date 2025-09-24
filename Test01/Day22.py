# class Dog:
#     def sound(self):
#         return "Bark"
    
# class Cat:
#     def sound(self):
#         return "Meow"
    

# def make_sound(animal):
#     print(animal.sound())
    

# dog = Dog()

# cat = Cat()

# make_sound(cat)


# print(10 + 20)

# print("hello" + "Sam")

# print([1,2] + [3,4])





# class Math:
    
#     # def add(self, a, b):
#     #     return a + b
    
#     def add(self, a = 0, b = 0, c = 0):
#         return a + b + c


# m = Math()

# print(m.add(10,15,10))


# class Animal:
#     def speak(self):
#         return "Animals make sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "Dog Barks"
    


# d = Dog()
# a = Animal()

# print(a.speak()) 
# print(d.speak())    




from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, acc_no, holder, balance = 0):
        self.__balance = balance
        self.acc_no = acc_no
        self.holder = holder
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(F"Deposited {amount}, New Balance is {self.__balance}")
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(F"Withdraw Success{amount}, new balance {self.__balance}")
        else:
            print("Insufficient Balance")
    
    @abstractmethod
    def calculate_interest(self):
        pass
        


class SavingAccount(Account):
       def calculate_interest(self):
           return self.get_balance() * 0.05
       

class CurrentAccount(Account):
       def calculate_interest(self):
           return self.get_balance() * 0.02
       

saving = SavingAccount(101, "Sam", 1000)
current  = CurrentAccount(102, "Rahul", 3000)


# saving.deposit(500)

# saving.withdraw(500)

# current.deposit(500)

print(saving.calculate_interest())

print(current.calculate_interest())

        