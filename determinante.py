def organizeMatriz(matriz):
    """organizeMatriz é uma função que cria duas novas listas para que Det possa retorna o valor desejado, a lógica por trás dele é simples: organizar as diagonais em linhas verticais, perceba que a diagoanal que se forma no 1 - 5 - 9, 2 - 6 - 7 e assim por diante
1 2 3       1 2 3       1 2 3
4 5 6   ->  5 6 4   ->  6 4 5
7 8 9       9 7 8       8 9 7
:matriz parâmetro que passa a matriz."""
    lista1 = matriz[:]
    lista2 = matriz[:]
    
    lista1.pop(3)
    lista1.insert(5, matriz[3])
    lista1.insert(6, matriz[8])
    lista1.pop()

    lista2.insert(3, matriz[5])
    lista2.pop(6)
    lista2.pop(6)
    lista2.append(matriz[6])

    return lista1, lista2

def det(matriz):
    l1, l2 = organizeMatriz(matriz)
    det = 0
    for n in range(3):
        det += l1[0+n] * l1[3+n] * l1[6+n]
        det -= l2[0+n] * l2[3+n] * l2[6+n]

    return det

matriz = []
for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                matriz.append(float(input(f'DIGITE UM NÚMERO REAL PARA LINHA {linha+1}, COLUNA {coluna+1}: ')))
                break
            except:
                print('\033[31mERRO!\033[0;0m')

print('deteminante:', det(matriz))
