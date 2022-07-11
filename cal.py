print("ENTER a NUMBER")
a=int(input())
print("Enter another number")
b=int(input())
print("ENTER '+'/'-'/'*'/'%' of ur choice")
ch=input()
if ch=='+':
    a=a+b
    print("THE SUM OF a,b is {} ".format(a))
elif ch=='-':
     a=a-b
     print("THE difference OF a,b is {} ".format(a))
elif ch=='*':
     a=a*b
     print("THE mul OF a,b is {} ".format(a))
else :
    print("choice entered is invalid")
