#Program for Demonstrating Default Arguments technique
#DefaultArgsEx2.py
def insertstuddetails(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
insertstuddetails(100,"RS",3.5) # Function Call with Possitional args
insertstuddetails(200,"TR",4.5) # Function Call with Possitional args
insertstuddetails(300,"MC",2.5) # Function Call with Possitional args
insertstuddetails(400,"DR",1.5) # Function Call with Possitional args
insertstuddetails(sname="KN",marks=1.5,sno=500) # Function Call with Keyword args
insertstuddetails(500,"KV",0.0,"JAVA")# Function Call with Possitional args
insertstuddetails(600,"UD",4.5) # Function Call with Possitional args
insertstuddetails(crs="Dajngo",marks=3.5,sno=700,sname="JS") # Function Call with Possitional args
print("-"*50)
