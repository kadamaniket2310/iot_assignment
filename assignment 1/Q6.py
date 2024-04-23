def factorial(n):
    i = 1
    fact=1
    for i in range(1,n+1):
        fact = fact*i
        i = i+1
    return fact

a = int(input("Entre the number"))
print(factorial(a))