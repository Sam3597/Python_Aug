import csv


# with open("students.csv", "w", newline ="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "roll", "marks"])
#     writer.writerow(["Sam", 1, 89])
#     writer.writerow(["rahul", 2, 70])
#     writer.writerow(["suraj", 3, 90])

# print("Data Saved ...")



# with open("students.csv", "r") as file:
#     Data = csv.reader(file)
#     for row in Data:
#         print(row)

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Neha", 4, 75])
    

# print("Added new row")


# with open("students.csv", "w", newline="") as file:
#     KeyName = ["Name", "Roll", "Marks"]
#     writer = csv.DictWriter(file, fieldnames=KeyName)
    
#     writer.writeheader()
#     writer.writerow({"Name": "Sam", "Roll": 1, "Marks": 89})
#     writer.writerow({"Name": "Rahul", "Roll": 2, "Marks": 67})
#     writer.writerow({"Name": "Suraj", "Roll": 3, "Marks": 45})

# print("Added...")


with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Marks"], row["Roll"])