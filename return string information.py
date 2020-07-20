
# [ ] review and run example
work_tip = "save your code"

print("number of characters in string")
print(len(work_tip),"\n")

print('letter "e" occurrences')
print(work_tip.count("e"),"\n")

print("find the index of the first space")
print(work_tip.find(" "),"\n")

print('find the index of "u" searching a slice work_tip[3:9] -', work_tip[3:9])
print(work_tip.find("u",3,9),"\n")

print('find the index of "e" searching a slice work_tip[4:] -', work_tip[4:])
print(work_tip.find("e",4))

#.Count Example
# [ ] review and run example

work_tip = "good code has meaningful variable names"
print(work_tip)
print("how many w's? ", work_tip.count("w"))
print("how many o's? ", work_tip.count("o"))
print("uses 'code', how many times? ", work_tip.count("code"))

#.find(string) Example

# [ ] review and run example 
# set start index = 13 and end index = 33
print('search for "meaning" in the sub-string:', work_tip[13:33],"\n")
meaning_here = work_tip.find("meaning",13,33)
print('"meaning" found in work_tip[13:33] sub-string search at index', meaning_here)
# [ ] review and run example 
# if .find("o") has No Match, -1 is returned
print ("work_tip:" , work_tip)
location = work_tip.find("o")

# keeps looping until location = -1 (no "o" found)
while location >= 0:
    print("'o' at index =", location)
    # find("o", location + 1) looks for a "o" after index the first "o" was found
    location = work_tip.find("o", location + 1)
print("no more o's")# [ ] review and run example 
print()


#task 1
# [ ] use len() to find the midpoint of the string 
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"
midpoint  =  int(len(random_tip)/2)
print(random_tip[:midpoint])
print(random_tip[midpoint:])

#task 2 
# for letters: "e" and "a" in random_tip
# [ ] print letter counts 
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"
print("'e' is random_tip : ", random_tip.count("e"), " times")
print("'a' is random_tip : ", random_tip.count("a"), " times")

#Task 3 .find(string)
# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
location = long_word.find("t")

while location >= 0:
    print(long_word[location:])
    location =long_word.find("t",location +1)
print("no more o's")    

#Task 4 Program: print each word in a quote
quote = "they stumble who run fast"
start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start = space_index
    space_index = quote.find(" ",space_index+1)
    # code to print word (index slice start:space_index)
    # [ ] Print each word in the quote on a new line
print("no more space")