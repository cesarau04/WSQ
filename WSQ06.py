import random
total = 0 #Will be the total of chances
guess = 0 #To count the chances

for i in range(1):
    x = random.randrange(1,101) #The Random Number
    print ("Hi :) let's play, guess my number ^^ it's between 1 and 100")
    g = int(input("What's the number you think I have?: ")) #Number given by the user

    while g != x:
        if (g<x):
            print ("Sorry, my number is bigger")
            guess = guess + 1
            total = guess
            g = int(input("Try again: ")) #Ask again for another number
            continue
        else:
            print ("Sorry, my number is lower")
            guess = guess + 1
            total = total
            g = int(input("Try again: ")) #Ask again for another number
            continue
    print ("You got it, congratulations you won!")
    print ("You needed a total of", total, "chances to guess right")

#It was a quite difficult
