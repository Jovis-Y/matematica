def criarMatriz():
    l = int(input("insira o número de linhas: "))
    c = int(input("insira o número de colunas: "))
    matriz = []
    for linha in range(l):
        matriz.append([])
        for coluna in range(c):
            matriz[linha].append(int(input(f"insira um valor para a posição {linha+1,coluna+1}: ")))
    return matriz

def multiplicar(m1, m2):
    resultado = []
    if len(m1[0]) != len(m2):
        print("\ninsira uma matriz que tenha o número de linhas igual ao número de colunas de outra matriz")
        exit()
    for i in range(len(m1)):
        resultado.append([])
    for coluna_m2 in range(len(m2[0])):
        for linha in range(len(m1)):
            soma = 0
            for coluna in range(len(m1[0])):
                soma += m1[linha][coluna] * m2[coluna][coluna_m2]
            resultado[linha].append(soma)
    return resultado

m1 = criarMatriz()
m2 = criarMatriz()
for i in multiplicar(m1, m2):
    print(i)
print("multiplicação entre matriz m1 e m2")
