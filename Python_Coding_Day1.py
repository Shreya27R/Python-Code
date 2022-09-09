#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Code to get the revsere of a number
#first get the number
num=int(input("Enter the number :"))
reversed_num=0
#get the reverse of the number
while num!=0:
    digit= num%10
    reversed_num= reversed_num*10+digit
    num//=10
print("The reversed number is {}".format(str(reversed_num)))


# In[ ]:


#Code to check arm strong number for 3 digits
number=int(input("Enter the number : "))
#initialize sum=0
sum=0
#get the sum of cube of all the digits in number
temp=number
while temp > 0:
    digit=temp%10
    sum = sum + digit**3
    temp =temp//10
if sum==number:
    print("The number {} is armstrong number".format(int(sum)))
else :
    print("The number is not armstrong")
