students = []

def addStudent(name, roll, city):
    student = {"name": name, "roll": roll, "city": city}
    students.append(student)
    print("Student added successfully")


def viewStudents():
    if not students:
        print("No students found")
    else :
        for s in students:
            print(F"Name: {s['name']}, Roll number: {s['roll']}, City: {s['city']}")

def searchStudent(roll):
    for s in students:
        if s['roll'] == roll:
            return s
    return None

def updateStudent(roll, new_city):
    student = searchStudent(roll)
    if student:
        student["city"] = new_city
        print("City updated successfully")
        viewStudents()
    else:
        print("Student not found")

def deleteStudent(roll):
    # global students
    # students = [ s for s in students if s['roll'] != roll]
    # print("Student deleted Successfully")
    # student = searchStudent(roll)
    
    student = searchStudent(roll)
    
    students.remove(student)
    print("Student deleted")
    
    
        




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
        roll = int(input("Enter roll number to search: "))
        student = searchStudent(roll)
        if student:
            print(F"Roll number: {student['roll']}, Name : {student['name']}, City: {student['city']} ")
        else:
            print("Student not found")
            
    elif choice == 4:
        roll = int(input("enter roll number to update: "))
        new_city = input("enter new city: ")
        updateStudent(roll, new_city)
        
    elif choice == 5:
        roll = int(input("enter roll number to delete: "))
        deleteStudent(roll)
        
    elif choice == 6:
        print("Thank You")
        break
    
    else:
        print("Invalid choice")