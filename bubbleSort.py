a = ["4","1","5","8","2"]

print("List Before Sorting:",a)

n = len(a)

for i in range(n-1):
    for j in range(n-i-1):
        if(a[j] > a[j+1]):
            k = a[j]
            a[j] = a[j+1]
            a[j+1] = k

print("List After Sorting:",a)
