a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for x in a:
    if x % 2 == 0:
        print(x)
    else:
        pass

print([num for num in a if num % 2 == 0])
