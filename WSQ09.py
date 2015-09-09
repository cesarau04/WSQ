def number_given(): #Function where the "n" is given
    while (True):
        try:
            n = int(input("Number; "))
            while n < 0:
                print("No negative number allowed")
                n = int(input("Number; "))
                continue
            break
        except ValueError:
            print("~~ALERT!~~   Words and float numbers aren't allowed")
    return(n)

def factorial_number(n): #Fuction where the magic happens
    n1 = 0
    n2 = n
    nf = 0
    while n1 != 1:
        if (n == 0):
            nf = 1
            return(nf)
        n1 = n2-1
        nf = n * (n1)
        n = nf
        n2 = n1
        continue
    return(nf)

#Program begins here ~
print("Please enter your number (integer positive): ")
n = (number_given())
print("The factorial of", n, "is", factorial_number(n))
r = input("Want to reset? 'y'/'n': ")

while r == "y":
    n = number_given()
    print("The factorial of", n, "is", factorial_number(n))
    r = input("Want to reset? 'y'/'n': ")
    continue
else:
    print("Have a nice day! :)")
