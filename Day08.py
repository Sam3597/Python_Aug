# for i in range(1,5):
#     if i == 3:
#        pass
#     print(i)


# for num in range(1,4):
#     if num == 3:
#         break
#     print(num)

# else:
#     print("Loop completed")


# num = 1

# while num <= 10:
#     if num == 5:
#        num +=1
#        continue
#     print(num)
#     num +=1
    

# else:
#     print("Loop finished")



# products = ['pen', 'pencil', 'book',]
# search = 'marker'

# for i in products:
#     if i == search:
#         print("Product found :", i)
#         break
# else:
#     print("Product is not available")


# while True:
#     pwd = input("Enter a password (min 6 Chars) :")
#     if len(pwd) < 6:
#         print("password is too short, Try Again")
#         continue
#     print("Password accepted")
#     break


# while True:
#     print("Calculator Menu")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
    
    
#     choice = input("Enter your choice (1-5) :")
    
#     if choice == "5":
#         print("Exiting the calculator..")
#         break
    
#     num1 = int(input("Enter first number :"))
#     num2 = int(input("Enter Second number :"))
    
#     if choice == "1":
#         print("Addition :", num1 + num2)
#     elif choice == "2":
#         print("Subtraction :", num1 - num2)
#     elif choice =="3":
#         print("Multiplication :", num1 * num2)
#     elif choice == "4":
#         if num2 != 0:
#            print("Division :", num1 / num2)
#         else:
#             print("Division by 0 is not possible")
#     else:
#         print("Invalid Choice")
    
    

num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num //= 10
print("Reversed =", rev)
        
    