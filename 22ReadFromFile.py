file='input.txt'
fhand=open(file,"r")
full_txt=fhand.read()
words=full_txt.split()
print(words)
words.sort()
print('Sorted list', words)
print([ (i,words.count(i)) for i in set(words) ])
