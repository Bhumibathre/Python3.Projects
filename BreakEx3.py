#Program for Demonstrating break keyword 
#BreakEx3.py
s="MISSISSIPPI"
ictr=0
for ch in s:
    if(ch=="I"):
        ictr=ictr+1
        if(ictr==2):
            break 
        else:
            print(ch,end="")
    else:
        print(ch,end="")
 


