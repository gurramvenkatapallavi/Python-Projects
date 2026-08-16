st ="Hello  World"
word=" "
res=" "
for ch in st:
    if ch!=' ':
        word=ch+word
    else:
        if word!=' ':
            res+=word
            word=" "
        res+=ch
if word!=" ":
    res+=word
    print(res)