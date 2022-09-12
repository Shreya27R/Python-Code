#Anagam ->anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once
def anagramCheck(str1,str2):
    if (sorted(str1)==sorted(str2)):
        return True
    else:
        return False


str1=input("Enter string 1:")
str2=input("Enter string 2:")
if anagramCheck(str1,str2):
    print("Anagram")
else:
    print("Not a Anagram")


#To check if the given string is a palindrome
string = input("Please give a String : ")
if(string == string[:: - 1]):
   print("Given String is a Palindrome")
else:
   print("Given String is not a Palindrome")

 #Using loop
 # function to check string is
# palindrome or not
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
s = input("Enter the string :")
ans = isPalindrome(s)

if (ans):
    print("Yes it's Palindrome")
else:
    print("No it's not a Palindrome")


#To check if the charecater is vowel or consonant
ch=input("Enter a character to check vowel or consonant :")
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
	#if ‘if’ condition satisfy
	print("Given character", ch ,"is vowel")
else:
#if ‘if’ condition does not satisfy the condition
	print("Given character",ch, "is  consonant")
