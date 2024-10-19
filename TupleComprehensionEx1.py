#tupleComprehensionEx1.py
print("Enter List of Values separated by space:")
x=(int(val) for val in input().split()) # feeling that It is tuple Comprehension
#here x is called an object of <class,generator>
t=tuple(x) # Type Casting generator object into tuple object
print("Elements in tuple=",t)
print(type(t))
