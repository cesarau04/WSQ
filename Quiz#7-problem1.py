import math
def distance (x1,x2,y1,y2):
    result = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return (result)

x1 = (float(input("Give me x1: ")))
x2 = (float(input("Give me x2: ")))
y1 = (float(input("Give me y1: ")))
y2 = (float(input("Give me y2: ")))
r = distance(x1,x2,y1,y2)
print ("the distance between the numbers given is", r)
