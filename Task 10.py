m=int(input("enter the marks"))
p=int(input("enter the marks"))
c=int(input("enter the marks"))

if m>80 and p>80 and c>80:
    print("Great")
elif m>60 and m<80 and p>60 and p<80 and c>60 and c<80:
    print("Good")
elif m>35 and m<60 and p>35 and p<60 and c>35 and c<60:
    print("Pass")
else:
    print("Fail")
