age = 19
has_id = True

# if age >= 18 :
#   if has_id:
#         print("Eligible for voting")
#   else:
#         print("Get an ID")
# else:
#     print("you are not eligible")
        
    
# marks = 80

# if marks >= 90:
#     print('A')
#     print("good")
# elif marks >= 70 and marks < 90:
#     print('B')
# elif marks >= 50 and marks <70:
#     print('C')
# else:
#     print('D')
  
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

operator = input("Enter operator from '+,-,/,*'")

if operator == "+" :
    print(F"Addition : {num1 + num2}")
elif operator == "-":
    print("Substraction: ", num1 - num2)
elif operator == "/":
    if num2 != 0:
      print("Division :", num1/num2)
    else:
        print("Division by 0 is not possible")
elif operator == "*":
    print("Multi :", num1 * num2)
else:
    print("Invalid Operator")
