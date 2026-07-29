marks=int(input("Enter your Marks:"))
print("\n")
grade='0'

if(marks<=100 and marks>=91):
    grade='A+'
elif(marks<=90 and marks>=81):
    grade='A'
elif(marks<=80 and marks>=71):
    grade='A-'
elif(marks<=70 and marks>=61):
    grade='B'
elif(marks<=60 and marks>=51):
    grade='C'
elif(marks<=50 and marks>=41):
    grade='D'
else:
    grade='F'

print("Your grade is:",grade)