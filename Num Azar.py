import random

num=random.randint(1,100)

x=0

while x != num:
    x = int(input("Introduce un numero: "))

    if x == num:
        print(f"El numero {num} es correcto")
    elif x < num:
         print(f"El numero secreto es mayor")
    else:
        print(f"El numero secreto es menor")