import math
def calculuate_e(precision):
    result = 0
    for i in range(precision+1):
        factorial = math.factorial(i)
        num_e = 1/factorial
        result = num_e + result
    return round(result,precision)

def main():
    precision = int(input("How many digits you want: "))
    print (calculuate_e(precision))

if __name__ == "__main__":
    main()
