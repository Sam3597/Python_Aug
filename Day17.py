# import os

# print(os.getcwd())

# os.mkdir("Test01")

# import sys

# print(sys.version)
# print(sys.platform)


# import statistics

# data = [10,20,30,40,50]

# print(statistics.mean(data))
# print(statistics.median(data))


# import calendar

# print(calendar.month(1999, 9))


# import Calc

# print(Calc.Multi(10, 21))


from Test01 import math, string
import Test01

print(math.Add(5,3))
print(string.greet("Sam"))
print(Test01.x)

