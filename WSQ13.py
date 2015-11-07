import math

def baby_root(n):
    num_pow = 1 #Number power to x
    multiOfNumbers = 1 #To prove the latest pow of x that can be tested

    while multiOfNumbers < n: #Check multiOfNumbers
        multiOfNumbers = (num_pow) * (num_pow)
        num_pow += 1

    root = (num_pow + (num_pow-1))/2 #By Babylonian Method

    for i in range(6): #I think 6 times is okay to find the closest sqrt
        secondStep = n/root
        root = (root+secondStep)/2
    return (round(root, 6)) #Round the result

def main():
    #Code here
    number_given = float(input("Give me your number: "))
    print ("The root of",number_given,"is", baby_root(number_given))

if __name__ == "__main__":
    main()
