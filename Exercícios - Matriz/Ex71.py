matrizManha=[]
matrizTarde=[]
matrizNoite=[]
 
linhas = int(input("Digite a quantidade de fileiras: "))
colunas = int(input("Digite a quantidade de cadeiras: "))
countM = 0
countT = 0
countN = 0

for l in range(0, linhas, 1):
    matrizManha.append([])
    matrizTarde.append([])
    matrizNoite.append([])
    for c in range(0, colunas, 1):
        if l == 0:
            matrizManha[l].append(c+1)
            matrizTarde[l].append(c+1)
            matrizNoite[l].append(c+1)
        else:
            matrizManha[l].append("-")
            matrizTarde[l].append("-")
            matrizNoite[l].append("-")

resposta = 'S'

while resposta == 'S':
    nome = input("Digite seu nome: ").capitalize()
    sessao = input("Digite o sessao que você quer: ").upper()
    sessao = sessao[0]
    while sessao != 'M' and sessao != 'T' and sessao != 'N':
        sessao = input("Valor inválido, digite novamente: ").upper()
        sessao = sessao[0]
    if (sessao[0] == 'M'):
        for l in range(0, linhas, 1):
            print(l, matrizManha[l])
        linha = int(input("Digite a fileira desejada: "))
        coluna = int(input("Digite a cadeira desejada: "))

        while matrizManha[linha][coluna-1] != "-":
            print("Lugar já ocupado.")

        matrizManha[linha][coluna-1] = nome
        print("Seu lugar foi reservado.")
        countM += 1
    elif (sessao[0] == 'T'):
        for l in range(0, linhas, 1):
            print(l, matrizTarde[l])
        linha = int(input("Digite a fileira desejada (1 a {}): ".format(len(linhas))))
        coluna = int(input("Digite a cadeira desejada (1 a {}): ".format(len(colunas))))

        while matrizTarde[linha][coluna-1] != "-":
            print("Lugar já ocupado.")

        matrizTarde[linha][coluna-1] = nome
        print("Seu lugar foi reservado.")
        countT += 1
    elif (sessao[0] == 'N'):
        for l in range(0, linhas, 1):
            print(l, matrizNoite[l])
        linha = int(input("Digite a fileira desejada (1 a {}): ".format(len(linhas))))
        coluna = int(input("Digite a cadeira desejada (1 a {}): ".format(len(colunas))))

        while matrizNoite[linha][coluna-1] != "-":
            print("Lugar já ocupado.")

        matrizNoite[linha][coluna-1] = nome
        print("Seu lugar foi reservado.")
        countN += 1
    
    resposta = input("Você deseja reservar mais algum lugar? ").upper()
    resposta = resposta[0]

    while resposta != "S" and resposta != "N" :
        resposta = input("Digite sim ou não. ").upper()
        resposta = resposta[0]

    if resposta == "N":
        for l in range(0, linhas, 1):
            print(matrizManha[l])
        for l in range(0, linhas, 1):
            print(matrizTarde[l])
        for l in range(0, linhas, 1):
            print(matrizNoite[l])
