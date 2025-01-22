#1
fixedchnge=50
def bill(units):
    if units<=100:
        print("5",5+fixedchnge)
    elif units<=200:
        print("7 rs per unit",7+fixedchnge)
    elif units>200:
        print("10 rs per unit",10+fixedchnge)
    else:
        print("nothing")
rs=bill(230)
print(rs)

#2
def num(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    return c
print(num(23,45,60))
#3
def arithematic(x,y,value):
    if value==1:
        print("add",x+y)
    elif value==2:
        print("sub",x-y)
    else:
        print(x,y)
res=arithematic(10,30,2)
print(res)
#4
def fact(num):
    if num<=1:
        return 1
    res=num*fact(num-1)
    print(res)
    return res
fact(5)
#6
def fb(n):
    for i in range(n,101):
        if i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        if i%3==0 and i%5==0:
            print("FIZZBUZZ")
res=fb(1)   
print(res)
#7
def div():
    n=int(input("enter a number:"))
    print(n)
    for i in range(1,n+1):
        if n%i==0:
            print(i)
div()
