#Program for Demonstrating break keyword
#BreakEx1.py
s="PYTHON"
print("for loop without break")
for ch in s:
    print(ch)
else:
    print("for loop --else part")
print("----------------------------------")
print("for loop with break kwd")
#My Requirement today is to display "PYTH" only without using Indexing and Slicing
for ch in s:
    if(ch=="O"):
        break
    else:
        print(ch,end="")

else:
    print("for loop --else part")
print()
print("Other Part of the Program")