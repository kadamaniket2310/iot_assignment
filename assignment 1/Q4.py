a = int(input("Entre the number :"))
b = int(input("Entre the number :"))
c = int(input("Entre the number :"))

if(a > b) and (a > c):
    print(f"number a is greater")
elif(b > a) and (b > c):
    print(f"number b is greater")
else:
    print(f"number c is greater")