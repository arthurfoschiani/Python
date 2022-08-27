#Verificar se formam ou não um triângulo retangulo

l1 = float(input("Digite o primeiro lado do triangulo: "))

l2 = float(input("Digite o segundo lado do triangulo: "))

l3 = float(input("Digite o terceiro lado do triangulo: "))

boole = False

if l1 > l2 and l1 > l3:
    if (l1 * l1) == (l2 * l2) + (l3 * l3):
        boole = True
elif l2 > l1 and l1 > l3:
    if (l2 * l2) == (l1 * l1) + (l3 * l3):
        boole = True
elif l3 > l1 and l3 > l2:
    if (l3 * l3) == (l2 * l2) + (l1 * l1):
        boole = True

if boole == True:
    print("É um triangulo retângulo")
else:
    print("Não é um triangulo retangulo")