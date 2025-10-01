# class MyError(Exception):
#     pass


# try:
#     raise MyError("Something went wrong")

# except MyError as e:
#     print("this is custom exception", e)



# class AgeTooSmallError(Exception):
#     pass

# class AgeTooLargeError(Exception):
#     pass


# try:
#     age = int(input("Enter your age :"))
#     if age < 18:
#         raise AgeTooSmallError("Age is too small..")
#     elif age > 80:
#         raise AgeTooLargeError("Age is too large")
#     else:
#         print("Valid age", age)

# except (AgeTooSmallError, AgeTooLargeError) as e:
#     print("Error :", e)
    
# except ValueError:
#     print("Please enter a valid number..")





# class InsufficientFundError(Exception):
#     pass

# balance = 5000

# try:
#     amount = int(input("Enter amount to withdraw :"))
#     if amount > balance:
#         raise InsufficientFundError("Not enough balance to withdraw")
#     else:
#         balance -= amount
#         print("Withdraw success..")

# except InsufficientFundError as e:
#     print("Error :", e)

# except ValueError:
#     print("Please enter amount only")



# age = int(input("Enter your age :"))

# if age < 18:
#     raise ValueError("Age must be 18 years or more")
# else:
#     print("You are eligible")
    

# try:
#     age = int(input("Enter your age :"))
#     if age < 18:
#        raise ValueError("Age must be 18 years or more")
# except ValueError as e:
#     print("Error :", e)


print( True and False)