hum = int(input("How many cars are in the parking lot?"))
if hum > 15:
    print("Oh no! Too many!")
elif hum < 1:
    print("The parking lot is empty!")
else:
    print("Ok then.")

heythee = int(input("How many teeth did you lose?"))
if heythee > 25:
    print("Impossible!")
elif heythee < 1:
    print("You will probably lose teeth as you grow older.")
else:
    print("Wonderful!")

gee = int(input("How many days does it take Earth to make a full ratation around the sun?"))
if gee > 365:
    print("You lost.")
elif gee < 364:
    print("You lost.")
else:
    print("Yes! Good job!")
    
tummy = int(input("How many times do you brush your teeth a day?"))
if tummy < 2:
    print("Try brushing more often!")
elif tummy > 4:
    print("That's unnecessary.")
else:
    print("Good job!")

total = hum + heythee + gee + tummy
if total > 400:
    print("Sorry, but you have lost the quiz. Try again later.")
elif total < 385:
    print("Too bad you lost!")
else:
    print("Good job! You won!")

print("Your total was", total)



    
    

