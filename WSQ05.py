f = input("Hi dude ^^ tell me what is the temperature in Fahrenheit?: ")
f = int(f)
c = int(5 * ((f-32)/9))
print ("Hey the temperature of ", f, "Fahrenheit is", c, "Celsius")
if c > 0:
    if c <= 99:
        print ("Dude the water does not boil at this temperature (normally)")
    else:
        print ("Usually the water boils at this temperature")
else:
    print ("The water will froze at this temperature")
#Banana
#Hey notice me, I'm a commentss
