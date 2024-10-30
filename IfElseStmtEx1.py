#Program finding Biggest of Two Number and check for equality by using if..else stmt
#IfElseStmtEx1.py
a=float(input("Enter First Value:")) # 10
b=float(input("Enter Second Value:")) # 2
if(a>b):
    print("big({},{})={}".format(a,b,a))
else:
    if(b>a):
        print("big({},{})={}".format(a, b, b))
    else:
        print("Both Values equal")
print("Program execution completed")

