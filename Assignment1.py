l1 = [1,2,3]
l2 = [1,2,3]
print(id(l1))
print(id(l2))
if id (l1) == id (l2):
    print(l1[1])
    
else:
    print(id(l1[0]),id(l1[-1])) 