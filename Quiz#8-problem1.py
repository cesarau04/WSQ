def main():
    def dot_product(numlist1, numlist2):
        result = 0
        suma_numbers = 0
        if len(numlist1) == len(numlist2):
            for i in range (len(numlist1)):
                p = numlist1[i] * numlist2[i]
                suma_numbers = suma_numbers + p
            return suma_numbers
        else:
            print (float('NaN'))

    def ask_numbers():
        numlist = []
        answer = "y"
        counter = 0
        while answer != "n":
            n = int(input("Give me a number: "))
            numlist.append(n)
            counter = counter + 1
            if counter == 4:
                answer = (input("You typed 4 elements already, you can type more if you want y/n: ")).lower()
            elif counter > 4:
                answer = (input("continue = y,   exit = n:   ")).lower()
        return numlist

    print("List 1")
    numlist1 = ask_numbers()
    print ("") #Space to separate the lists
    print ("List 2")
    numlist2 = ask_numbers()
    dot = dot_product(numlist1, numlist2)
    print ("") #Space to separate the lists
    print ("The dot product of the list is: ",dot)

if __name__ == "__main__":
    main()
