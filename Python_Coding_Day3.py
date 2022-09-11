#Conatins Fibonacci series,Palindrome,Greatest of the integer,Find character from the string,get the count of specific character

#Fibonacci number using  recursive method use function named Fibonacci
first,second=0,1
n = int(input("please give a number for fibonacci series : "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("The fibonacci series is: ")

for i in range(0,n):
    print(fibonacci(i))


#To check if the give number is palindorme or not
n=int(input("Please give a number to check if it is palindorme or not :"))
#store the n in temp variable
reverse,temp=0,n
#get the reverse of the number
while temp!=0:
    reverse = reverse*10 + temp%10
    temp=temp//10
    #Compare reverse number and n
if reverse ==n:
    print("Number is a plaindoreme")
else:
    print("Number is not a Plaindrome")


    #To check if the give number is palindorme or not
#First check the number is less than 10 then return
num=int(input("Please give a number to check if it is palindorme or not :"))
def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num%10)+ str(reverse(num//10)))
def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(num)==1:
    print("The given number is a palindorme")
else :
    print("The given number is not a palindrome")


#Find the greatest of the 3 interger
a= int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c= int(input("Enter the 3rd number:"))
def greatest(a,b,c):
    if a >b and a > c:
        return a
    elif b >a and b > c:
        return b
    else:
        return c
print("The greatest number is :"+ str(greatest(a,b,c)))

#Can use below code also to find the greatest of the integer
n1 = int(input("please give first number n1: "))
n2 = int(input("please give second number n2: "))
n3 = int(input("please give third number n3: "))
if n1>=n2 and n1>=n3:
	print(" n1 is greatest");
if n2>=n1 and n2>=n3:
	print(" n2 is greatest");
if n3>=n1 and n3>=n2:
	print("n3 is greatest");


#Program to remove the given character from the string
s1=input("Please enter a string:")

s2=input("Please enter a charcter to remove:")

def remove_character(s1,s2):
    print(s1.replace(s2,''))
remove_character(s1,s2)


#Python Program to count the occurrence of given character in a string.
s=input("Please Enter a string :")
char=input("Please enter the character to get the count :")
count=0
for i in range(len(s)):
    if s[i] == char:
        count=count+1
print("Total occurence of {} is {}".format(char,count))
