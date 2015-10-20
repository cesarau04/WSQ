def fibonacci(n):
    if n==0:
        return (0)
    elif n==1:
        return (1)
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = (int(input("Give me a non-negative Integer: ")))
while n<0:
    n = (int(input("You gave me a non-negative Integer, try again: ")))
else:
    fibo = fibonacci(n)
    print (fibo)
