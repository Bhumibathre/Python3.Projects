#Program for Demonstrating break keyword
#BreakEx2.py
s="PYTHON"
print("while loop without break")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("while loop --else part")
print("---------------------------------------")
print("while loop with break")
#My Requirement today is to display "PYT" only without using Indexing and Slicing
i=0
while(i<len(s)):
    if(s[i]=="H"):
        break
    else:
        print(s[i],end="")
        i=i+1
else:
    print("while loop --else part")
print()
print("Other statements in program")

