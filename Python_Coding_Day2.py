#Question 3 Print the number is prime or not
#!/usr/bin/env python
i,temp=0,0
number=int(input("Enter the number to check prime or not:"))
for i in range(2,number//2):
    if number%i==0:
        temp=1
        break
if temp==1:
    print("The number {} is not prime number".format(int(number)))
else:
    print("The number is Prime Number")




# question 4 ---Print the fibonacci series of a number
first,second=0,1
n= int(input("Please enter the number to get the fibonacci series :"))
#Loop from 0 to n number
for i in range(0,n):
    #check first if the number is less than and equal to 1 if less then store value in result
    if i <=1:
        result=i
    else:
        result = first + second
        first = second
        second = result
    print(result)
