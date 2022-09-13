#To check if the given character is digit or not

character = str(input("Enter the value character:"))
if character >= '0' and character <= '9':
    print("The entered character" ,character ,"is a Digit")
else:
    print("The entered character" ,character ,"is not a Digit")



#To check if the given character is digit or not using isdigit function

character = str(input("Enter the value character:"))
if character.isdigit():
    print("Its a digit")
else:
    print("Its not a digit")


#Replace wuth string space with given character

#taking input from the user
string = input("Enter a String value : ")
result = ''  #empty string
ch = input("Enter a Character : ")
for i in string:  #iterating using for loop
        if i == ' ':  #if any space found in the string
            i = ch   #replacing space with character
        result += i   #concatenating each character of the string without space
print("String after removing space with t = ",result)
