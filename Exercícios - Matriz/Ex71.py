matriz=[]
 
linhas = 11
colunas = 4
count = 0

for l in range(0, linhas, 1):
    matriz.append([])
    for c in range(0, colunas, 1):
        if l == 0:
            matriz[l].append(c+1)
        else:
            matriz[l].append("")

resposta = 'S'

while resposta == 'S' and count < 40:
    nome = input("Digite o nome da pessoa que viajará: ").capitalize()
    for l in range(0, linhas, 1):
        print(l, matriz[l])
    linha = int(input("Digite a fileira desejada: "))
    coluna = int(input("Digite a coluna desejada: "))

    if matriz[linha][coluna-1] != "":
        print("Lugar já ocupado.")
    else:
        matriz[linha][coluna-1] = nome
        print("Lugar reservado.")
        count += 1
    
    resposta = input("Você deseja reservar mais algum lugar? ").upper()
    resposta = resposta[0]

    while resposta != "S" and resposta != "N" :
        resposta = input("Digite sim ou não. ").upper()
        resposta = resposta[0]

    if resposta == "N":
        for l in range(0, linhas, 1):
            print(matriz[l])
