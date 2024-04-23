
arr = [3,1,3,4]
arr.sort()
n = 0
for i in range(len(arr)):
    if(arr[i] > n):n += 1
print(n)

