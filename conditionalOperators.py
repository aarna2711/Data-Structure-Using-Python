print("Conditional Operators:\n")

a=input("Enter the value of A:")
b=input("Enter the value of B:")
c=input("Enter the value of C:")

print("\n")
if(a>=b and a>=c):
    print("A is the largest.")
elif(b>a and b>c):
    print("B is the largest.")
else:
    print("C is the largest.")
