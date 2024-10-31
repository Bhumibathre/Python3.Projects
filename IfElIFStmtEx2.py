#progrm for finding biggest of Three Numbers and check for equality
#IfElIFStmtEx2.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
#logic a big
if (a>=b) and (a>c):
    print("Big({},{},{})={}".format(a,b,c,a))
#logic b big
elif(b>a) and (b>=c):
    print("big({},{},{})={}".format(a,b,c,b))
#logic c big
elif(c>=a) and (c>b):
    print("big({},{},{})={}".format(a,b,c,c))
#equality
elif(a==b) and (b==c) and (a==c):
    print("All Values are equal")
