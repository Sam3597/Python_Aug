# class Student:
#     school_name = "ABC" #Class Variable
    
#     def __init__(self, name, roll):
        
#         self.name = name #Instance Varibale
#         self.roll = roll #Instance Varibale
        

# s1 = Student("Sam", 1)
# s2 = Student("Rahul", 2)

# print("School name (s1):", s1.school_name)
# print("School name (s2):", s2.school_name)

# print("Student 1:", s1.name, s1.roll)
# print("Student 2:", s2.name, s2.roll)

# Student.school_name = "XYZ"


# print("School name (s1):", s1.school_name)
# print("School name (s2):", s2.school_name)
        
        

# class Student:
    
#     def __init__(self, name, marks):
        
#         self.__name = name
#         self.__marks = marks
        
#     def get_name(self):
#         return self.__name
            
#     def get_marks(self):
#         return self.__marks
        
#     def set_name(self, name):
#         self.__name = name
        
#     def set_marks(self, marks):
#             if marks >= 0 and marks <= 100:
#               self.__marks = marks
#             else:
#                 print("Invalid marks")
                

# s1 = Student("Sam", 80)

# print("Name:", s1.get_name())      
# print("Marks:", s1.get_marks())   

# s1.set_name("Rahul")
# s1.set_marks(101) 

# print("Name:", s1.get_name())      
# print("Marks:", s1.get_marks())      



#Public Variable

# class Student:
#     def __init__(self, name):
#         self.name = name
        
# s = Student("Sam")
# print(s.name)
     

#Protected Variable

# class Student:
#     def __init__(self, name):
#         self._name = name
        
# s = Student("Sam")
# print(s._name)


#Private Variable

class Student:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
        
s = Student("Sam")
print(s.get_name())