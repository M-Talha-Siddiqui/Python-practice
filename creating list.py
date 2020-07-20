# [ ] review and run example
# define list of strings
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]

# display type information
print("ft_bones: ", type(ft_bones))

# print the list
print(ft_bones)
# [ ] review and run example
# define list of integers
age_survey = [12, 14, 12, 29, 12, 14, 12, 12, 13, 12, 14, 13, 13, 46, 13, 12, 12, 13, 13, 12, 12]

# display type information
print("age_survey: ", type(age_survey))

# print the list
print(age_survey)
# [ ] review and run example
# define list of mixed data type
mixed_list = [1, 34, 0.999, "dog", "cat", ft_bones, age_survey]

# display type information
print("mixed_list: ", type(mixed_list))

# print the list
print(mixed_list)
# [ ] review and run example
print(ft_bones[0], "is the 1st bone on the list")
print(ft_bones[2], "is the 3rd bone on the list")
print(ft_bones[-1], "is the last bone on the list")

Street = ["Gulshan" , "Malir", "Cantt", "DHA" , "Bahadurabad"]
print(" No parking in ", Street[0]," or ", Street[4] )
add_2_num = [2,15,43,5,16,98]
print("The sum of the list is:" , add_2_num[0] + add_2_num[1] + add_2_num[2] + add_2_num[3]+ add_2_num[4] +add_2_num[5])

# [ ] Review & Run, but ***Do Not Edit*** this code cell
# [ ] Fix the error by only editing and running the block below

print(" Total of checks 3 & 4 = $", add_2_num[2] + add_2_num[3])

#.append() method adds an item to the end of a list
# [ ] review and run example
# the list before append
sample_list = [1, 1, 2]
print("sample_list before: ", sample_list)

sample_list.append(3)
# the list after append
print("sample_list after:  ", sample_list)

#task 1
# Currency Values
# [ ] create a list of 3 or more currency denomination values, cur_values
# cur_values, contains values of coins and paper bills (.01, .05, etc.)

# [ ] print the list


# [ ] append an item to the list and print the list
currency_value = [ 0.1,0.2,0.05,0.5]
print("currency vallue contain value of coins:", currency_value)

currency_value.append(1)
print("currency value now contain coin of :" ,currency_value)

# [ ] append additional values to the Currency value list using input()

# [ ] print the appended list
currency_value.append(float(input(" Enter what you want to add:")))
print("curreny value is ", currency_value)

#while loop .append()
#define an empty list: bday_survey
#get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
#using a while loop (while user not entering "quit")
#append the bday input to the bday_survey list
#get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
#print bday_survey list

b_day = []
birthday = " "
while birthday != 'q':
    birthday = input(" Enter the date of the month you were born or 'q' for quit :")
    b_day.append(birthday)
    print("Birthday = ",b_day)

#replace items in a list
list_num  = [1,4, 7]
print("list num : ", list_num)
if list_num[0]<5:
    list_num[0] = "small"
else:
    list_num[0] = "large"
print("list num : ", list_num)

three_word = ['Muhammad', 'Talha', 'Siddiqui']
three_word[0] = three_word[0].upper()
three_word[2] = three_word[2].swapcase()
print(three_word)

#Insert
# [ ] review and run example
# the list before Insert
party_list = ["Joana", "Alton", "Tobias"]
print("party_list before: ", party_list)
print("index 1 is", party_list[1], "\nindex 2 is", party_list[2], "\n")
# the list after Insert
party_list.insert(1,"Colette")
print("party_list after:  ", party_list)
print("index 1 is", party_list[1], "\nindex 2 is", party_list[2], "\nindex 3 is", party_list[3])

#Deleting List using del and .pop()
purchase_amounts = []
insert = " "
subtotal = 0
while insert != "q":
    insert = input("Enter the purchase amount :")
    purchase_amounts.append(insert)
    print(purchase_amounts)
del purchase_amounts[-1]
print(purchase_amounts)
while purchase_amounts:
    subtotal += float(purchase_amounts.pop())
print(float(subtotal))


#.remove(object) removes the 1st item that matches
# [ ] review and run example
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]

print(dogs)
while "Poodle" in dogs:
    dogs.remove("Poodle")
    print(dogs)
# [ ] remove one "Poodle" from the list: dogs , or print "no Poodle found"
# [ ] print list before and after    
print(dogs)
while "Poodle" in dogs:
    dogs.remove("Poodle")
    break
print(dogs)