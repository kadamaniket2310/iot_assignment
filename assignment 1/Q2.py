i = int(input("Entre the number"))
j = i 
a = i/1000
i = i%1000

b = i/100
i = i%100

c = i/10
i = i%10

print(f"{int(a)} {int(b)} {int(c)} {int(i)}")
print(f"{int(j)} = {int(a)}000 + {int(b)}00  + {int(c)}0  + {int(i)}")
print(f"{int(i)} {int(c)} {int(b)} {int(a)}")