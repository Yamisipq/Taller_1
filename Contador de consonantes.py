frase: str.lower=(input("Ingresa una frase: "))
frase = frase.replace(" ","")
vocal = "aeiou"

cv=0
cc=0

for i in frase:
    if i in vocal:
        cv += 1
    else:
        cc += 1


print(cv)
print(cc)