#Program for Finding Biggest of Two Numbers and check for Equality
#SimpleIfEx1.py
a=float(input("Enter First Value:")) # 10
b=float(input("Enter Second Value:")) # 2
if(a>b):
    print("Big({},{})={}".format(a,b,a))
if(b>a):
    print("Big({},{})={}".format(a, b, b))
if(a==b):
    print("Both values are equal")
print("Program Execution completed")