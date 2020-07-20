# Task 7
# Program: Words after "G"/"g"
       
quote =  (input (" enter a quote :")).lower()
print(quote)
word = ""

for i in quote:
    if i.isalpha():
        word  = word + i    
    elif word[0] >= "h":
        print(word.title())
        word = ""
    else:
        word = "" 
print(word)