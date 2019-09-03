import random
i = random.randint(0, 100)
k = 0
print(i)
while True:
    j = input("Let the system know if the number generated is the exact number or too high or too low number: ")
    print(i)

    if j == 'H':
        print("Number is high!!")
        import random
        i = random.randint(0, 100)
        k=k+1
    elif j == 'L':
        print("Number is low!!")
        import random
        i = random.randint(0, 100)
        k=k+1
    elif j == 'R':
        print("Entered number is the right number!! but you took",k,"attempts to GUESS it")
        break
    else:
        print("Please enter a valid input")


