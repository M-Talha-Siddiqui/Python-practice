# [ ] Get user input for 1 fav_food
# [ ] iterate through letters in fav_food 
#    - print each letter on a new line
fav_food = input("Enter your favourite food : ")
for i in fav_food:
    print(i)
# [ ] iterate work_tip string concatenate each letter to variable: new_string 
# [ ] concatenate the letter or a "-" instead of a space " "
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"


#get user input for first_name
##create an empty string variable: new_name
#iterate through letters in first_name Backwards
#add each letter to new_name as you iterate
#Replace the letter if "e", "t" or "a" with "?" (hint: if, elif, elif, else)
# print new_name
first_name = input("Enter the first name :  ")
new_name = " "

print(first_name[::-1])
    
for xyz in first_name:
    
    if xyz == "e":
        xyz = "?"
    elif xyz == "t":
        xyz = "?"
    elif xyz == "a":
        xyz = "?"
    else:
        xyz =  xyz
    new_name += xyz
print(new_name) 

#Task 5
# [ ] find and display the length of the string: topic
topic = ".len() returns the length of a string"
print(len(topic))

# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"
midpoint = len(topic)/2
print(len(topic))
print(midpoint)

# [ ] print index where first instance of the word  "code" starts using .find()
work_tip = "Good code is commented code"
print(work_tip.find("code"))

# [ ] search for "code" in work_tip using .find() 
# [ ] search substring with substring index start= 13,end = last char 
# [ ] save result in variable: code_index
# [ ] display index of where "code" is found, or print "not found" if code_index == -1
work_tip = "Good code is commented code"
code_index = work_tip.find("code",13,)
if code_index == -1:
    print( code_index , " not found")
else:
    print( code_index, " found.")

#Task 6
# [ ] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"
print(work_tip)
print(work_tip.count("w"))
print(work_tip.count("o"))
print(work_tip.count("code"))


# [ ]  count times letter "i" appears in code_tip string
# [ ] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
print ("code_tip:" , code_tip)
print(code_tip.count("i"))
start = 0
start_index = code_tip.find("i")

while start_index >= 0 :
    print(" 'i' index ", start_index)
    start_index  = code_tip.find("i", start_index +1)
print(" no more 'i' ")    

 