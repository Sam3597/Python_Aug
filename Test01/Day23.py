# try:
#    a = int(input("enter a number :"))
#    b = int(input("enter another number :"))
    
#    print("Result :", a / b)
    
# except ZeroDivisionError:
#     print("You cannot divide by zero")


# try:
#     # Code that may cause error

# except ErrorType:
#     # what to do if that error happens

# else:
#     # Runs if no error happens

# finally:
#     # Always runs



# try:
#     num = int(input("Enter a number :"))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Division by zero not possible")

# except ValueError:
#     print("Please enter a number only")

# else:
#     print("Result:", result)

# finally:
#     print("Thank you, program finished")



# mylist = [10,20,30]

# try:
#     index = int(input("Enter index (0 - 2) :"))
#     print("Value: ", mylist[index])

# except IndexError:
#     print("Index out of range")

# except ValueError:
#     print("Please enter a number only")


    
    

# student = {"name": "sam", "age": 25}

# try:
#     key = input("Enter the key: ")
#     print("Result :", student[key])
    
# except KeyError:
#     print("Key not found")


# try:
#     file = open("Data.txt", "r")
#     content = file.read()
#     print(content)
#     file.close()

# except FileNotFoundError:
#     print("File does not exist")



try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result  = num1 / num2
    print(result)

except (ZeroDivisionError, ValueError) as e:
    print("Error occurred", e)
    


