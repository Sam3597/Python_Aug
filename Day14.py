file = open ("sample.txt", "w")
file.write("line 1\nline 2\nline 3")
file.close()

# with open("sample.txt", "r") as file :
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())


# with open("sample.txt", "r") as file :
#     print(file.readlines())


with open("sample.txt", "w") as f :
    f.writelines(["First line\n", "Second line\n", "Third line"])
    

# with open("sample.txt", "r") as f :  
#     print(f.read())


# with open("sample.txt", "r") as f :
#     print(f.name)
#     print(f.mode)
#     print(f.closed)

# print(f.closed)
      

# with open("sample.txt", "r") as f :
#     lines = f.readlines()
#     print(len(lines))

# with open("sample.txt", "r") as f :
#     data = f.read()

# with open("newfile1.txt", "w") as f1 :
#     f1.write(data)

# with open("sample.txt", "r") as f :
#     text = f.read(7)
#     print(text)
#     if "Python" in text:
#         print("Found the word")
#     else:
#         print("Not found")


# with open("sample.txt", "r") as f :
#     for line in f:
#         print(line)




    
