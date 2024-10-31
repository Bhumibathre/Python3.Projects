#EmployeePaySlip.py
eno=int(input("Enter Employee Number:"))
ename=input("Enter Employee Name:")
bsal=float(input("Enter Employee Basic Salary:"))
if(bsal<=0):
    print("{} is invalid Salary".format(bsal))
else:
    if(bsal>=10000):
        da = (25/100)* bsal
        ta = (15/100)*bsal
        cca = (2/100)*bsal
        hra=(8/100)*bsal
        ma=(1/100)*bsal
        lic=(2/100)*bsal
        gpf=(1.5/100)*bsal
    else:
        da = (12.5 / 100) * bsal
        ta = (7.5 / 100) * bsal
        cca = (1.5 / 100) * bsal
        hra = (6 / 100) * bsal
        ma = (0.5 / 100) * bsal
        lic = (1.5 / 100) * bsal
        gpf = (1.25 / 100) * bsal
    #Calculate Netsal
    netsal=(bsal+da+cca+ta+hra+ma)-(lic+gpf)
    #display employee pay slip
    print("="*50)
    print("Employee Pay Slip")
    print("=" * 50)
    print("Employee Number:{}".format(eno))
    print("Employee Name:{}".format(ename))
    print("Employee Basic Salary:{}".format(bsal))
    print("BENEFITS")
    print("\t\tDA={}".format(da))
    print("\t\tTA={}".format(ta))
    print("\t\tCCA={}".format(cca))
    print("\t\tHRA={}".format(hra))
    print("\t\tMA:{}".format(ma))
    print("DEDUCTIONS")
    print("\t\tLIC:{}".format(lic))
    print("\t\tGPF:{}".format(gpf))
    print("----------------------------")
    print("NET SALARY:{}".format(netsal))
    print("=" * 50)
print("Program Execution Completed")

