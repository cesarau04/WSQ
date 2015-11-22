import math

def calculate_E(accuracy):
    e_past = 1
    e_fact = 0
    counter = 1
    while True:
        e_fact += 1/math.factorial(counter)
        e = 1 + e_fact
        if ((e - e_past) < accuracy):
            break
        counter += 1
        e_past = e
    return (e)

def main():
    accuracy = float(input("Accuracy = "))
    print("e: ",calculate_E(accuracy))

if __name__ == '__main__':
    main()
