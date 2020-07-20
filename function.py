def yell_it():
    print("LOREY LAG GAEY !")
yell_it()
def say_this(phrase):  
      print(phrase)
say_this("fuck you")
# yell_this() yells the string Argument provided
def yell_this(phrase):
    print(phrase.upper() + "!")
    
# call function with a string
yell_this("It is time to save the notebook")
# use a default argument
def say_this(phrase = "Hi"):  
    print(phrase)
        
say_this()
say_this("Bye")     

word_to_yell = str(input("Enter what you want to yell : "))
def yell_this(phrase):
    print(phrase.upper() + "!")

yell_this(word_to_yell)

# Message double returns the string Argument doubled
def msg_double(phrase):
      double = phrase + " " + phrase
      return double

# save return value in variable
#msg_2x = msg_double("let's go")
print()
print(msg_double("let's go"))
#print(msg_2x)

def make_schedule(period1, period2):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title())
    return schedule

student_schedule = make_schedule("mathematics", "history")
print("SCHEDULE:", student_schedule)

#sequencing 
def hat_available(color):
    hat_colors = 'lack, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)
have_hat = hat_available('green')  
  
print('hat available is', have_hat)    

## bird program
def bird_available(bird):
    birds = 'crow robin parrot eagle sandpiper hawk pigeon'
    return(bird.lower() in birds)
bird2 = input("enter the name of bird: ")
print("this bird is in the list : " ,bird_available(bird2))