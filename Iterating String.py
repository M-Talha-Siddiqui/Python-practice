# [ ] review and run example
word = "cello"

for letter in word:
    print(letter)

print()    
# [ ] review and run example
# note: the variable 'letter' changed to 'item'
word = "trumpet"

for item in word:
    print(item)
# [ ] review and run example
# note: variable is now 'xyz' 
# using 'xyz', 'item' or 'letter' are all the same result
word = "piano"
print()    
for xyz in word:
    print(xyz)
# [ ] review and run example
# creates a new string (new_name) adding a letter (ltr) each loop
# Q?: how many times will the loop run?
student_name = "Skye"
new_name = ""
print() 

for ltr in student_name:
    if ltr.lower() == "y":
        new_name += ltr.upper()
    else:
        new_name += ltr
print(student_name,"to",new_name)

#[ ] Get user input for first_name
# [ ] iterate through letters in first_name 
#    - print each letter on a new line
First_name = input("Enter your first name : ")
new_name = " "
for wrd in First_name:
    if wrd.lower() == "i":
        new_name += wrd.upper()
    elif wrd.lower() == "o":
        new_name += wrd.upper()    
    else:
        new_name += wrd 
print (First_name , " to ", new_name)  

#Ieration and Slicing
# [ ] review and run example
student_name = "Skye"

for letter in student_name[:3]:
    print(letter)
print()
# Iterate BACKWARDS
# [ ] review and run example
student_name = "Skye"

# start at "y" (student_name[2]), iterate backwards
for letter in student_name[2::-1]:
    print(letter)

# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
other_word = " "
for ltr in long_word[::2]:
    other_word += ltr
print(other_word)    
# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"
fav_color = input(" Enter our favorite color : ")
new_color =""
for ltr in fav_color[::-1]:
    new_color += ltr
print(new_color.lower() + fav_color.title())    