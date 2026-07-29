print("Hello World!\n")

a=10
b=5

print("Arithmetic operator\n")
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Exponential: ",a**b)
print("Floor Division: ",a//b)

print("\n")
print("Relational operator\n")
print("Is A greater than B: ",a>b)
print("Is A greater than or equal to B: ",a>=b)
print("Is A less than B: ",a<b)
print("Is A less than or equal to B: ",a<=b)
print("Is A equal to B: ",a==b)
print("Is A not equal to B: ",a!=b)

print("\n") 
print("Logical operator\n")
print("A is less than 10 and greater than 0:",a>0 and a<10)
print("A is less than 10 or greater than 0:",a>0 or a<10)
print("A is less than 10 and greater than 0:",not(a<0 and a>10))

print("\n")
print("Bitwise operator\n")
print("Value of A before Left Shift:",a)
print("Value of A after Left Shift:",a << 1)
print("Value of A after Right Shift:",a >> 1)
print("Bitwise AND:",a&b)
print("Bitwise OR:",a|b)
print("Bitwise XOR:",a^b)
print("Bitwise NOT:",~a)


print("\n")
print("Ternary operator\n")
print("A is greater than B:",'Yes' if a>b else 'No')