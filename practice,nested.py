color = input("Please type the color of shirt (White = 'w' , Blue ='b') : ")
size = input("please type the size of shirt(L,M,S) : ")
if color == "w":
    if size.lower() == "l":
        print ("A ",size," size ", color, " color shirt")
    elif size.lower() == "m":
        print("A ",size," size ", color, " color shirt")
    else:    
        print("A ",size," size ", color, " color shirt is not avalable")
elif color == "b":
    if size.lower() == "m":
        print ("A ",size," size ", color, " color shirt")
    elif size.lower() == "s":
        print("A ",size," size ", color, " color shirt")
    else:    
        print("A ",size," size ", color, " color shirt is not avalable")
else:
    print("A ", color," color ", size, " size shirt is not available.")

#Program: ticket_check() - finds out if a seat is avaiable
def ticker_check(section, seats):
    if section.lower() == "g":
        if int(seats) > 0 & int(seats) < 11:
            return True
    elif section.lower() == 'f':
        if int(seats) >0 & int(seats) < 5:
            return True
    else:
        return False

print(ticker_check("g",11 ))                