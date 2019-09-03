def max(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input('Enter first value: '))
b = int(input('Enter second value: '))
c = int(input('Enter third value: '))
print(max(a,b,c))
