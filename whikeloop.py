# [ ] review the NUMBER GUESS code then run - Q. what cause the break statement to run?
number_guess = "0"
secret_number = "5"

while True:
    number_guess = input("guess the number 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess,"is correct!\n")
        break
    else:
        print(number_guess,"is incorrect\n")
# [ ] review WHAT TO WEAR code then run testing different inputs
while True:
    weather = input("Enter weather (sunny, rainy, snowy, or quit): ") 
    print()

    if weather.lower() == "sunny":
        print("Wear a t-shirt and sunscreen")
        break
    elif weather.lower() == "rainy":
        print("Bring an umbrella and boots")
        break
    elif weather.lower() == "snowy":
        print("Wear a warm coat and hat")
        break

    elif weather.lower().startswith("q"):
        print('"quit" detected, exiting')
        break
    else:
        print("Sorry, not sure what to suggest for", weather +"\n")

#[ ] Program: Get a name forever ...or until done
familiar_name = ""
while True:
    name = input(" Please enter a cmmon name : ")
    print()
    if name.isalpha():
        print("Hello ",name )
        break
    else:
        print("wrong name, type again")


# [ ] review the SEAT COUNT code then run 

seat_count = 0
while True:
    print("seat count:",seat_count)
    seat_count = seat_count + 1

    if seat_count > 4:
        break
# [ ] review the SEAT TYPE COUNT code then run entering: hard, soft, medium and exit

# initialize variables
seat_count = 0
soft_seats = 0
hard_seats = 0
num_seats = 4

# loops tallying seats using soft pads vs hard, until seats full or user "exits"
while True:
    seat_type = input('enter seat type of "hard","soft" or "exit" (to finish): ')
    
    if seat_type.lower().startswith("e"):
        print()
        break
    elif seat_type.lower() == "hard":
        hard_seats += 1
    elif seat_type.lower() == "soft":
        soft_seats += 1
    else:
        print("invalid entry: counted as hard")
        hard_seats += 1  
    seat_count += 1
    if seat_count >= num_seats:
        print("\nseats are full")
        break
        
print(seat_count,"Seats Total: ",hard_seats,"hard and",soft_seats,"soft" )

# review and run GREET COUNT
greet_count = 5

# loop while count is greater than 0
while greet_count > 0:
    print(greet_count, "!")
    greet_count -= 1
print("\nIGNITION!")

count_down = 0
all_animal = ""
while count_down <= 4:
    Animal_name = input("Enter the name of animal : ")
    all_animal = Animal_name
    count_down += 1
    print(count_down , all_animal)    
    if Animal_name.lower() == 'exit':
        break