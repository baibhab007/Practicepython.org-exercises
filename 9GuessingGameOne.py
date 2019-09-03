import random
b = random.randint(1,9)
while True:
    a = int(input("Enter a number : "))
    if a==b:
        print("You guessed the right number")
        break
    elif a<=b:
        print("Entered number is less")
        print("Please try again")
    else:
        print("Entered number is more")
        print("Please try again")
