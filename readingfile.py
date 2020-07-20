poem_file = open('poem.txt', 'r')

poem_10char = poem_file.read(10)
print(poem_10char)
print()
print(poem_file.read(10))
poem_parts = poem_file.read(10)
print(poem_parts)
print()
poem_parts = poem_file.read(10)
print(poem_parts)

print()
poem_parts = poem_file.read(10)
print(poem_parts)
print()
poem_parts = poem_file.read(10)
print(poem_parts)
print()
poem_parts = poem_file.read(10)
print(poem_parts)


digits_of_pi_text = open("digits_of_pi.txt")
pi_digit = digits_of_pi_text.read(4)
print(pi_digit)
print()

print(pi_digit+digits_of_pi_text.read(4))

#These strings can be manipulated just like any other string, Boolean tests such as:
poem_file = open('poem.txt', 'r')
poem_part = poem_file.read(15).upper()
print(poem_part)
print()
oem_part = poem_file.read(6).title()
print(poem_part)
print()
poem_file = open('poem.txt', 'r')
poem_text = poem_file.read()
print(poem_text[8:26])

#File read as a list with .readlines()
poem1 = open('poem.txt', 'r')

# readlines and print as a list
poem_lines = poem1.readlines()
print(poem_lines)
for line in poem_lines:
    print(line)
    print(":-)")

#remove newline characters from lists created using .readlines()
count = 0

for line in poem_lines:
    poem_lines[count] = line[:-1]
    count += 1

print(poem_lines)
# [ ] print each list item 
for line in poem_lines:
    print(line)


# File .close() method frees resources
poem1.close()
print("use .readline() to read a line in a file as a string")
#use .readline() to read a line in a file as a string
# [ ] review and run example
# open address to file
poem1 = open('poem.txt', 'r')
# [ ] review and run example
# readline 1, 2, 3
poem_line1 = poem1.readline()
poem_line2 = poem1.readline()
poem_line3 = poem1.readline()
# [ ] review and run example: print the first 3 .readline() values
print("readline function: ", poem_line1 + poem_line2 + poem_line3)

rnb = open("rainbow.txt","r")
rainbow_1 = rnb.readline()
rainbow_2 = rnb.readline()
rainbow_3 = rnb.readline()
print(rainbow_1 + rainbow_2 + rainbow_3)
while rainbow_1:
    print(rainbow_1[:-1].title())
    rainbow_1 = rnb.readline()

rnb.close()
print()
#printing all the lines using while loop
poem1 = open('poem.txt', 'r')
# [ ] review and run example - use a while loop to read each line of a file 
#  remove last character ('\n') and print as upper case
poem_line = poem1.readline()

while poem_line:
    print(poem_line[:-1].upper())
    poem_line = poem1.readline()
# [ ] review and run example
poem1.close()

poem1 = open('poem.txt', 'r')
poem_line = poem1.readline().strip()

while poem_line:
    print(poem_line)
    poem_line = poem1.readline().strip()
    
poem1.close()


#writing on a file 
# [ ] review and run example
# - creates a new local file or overwrites the local file (makes it blank)
new_file = open('new_file.txt', 'w')
# [ ] review and run example to write some text to the file
new_file.write("This is line #1 with 'w'\nThis is line #2 with 'w'\nThis is line #3 withn 'w'!\n")
# [ ] review and run example
# - close file and re-open in read mode 
# - head pointer is at start of file
new_file.close()
new_file = open('new_file.txt', 'r')
# [ ] review and run example to see what was written to the file
new_text = new_file.read()
print(new_text)

new_file.close()

#using .seek() to set the read/write pointer to beginning of file
new_file = open('new_file.txt', 'w+')
# creates a new local file or overwrites the local file (makes it blank)
new_text = new_file.read()
print(new_text)
new_file.write("This is line #1 with 'w+'\nThis is line #2 with 'w+'\n")
new_text = new_file.read()

print(new_text)
#Expected: prints empty string above
#pointer was at end of file where there is nothing to read
#sets the pointer to the beginning of the file, enabling read() to input the entire file contents
# [ ] review and run example - sets pointer to beginning of file
new_file.seek(0)
# [ ] review and run example - now read starts from beginning of file
new_text = new_file.read()
print(new_text)

# # [ ] review and run example - clean up and close file
new_file.close()

#Task 2
#open outer_planets.txt in 'w+' mode (write plus read)
#open outer_planets.txt in write plus read mode 'w+'
#write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
#use .seek() to move the pointer to the start of the file
#use .read() to read the entire file contents
#print the entire file contents and close the file
outer_planet = open("open_planet.txt", 'w+')
planet=outer_planet.read()

outer_planet.write("Jupiter \nSaturn \nUranus \nNeptune \n")
outer_planet.seek(0)
planet=outer_planet.read()
print(planet)
outer_planet.close()

#setting the pointer in a file with positive offset values and whence location
new_file = open('new_file.txt', 'w+')
new_file.write("This is line #1 with 'w+'\nThis is line #2 with 'w+'\n")
new_file.seek(0)
new_contents = new_file.read()
print(new_contents)
print("\n now in the new line we print from index positio 13")
new_file.seek(13)
new_contents = new_file.read()
print(new_contents)
new_file.close()

#seek() with optional whence argument
# [ ] review and run example - setting pointer to end of file with whence value = 2
tips_file = open('code_tips.txt', 'w+')
tips_file.seek(0,2)
tips_file.write("-use seek(0,2) to set read/write at end of file\n")

# read from beginning of file - .seek(0,0) is same as .seek(0)
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)

#append plus mode a+
#append plus (a+) is append mode, plus read mode,append doesn't blank out the file contents with an overwrite
log_file = open('log_file.txt', 'a+')
def logger(log):
    log_entry = input("enter log item (enter to quit): ")
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (enter to quit): ")
        
    return count
logger(log_file) 
log_file.seek(0)
log_text = log_file.read()

print()
print(log_text)
log_file.close()

# [ ] review and run example - create a file with initial count of 0
count_file = open("count_file.txt", "w+")

count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip())

count_file.close()
# [ ] review and run example - can rerun this cell
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# get the int character(s) after the colon and space, cast and increment
count = int(count_line[10:])+1

# write the incremented value to the file - overwrite before value
count_file.seek(10)
count_file.write(str(count))

count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())

count_file.close()
# [ ]  review funtion code for inc_count() funtion that reads file and updates the count
# the file always has 1 line that is The count is: N, where N is an integer
def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt
# [ ] review and run example with call to function: inc_count() - **Run cell multiple times**
# opens file/prints initial value
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# call inc_count() to increase the count 5 times
for i in range(5):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()