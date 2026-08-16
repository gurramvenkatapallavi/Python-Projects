#extract vowels
st = input("enter the string")
res=" "
for i in st:
    if i in "AEIOUaeiou":
        res+=i
    elif i>="0" and i<="9":
        res+=i
print(res)  

#extract vowels and space between them
st = input("enter")
res=" "
for i in st:
    for j in i:
        if j in "AEIOUaeiou" or (j>='0' and j<='9') or j==" " :
            res+=j
print(res)   

#extract only vowels
st = input()
res=" "
i=0
while i<=len(st)-1:
    ch = st[i]
    if ch in 'AEIOUaeiou' or ch==" ":
        res+=ch
    i+=1
print(res)  

#remove vowels
st = input()
res=" "
i=0
while i< len(st)-1:
    ch=st[i]
    if ch not in "AEIOUaeiou":
        res+=ch
    i+=1
print(res)    