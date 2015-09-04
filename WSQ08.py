#WSQ03 42 Numbers
def sum_op(n,n2):
    s = n + n2
    return(s)
def minus_op(n,n2):
    r = n - n2
    return(r)

def multi_op(n,n2):
    m = n * n2
    return(m)

def divi_op(n,n2):
    di = n / n2
    di = round (di,2)
    return(di)

n = int(input("Enter a number: "))
n2 = int(input("Enter a second number: "))
print("This is the basic operations for the numbers entered")
print("Sum = ", sum_op(n,n2), ", minus = ", minus_op(n,n2), ", multiplication = ", multi_op(n,n2), ", division = ", divi_op(n,n2),)
