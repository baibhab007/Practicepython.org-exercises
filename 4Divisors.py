a = int(input("Enter a number : "))
count = 0
try:
    for i in range(1,a+1):
        if a%i == 0:
            print(i)
            i = i+1
            count = count + 1
        elif a%i != 0:
            if count > 0 and a==i:
                print("No divisor!!")
        else:
            break

except ZeroDivisionError:
    print("Good Job!!")

print("Above numbers are the divisors!!")
