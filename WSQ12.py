def gcd(a,b):
    if a == 0:
        return (0)
    elif b == 0:
        return ("Math ERROR")
    elif a > b:
        residuo = 1
        while residuo != 0:
            residuo = a % b
            a = b
            b = residuo
        return (a)

def main():
    #Code here
    num_a=int(input("Enter number a: "))
    num_b=int(input("Enter number b: "))
    print("GCD of (",num_a,"/",num_b,") is: ",gcd(num_a, num_b))

if __name__ == "__main__":
    main()
