#Verificar se formam ou não um triângulo

l1 = float(input("Digite o primeiro lado do triangulo: "))

l2 = float(input("Digite o segundo lado do triangulo: "))

l3 = float(input("Digite o terceiro lado do triangulo: "))

boole = True

if l1 <= l3 and l2 <= l3:
    if l1 + l2 <= l3:
        boole = False
elif l2 <= l1 and l3 <= l1:
    if l2 + l3 <= l1:
        boole = False
elif l3 <= l2 and l1 <= l2:
    if l1 + l3 <= l2:
        boole = False
else:
    print("erro")

if boole == True:
    if l1 == l2 == l3:
        print("Este trinagulo é equilátero")
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print("Este é um triangulo isósceles")
    else:
        print("Este é um triangulo escaleno")
else:
    print("As medidas não formam um trinagulo")