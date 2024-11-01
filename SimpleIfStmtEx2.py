#progrm for finding biggest of Three Numbers and check for equality
#SimpleIfStmtEx2.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
#logic a big
if (a>=b) and (a>c):
    print("Big({},{},{})={}".format(a,b,c,a))
#logic b big
if(b>a) and (b>=c):
    print("big({},{},{})={}".format(a,b,c,b))
#logic c big
if(c>=a) and (c>b):
    print("big({},{},{})={}".format(a,b,c,c))
#equality
if(a==b) and (b==c) and (a==c):
    print("All Values are equal")
