class Teacher:
    
    def __init__(self):
        self._name = "Sam" #_Teacher__name
        
    def subject(self):
        print("Teacher teaches Math")


class Student(Teacher):
    def name(self):
        print(self._name)
        print("student name is Sam")


s = Student()

s.subject()
s.name()


# class Programmer:
#     def coding(self):
#         print("i know coding in python")

# class Designer:
#     def designing(self):
#         print("i know designing")
        
# class Employee(Programmer, Designer):
#     def role(self):
#         print("Hello i am sam")
        

# e = Employee()

# e.coding()
# e.designing()
# e.role()




# class A:
#     def method_a(self):
#         print("this is A Class")

# class B(A):
#     def method_b(self):
#         print("this is B Class")
        
# class C(B):
#     def method_c(self):
#         print("this is C Class")
        


# c = C()

# b = B()


# c.method_a()
# c.method_b()
# c.method_c()





# class BankAccount:
#     def account_type(self):
#         print("this is a bank account")
        
# class SavingAccount(BankAccount):
#     def interest(self):
#         print("Saving account gives 4% interest")

# class CurrentAccount(BankAccount):
#     def overdraft(self):
#         print("Current account allows overdraft")
    



# s = SavingAccount()

# c = CurrentAccount()

# s.account_type()
# s.interest()

# c.account_type()
# c.overdraft()


# #Hybrid


# class Person:
#     def info(self):
#         print(" I am a person")

# class Student(Person):
#     def study(self):
#         print("I study different subjects")
        
# class Teacher(Person):
#     def teach(self):
#         print("I tech math")

# class TeachingA(Student, Teacher):
#     def role(self):
#         print(" iam both a student and teaching assistant")
        
# TA = TeachingA()

