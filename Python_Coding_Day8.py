#Find the missing number in an array
arr = []
num= int(input("enter size of array where num is: "))
for x in range(num-1):
    x=int(input("enter element of array : "))
    arr.append(x)
sum = (num*(num+1))/2;
sumArr = 0
for i in range(num-1):
    sumArr = sumArr+arr[i];
print(int(sum-sumArr))
