o = 0 #Counter
n = 0 #First number
suma = 0 #Sum

print ("~~~~We will calculate the sum of integers in range you provide~~~~")

while True:
    try:
        n1 = int(input("Tell me the lower bound: "))
        n2 = int(input("Tell me the upper bound: "))
        break
    except ValueError:
        print("You give a invalid number")

n1c = n1
n2c = n2

while (o == 0):
    if n2 < n1:
        print ("Check your numbers, they are inverted")
        n1 = int(input("Tell me the lower bound: "))
        n2 = int(input("Tell me the upper bound: "))
    elif n1 == n2:
        print("the number are equals, try again")
        n1 = int(input("Tell me the lower bound: "))
        n2 = int(input("Tell me the upper bound: "))
    else:
        o = 1

n2 = n2 + 1
n = n1

for i in range (n1,n2):
    if n1 != n2:
        suma += n
        n = n + 1
        continue

print("This is the suma of the numbers between", n1c ,"y", n2c,":", suma)
