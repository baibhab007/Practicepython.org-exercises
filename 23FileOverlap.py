l1='inputnum1.txt'
l2='inputnum2.txt'
fhand=open(l1,"r")
rhand=open(l2,"r")
full1_txt=fhand.read()
full2_txt=rhand.read()
num1=full1_txt.split()
num2=full2_txt.split()
print(num1)
print(len(num1))
print(num2)
print(len(num2))
p=[i for i in num1 if i in num2]
p1=set(num1)&set(num2)
print(sorted(p))
print(sorted(p1))
print(len(p))
print(len(p1))
