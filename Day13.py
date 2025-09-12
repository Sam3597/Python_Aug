#Reduce()

# [1,2,3,4,5]

# [3,7,5]


# [10,5]

# [15]


from functools import reduce

# num = [1,2,3,4,5]

# result = reduce(lambda a,b : a + b, num)

# print(result)

# num = [5,8,2,10,3]

# [8,10,3]
# [10,3]
# [10]

# maximum = reduce(lambda a,b : a if a > b else b, num)

# print(maximum)

#zip()

# names = ['sam', 'suraj', 'rahul','ram', 'vishal']


# ages = [27,22,28,45]

# info = list(zip(names, ages))

# print(info)

# for name, age in info :
#     print(name, "is", age)




#Recusrion

# def countdown(n):
#     if n == 0:
#         print("Times up")
#     else:
#         print(n)
#         countdown(n-1)


# countdown(10)





# file = open("data.txt", "w")

# 'w'
# 'a'
# 'x'
# 't'

# file = open("newFile.txt", "w")
# file.write("\ Hello There")
# file.write("Hello Python \n")
# file.close()


# file = open("newFile.txt", "r")

# data = file.read()

# print(data)

# file.close()
