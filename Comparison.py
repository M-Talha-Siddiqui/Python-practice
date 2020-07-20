# review and run code
"hello" < "Hello"
# review and run code
"Aardvark" > "Zebra"
# review and run code
'student' != 'Student'
# review and run code
print("'student' >= 'Student' is", 'student' >= 'Student')
print("'student' != 'Student' is", 'student' != 'Student')
# review and run code
"Hello " + "World!" == "Hello World!"
msg = "Hello"
# [ ] print the True/False results of testing if msg string equals "Hello" string
print(msg," = 'Hello' is " , msg == 'Hello' )

greeting = "Hello"
msg = input("Please type the greeting: ")
print (" the Greeting and input are same is ", greeting == msg)
# [ ] get input for variable named msg, and ask user to 'Say "Hello"'
# [ ] print the results of testing if msg string equals greeting string

# [ ] review and run code
msg = "Save the notebook"

if msg.lower() == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")
# [ ] review and run code
msg = "Save the notebook"
prediction = "save the notebook"

if msg.lower() == prediction.lower():
    print("message as expected")
else:
    print("message not as expected")

# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"
print("What is 8 + 13? : ")
Ans = input ("Answer : ")
if Ans == str(21):
    print("Correct Answer")
else:
    print("Incorrect Answer")

#Call the tf_quiz function with 2 arguments
#T/F question string
#answer key string like "T"
#Return a string: "correct" or incorrect"
def tf_quiz(question,key):
    ans = input(question)
    if ans.lower() == key.lower():
        print("Correct Answer")
    else:
        print("Incorrect Answer")
tf_quiz("Human are mmamals : ", "T")
            
