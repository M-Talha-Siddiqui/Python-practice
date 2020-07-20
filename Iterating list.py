#Iterating through List using for in 
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

for city in cities:
    print(city)
print("\n")
print("\n")

sales = [6, 8, 9, 11, 12, 17, 19, 20, 22]
total = 0

for sale in sales:
    total += sale
    
print("total sales:", total)
print("\n")

# [ ]  create a list of 7 integers: player_points
# [ ] print double the points for each point value
player_point = [15,25,35,95,73,41,35,62,76,16]

for point in player_point:
    print(2*point)

print("\n")
print("\n")
print("\n")
#Sorting list and filter in list. useing comparison operation while iterating list
# [ ] review and run example of sorting into strings to display
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
longer_names = ""
shorter_names = ""

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names += "\n" + bone_name
    else:
        longer_names += "\n" + bone_name

print(shorter_names)
print(longer_names)
print()

# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# [ ] Print only cities starting with "m"

for city in cities:
    if (city.lower()).startswith("m"):
        print(city)
    else:
        pass

print()

# [ ] Using cities, from the example in previous page. iterate through the list using "for"/"in"
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# [ ] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city
a_city = ""
no_a_city = ""
for city in cities:
    if "a" in city.lower():
        a_city += "\n" +  city
    else:
        no_a_city += "\n" + city

print("a_city:",a_city)
print("\n")
print("wait")
print("\n")
print("no_a_city", no_a_city)
print("\n")

# for Counting and searching in the list
# [ ] review and run example
# iterates the "cities" list, count & sum letter "a" in each city name

cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search_letter = "a"
total = 0

for city_name in cities:
    total += city_name.lower().count(search_letter)

print("The total # of \"" + search_letter + "\" found in the list is", total)

# Search Function
# [ ] review and run example
# city_search function has a default list of cities to search
def city_search(search_item, cities = ["New York", "Shanghai", "Munich", "Tokyo"] ):
    for city in cities:
        if city.lower() == search_item.lower():
            return True
        else:
            # go to the next item
            pass
    # no more items in list
    return False

# a list of cities
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

search = input("enter a city visited: ")

# Search the default city list
print(search, "in default cities is", city_search(search))

# search the list visited_cities using 2nd argument
print(search, "in visited_cites list is", city_search(search,visited_cities))
print("\n")


#create list, paint_colors, with 5+ colors
#get user input of string:color_request
#iterate through each color in paint_colors to check for a match with color_request
# [ ] complete paint stock

paint_colors = ["red", "orange" , "green", "blue", "voilet", "Yellow", "black" , "indigo"]
colour_request = input("please enter a color name:")
for color in paint_colors:
    if color.lower() == colour_request.lower():
        print(colour_request, " is in the list.")
    else:
        print(colour_request , " is not same as " , color)
        pass
print("\n")
   
#Range concept range(stop) 
for count in range(10):
      print(count)
print()

digits = range(10)
print("digits =", list(digits), "\n")

for count in digits:
    print(count)

sub_total = 0
for item in range(10):
    sub_total += item
    print("sub_total:", sub_total)
print("Total =", sub_total)

# [ ] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040
initial_value = 1 
for value in range(1,8):
    initial_value *= value
    print(initial_value)

# [ ] review and run example
sub_total = 0
temp = 0
for item in range(5, 11):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)
print()

for count in range(25,101,25):
      print(count)
# [ ] review and run example
sub_total = 0
temp = 0
for item in range(25,46,5):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)

for count in range(10,21,2):
    print(count)

for count in range(20,10,-2):
    print(count)


#Input a word string (word)
#find the string length of word
#use range() to iterate through each letter in word (can use to range loops)
#Save odd and even letters from the word as lists
#odd_letters: starting at index 0,2,...
#even_letters: starting at index 1,3,...
#print odd and even lists
# [ ] complete List of letters program- test with the word "complexity"
word = input("Enter the string you want:")
length = len(word)
odd_list = ""
even_list = ""
for num in range(length):
    if num%2 ==0:
        even_list += word[num]
        print("even list " ,even_list)
    else:
        odd_list += word[num]
        print("odd list " ,odd_list )
print()
print("even list " ,even_list)
print()
print("odd list " ,odd_list )

