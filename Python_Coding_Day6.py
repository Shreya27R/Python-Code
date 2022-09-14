#Converting to upper case from lowercase
string = input("Enter a String to convert to upper case : ")
result=''
for i in string:  #iterate through each letter/character from the string
        if i.islower():  #if lowercase
            i = i.upper() #converting lowercase into uppercase letter
        result += i #concatenating each character of the string without lowercase letter
print("String after converting lower case to upper :",result)



#Python code to remove vowels from the string
#taking the input string from the user
string = input("Enter a String : ")
result=''
for j in string:
#iterating through each character of the string
    if j in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
     #seaching for vowels
        j = ''
#if vowel found replace it with empty string
    result += j
    #concatenate rest of the string
print("String after removing the vowels are as follows:",result)
