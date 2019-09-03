i = input("Enter a statement: ")
j = len(i)
print("The statement in reverse order is: ")
for str in range(j):
    print(i[j-1],end=' ')
    j=j-1
    str+=1

print("\n The statement in reverse order considering the words in the same place is: ")
k = i.split()
j = len(k)
for str in k:
    print(k[j-1],end=' ')
    j-=1
