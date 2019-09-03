from datetime import date
now = str(date.today())
name = input("Enter your name: ")
age = int(input("Enter your age: "))
diff = 100 - age
age1 = int(now[0:4]) + int(diff)
print(name + " will be 100 years old in the year " + str(age1))
inp = input(print("To know the actual date, please press d: "))
if inp == 'd':
    print("Live first!!")
else:
    print("Goodbye")
