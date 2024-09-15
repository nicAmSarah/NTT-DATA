texto = input("Digite alguma palavra")
vogais= "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print()