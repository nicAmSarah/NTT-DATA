nome = "Sarah"

print(nome.upper())  #maiusculo
print(nome.lower()) #minusculo
print(nome.title()) #primeiraMaiuscula

texto = "  ola    "
print(nome)
print(texto.strip())  #apagar os espaços
print(texto.lstrip())   #apagar os espaços da esquerda
print(texto.rstrip())   #apagar os espaços da direita

palavra = "NumSei"

print(palavra.center(14)) #centralizar a palavra
print(palavra.center(14,"x")) #centralizar a palavra incluindo caracteres
print("-".join(palavra))    #incluir nas letras o caractere pedido