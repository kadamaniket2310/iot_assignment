math = int(input("Entre the math :"))
physics = int(input("Entre the physics :"))
chemistry = int(input("Entre the chemistry :"))

avg = (math+physics+chemistry)/3

if(avg>90) and (avg<100):
    print(f"Grade A")

elif(avg>80) and (avg<89):
    print(f"Grade B")

elif(avg>70) and (avg<78):
    print(f"Grade C")

elif(avg>60) and (avg<69):
    print(f"Grade D")

else:
    print(f"Grade F")

