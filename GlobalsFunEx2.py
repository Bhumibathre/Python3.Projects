#Program for Demonstrating globals()
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40 # # Here a,b,c,d are called global Variables
def operations():
    x=100
    y=200
    z=300
    k=400 # Here x,y,z,k are called local Var
    res=a+b+c+d+x+y+z+k
    print("Sum=",res)
#Main Program
operations() # function call