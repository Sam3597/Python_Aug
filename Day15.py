# name = "sam" #Global Variable

# def hello():
#     name = "sam" #Local Varibale
#     print("hello", name)
    
# def outer():
#     name = "Sam"
    
#     def inner():
        
#         print(name)
#     inner()

# outer()


# count = 0

# def increase():
#     # global count
#     print(count)
#     # count += 1

# increase()

# print(count)
    



# students = []

def addStudent(name, roll, city):
    with open("Students.txt", "a") as file:
        file.write(F"{name}, {roll}, {city}\n")
    print("Student added successfully")


def viewStudents():
    with open("Students.txt", "r") as file:
        data = file.readlines()
        if not data:
            print("No students found")
        else:
            print("\nAll Students")
            for line in data:
                name, roll, city = line.strip().split(',') #'sam, 1, pune' 
                print(F"Name: {name}, Roll: {roll}, City: {city}")
     

def searchStudent(roll_number):
    found = False
    with open("Students.txt", "r") as file:
        for line in file:
          name, roll, city = [x.strip() for x in line.strip().split(',')]  #'sam','1','pune'
          if roll == str(roll_number):
              print(F"Found: Name: {name}, Roll: {roll}, City: {city}")
              found = True
              break
    if not found :
        print("Student not found")

def updateStudent(roll_number, new_city):
    with open("Students.txt", "r") as file:
        data = file.readlines()
    with open("Students.txt", "w") as file:
        updated = False
        for line in data:
            name, roll, city = [x.strip() for x in line.strip().split(',')]  #'1' == '1'
            
            if roll == str(roll_number):
                city = new_city
            
                updated = True
            file.write(F"{name}, {roll}, {city}\n")
    
    if updated:
        
        print(F"Student with roll number {roll_number} updated successfully")
    else:
        print("Student not found")
                    
            
    

def deleteStudent(roll_number):
    with open("Students.txt", "r") as file:
        data = file.readlines()
        
        deleted = False
        
        with open("Students.txt", "w") as file:
            for line in data:
                name, roll, city = [x.strip() for x in line.strip().split(',')]
                
                if roll == str(roll_number):
                    deleted = True
                    continue
                
                file.write(F"{name}, {roll}, {city}\n")
            
            if deleted:
                print(F"Student with roll number {roll_number} deleted successfully")
            else:
                print("Student not found")
        
        
    
    
        




while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        city = input("Enter city: ")
        
        addStudent(name, roll, city)
    
    elif choice == 2:
        viewStudents()
    
    elif choice == 3:
        roll_number = int(input("Enter roll number to search: "))
        student = searchStudent(roll_number)
        
            
    elif choice == 4:
        roll_number = int(input("enter roll number to update: "))
        new_city = input("enter new city: ")
        updateStudent(roll_number, new_city)
        
    elif choice == 5:
        roll_number = int(input("enter roll number to delete: "))
        deleteStudent(roll_number)
        
    elif choice == 6:
        print("Thank You")
        break
    
    else:
        print("Invalid choice")