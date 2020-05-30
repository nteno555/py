import random

secret = random.randrange(1, 101)

hm = 0
tries = 0


while hm != secret:
    try:
        hm = int(input("Guess a number between 1 and 101!"))
    except:
        print("INVALID INPUT")
        continue

    tries = tries + 1

    if hm > secret:
        print("Too high!")

    elif hm < secret:
        print("Too low!")

    else:
        print("You got it!")

print("The number was", secret)
print("You took", tries,"tries.")





