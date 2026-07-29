mytuple=("Apple","Blueberry","Cherry","Dragon Fruit","Elderberry")

print(mytuple)
print("The first element is:",mytuple[0])
print("The last element is:",mytuple[-1])

temp=list(mytuple)

mytuple=tuple(temp)

temp[1]="Banana"
print(mytuple)

temp=list(mytuple)
del temp[1]
mytuple=tuple(temp)

print(mytuple)
