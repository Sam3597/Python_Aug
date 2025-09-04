# def function_name (name, a, b):
#     return F"Hello {name} addition is {a + b}"
    

# name = 'Sam' 

# A = 10
# B = 5   
# print(function_name("Sam", 10, 5))



# def check_even_odd(num):
#     if num % 2 == 0:
#         return "num is even"
#     else:
#         return "num is odd"
    

# print(check_even_odd(11))



# def check_sum(numbers):
#     sum1 = min(numbers)
    
#     return sum1


# num = [10,5,4,6,8,10]

# print(check_sum(num))  




# def bill(units):
    
#    if units <=100:
#        return units*5
#    elif units <=200:
#        return (100 * 5) + (units - 100) * 7
#    else:
#        return (100 * 5) + (100 * 7) + (units -200) * 10
   
   
# print(bill(201))



def atm(balance, amount):
    if amount > balance:
        return "insufficient fund"
    else:
        balance -= amount     
        
        return F"withdrawal successful, remaining balance is {balance}"



print(atm(10000, 11000)) 
    
    
    