a = input("Enter a string to check for palindrome: ")
if a == a[::-1]:
    print(a,"is palindrome")
else:
    print(a,"is not palindrome")

