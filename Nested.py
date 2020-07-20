print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
# select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
print()
    
if sandwich_type.lower() == "c":
    # select cheese type
    print("Please select a cheese.")
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    print()
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich.  Thank you.")
    elif cheese_type.lower() == "m":
        print("Here is your Manchego Cheese sandwich.  Thank you.") 
    else:
        print("Sorry, we don't have", cheese_type, "choice today.")

elif sandwich_type.lower() == "v":
    print("Here is your Veggie Special. Thank you.")
        
else:
    print("Sorry, we don't have", sandwich_type, "choice today.")
print()
print("Goodbye!")
#Program: Say "Hello"
# [ ] Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n
print(" Greeting Program , type 'y' for saying Hello and 'N' for nod only")
greeting = input('"Want to say Hello? :  "')
if greeting.lower() == 'y':
    print("For full Hello type 'y' and for small one type 'n'")
    full = input("Want to say full Hello? : ")
    if full.lower() == 'y':
        print("Hello")
    else:
        print('Hi')
elif greeting.lower() == 'n':
    print("Freindly nod")
else:
    print(greeting, " is the incorrect input.")            

#Program: [ ] 3 Guesses
# [ ] Create the "Guess the bird" program 
bird_names = " eagle crow sparrow phenix swan chicken duck  "
bird_guess = input ("Guess a birds name : ")
#if bird_guess in bird_names == True:
#    print("wrong guess, please try again.")
#    guess_2 = input("Guess a birds name : ")
# #   if bird_guess in guess_2 == False:
#        print("wrong guess, please try again.")
#        guess_3 = input("Guess a birds name : ")
#        if bird_names in guess_3 == False:
#          print("wrong guess, your have no chances left. ") 
#        else:
#            print(" 3rd try , yes")   
#    else:
#        print("2nd try ,yes")
#else:
#    print("1st try , yes")


if bird_guess in bird_names:
    print("1st try , yes")  
else:
    print("wrong guess, please try again.")
    guess_2 = input("Guess a birds name : ")
    if bird_guess in guess_2:
        print("2nd try ,yes")
    else:
        print("wrong guess, please try again.") 
        guess_3 = input("Guess a birds name : ")
        if bird_names in guess_3:
            print(" 3rd try , yes")
        else:
            print("wrong guess, your have no chances left. ")

