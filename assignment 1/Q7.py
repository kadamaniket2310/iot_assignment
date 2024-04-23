def factorial():
    i = 1
    j = 1
    fact=1
    for i in range(1,11):
        while j<=i:
            fact = fact*j
            j = j+1
        i = i+1
        print(fact)

factorial()



