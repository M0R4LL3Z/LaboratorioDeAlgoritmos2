#Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão nas diagonais.

Matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

value = Matriz[0][0] + Matriz[1][1] + Matriz[2][2]
value2 = Matriz[0][2] + Matriz[1][1] + Matriz[2][0]

print(f'Soma das diagonais é igual a {value + value2}')