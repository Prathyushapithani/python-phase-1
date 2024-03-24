n=int(input("enter the value"))
e=n
b=0
d=0
while n>0:
    a=n%10
    b=b+a
    c=a**3
    n=n//10
    d=d+c
if d==e:
    print("Yes")
else:
    print("No")
