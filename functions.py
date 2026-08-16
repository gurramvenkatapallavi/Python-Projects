#argumented function for the armstrong number
def armstrong(num):
    total =0
    count = digits(num)
    while num !=0:
        rem = num%10
        total += rem**count
        num//=10
    return total    
def digits(p):
    c =0
    while  p!=0:
        r = p%10
        c+=1
        p//=10
    return c   
num = int(input('enter'))
temp = num
result = armstrong(num)
if temp == result:
    print("Armstrong number")
else:
    print("Not Armstrong number")
    
    
#argumented funtion used to check whether the given number is prime or not
def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("Not prime")
        
        
num = int(input("enter the number"))
prime(num)
       
#argumneted spy number using the functions
def spy(num):
    sum =0
    pro =1
    while num!=0:
        rev = num % 10
        sum+=rev
        pro*=rev
        num //=10
    if (pro == sum):
        print("Spynumber")
    else:
        print('not spynumber')
        
num = int(input("enter the number"))
spy(num)
        
    
