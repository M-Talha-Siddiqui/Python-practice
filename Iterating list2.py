
#combine List
# [ ] review and run example
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# .extend() 
# extending visited_cities list (IN PLACE) by concatenating wish_cities
visited_cities.extend(wish_cities)
print("ALL CITIES",visited_cities)
print()

 #review and run example
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# (+) Addition operator for lists creates a (NEW) combined List
all_cities = visited_cities + wish_cities

print("ALL CITIES",all_cities  )

#reverse
#.reverse() : reverse a list in place
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("regular", cities_1)
cities_1.reverse()
print("reversed", cities_1)

# [ ] review and run example
all_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("regular list",all_num, "\n")
all_num.reverse()
print("reverse list",all_num, "\n")
num_len = len(all_num)

print("Three Multiple")
for num in all_num:
    if num/3 == int(num/3):
        print(num)
    else:
        pass

#Sorting the list
# [ ] review and run example
quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]

# use .sort()
quiz_scores.sort()

print("quiz_scores:", quiz_scores)
# [ ] review and run example
game_points = [3, 14, 0, 8, 21, 1, 3, 8]

# use sorted()
sorted_points = sorted(game_points)

print("game_points:", game_points)
print("sorted_points:", sorted_points)
# [ ] review and run example
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("Unsorted", cities_1)
cities_1.sort()
print("Sorted", cities_1)
visited_cities.sort()
print("visited_cities " , visited_cities)

#Split list
#.split() by default, splits a string at spaces (" ") to create a list

# [ ] review and run example
tip = "Notebooks can be exported as .pdf"
tip_words = tip.split()

print("STRING:", tip)
print("LIST:", tip_words, "\n")

for word in tip_words:
    print(word)
# [ ] review and run example
print()
rhyme = "London bridge is falling down"

rhyme_words = rhyme.split()

rhyme_words.reverse()

for word in rhyme_words:
    print(word)

#Task
# [ ] split the string(rhyme) into a list of words (rhyme_words)
# [ ] print each word on it's own line
rhyme = 'Jack and Jill went up the hill To fetch a pail of water'
word_rhyme = rhyme.split()
for word in word_rhyme:
    print(word)
print()


#to split on characters other than " " (space), provide .split() a string argument to use as break points

# [ ] review and run example
code_tip = "Python-uses-spaces-for-indentation"
tip_words = code_tip.split('-')

print(tip_words)
# [ ] review and run example - study the list print output
code_tip = "Python uses spaces for indentation"

# split on "a"
tip_words = code_tip.split('a')
print(code_tip)
print(tip_words)
# [ ] review and run example
# triple quotes ''' ''' preserve formatting such as spaces and line breaks
big_quote = """Jack and Jill went up the hill
To fetch a pail of water
Jack fell down and broke his crown
And Jill came tumbling after"""

# split on line breaks (\n)
quote_lines = big_quote.split('\n')
print(quote_lines, '\n')

# print the list in reverse with index slicing
for line in quote_lines[::-1]:
    print(line)


# [ ] split poem into a list of phrases by splitting on "*" a
# [ ] print each phrase on a new line in title case
poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
split = poem.split("*")
for w in split:
    print(w, "\n")

#.join() is a method applied to a separator string and iterates through its argument

# [ ] review and run example
tip_words = ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf'] 

# join tip_words objects with spaces
print(" ".join(tip_words))
# [ ] review and run example
no_space = ""
letters = ["P", "y", "t", "h", "o", "n"]
print(no_space.join(letters))
# [ ] review and run example - .join() iterates through sequences
dash = "-"
space = " "
word = "Iteration"
ellipises = "..."

dash_join = dash.join(word)
print(dash_join)
print(space.join(word))
print(ellipises.join(word))
# [ ] .join() letters list objects with an Asterisk: "*"
letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
print("*".join(letters))

#print to the same line with multiple print statements (end=) or insert any character as an end in print("String", end="+")

# [ ] review and run example
hello_letters = list("Hello")
print(hello_letters)
# [ ] review and run example
# cast sting to list
word_letters = list("concatenates")

# .join() concatenates the list
# print on same line setting the end character
print('~'.join(word_letters))
# [ ] review and run example
print("Hello ", end = '')
print("world")
# [ ] review and run example
# This  is the default print end
print("Hello World!", end="2\n")
print('still something to learn about print()')
# [ ] review and run example
# end inserts any valid str character: A-z, 0-9,!,@,*,\n,\t or ''(empty string)...
for letter in "Concatenation":
    print(letter, end='*')
