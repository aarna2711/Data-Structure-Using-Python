lst=['11','22','33','44','55','66','77','88','99']
print("First Item:",lst[0])
print("Last Item:",lst[-1])
print("Item at Index 2:",lst[2])
print("Items from Index 3 to 5:",lst[3:6])

print("\n")
#Append
lst.append(110)
print("List after append 110:",lst)
print("\n")

#Pop
lst.pop()
print("List after pop function:",lst)
print("\n")

#Replace
lst[0]=111
print("List after replacing item at firsts position:",lst)
print("\n")

#Reverse
lst.reverse()
print("List after reversing:",lst)
print("\n") 

#Remove
lst.remove(111)
print("List after removing 111:",lst)
print("\n")

#Sort
lst.sort()
print("List after sorting:",lst)
print("\n")

#Insert
lst.insert(1,00)
print("List after inserting:",lst)
print("\n")

#Delete
del lst[0]
print("List after deleting 00:",lst)


