# [ ] review and run example - note the first element is always index = 0
student_name = "Alton"
print(student_name[0], "<-- first character at index 0")
print(student_name[1])
print(student_name[2])
print(student_name[3])
print(student_name[4])
# [ ] review and run example
student_name = "Jin"
if student_name[0].lower() == "a":
    print('Winner! Name starts with A:', student_name)
elif student_name[0].lower() == "j":
    print('Winner! Name starts with J:', student_name)
else:
    print('Not a match, try again tomorrow:', student_name)

# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters
# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else
street_name = "Uinvesistatstrasse"
print(street_name[0])
print(street_name[2])
print(street_name[4])
team_name = input("Enter team name with second character is 'i','o','u' : ")
if team_name[1] == "i":
    print("team name has 'i' as 2nd character. ")
elif team_name[1] == "o":
    print("team name has 'o' as 2nd character. ")
elif team_name[1] == "u":
    print("team name has 'u' as 2nd character. ")
else:
    print ("Team name has no vowel as 2nd character.")  


 # get last letter
end_letter = student_name[-1]
print(student_name,"ends with", "'" + end_letter + "'")
# [ ] review and run example
# get second to last letter
second_last_letter = student_name[-2]
print(student_name,"has 2nd to last letter of", "'" + second_last_letter + "'")
# [ ] review and run example
# you can get to the same letter with index counting + or -
print("for", student_name)
print("index 3 =", "'" + student_name[2] + "'")
print("index -2 =","'" + student_name[-2] + "'")     

#String Slicing
# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters using a slice
print("slice student_name[2:5]:",student_name[2:5])
# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters individually
print("index 2, 3 & 4 of student_name:", student_name[2] + student_name[3] + student_name[4])
# [ ] review and run example
long_word = 'Acknowledgement'
print(long_word[2:11])
print(long_word[2:11], "is the 3rd char through the 11th char")
print(long_word[2:11], "is the index 2, \"" + long_word[2] + "\",", "through index 10, \"" + long_word[10] + "\"")

# [ ] review and run example
student_name = "Colette"
# return every other
print(student_name[::2])
print(student_name[::1])
# [ ] review and run example of stepping backwards using [::-1]
long_word = "characteristics"
# make the step increment -1 to step backwards
print(long_word[::-1])
print(long_word[::2])
#task 5
# [ ] print the first 4 letters of long_word
print ("task 5")
print(long_word[:4])

# [ ] print the first 4 letters of long_word in reverse
print(long_word[-12:-16:-1])

# [ ] print the last 4 letters of long_word in reverse
print(long_word[-1:-5:-1])

# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
print(long_word[6:2:-1])

