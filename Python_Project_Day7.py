#Python Program to count the number of vowels and consonants 
string_value =input("Enter the string :")
vowels=0
consonants =0
for i in string_value: #iterate through each value
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        vowels+=1
    elif i.isalpha():
        consonants+=1
print("Count of Vowels:{} Count of Consonants:{}".format(vowels,consonants))
