#Leia uma matriz 3 x 3, conte e escreva quantos valores maiores que 10 ela possui

matriz = [
    [1,2,3],
    [6,5,4],
    [12,13,14]
]
c = 0
for line in matriz:
    for column in line:
        if column > 10:
            c += 1
print(f'Existem {c} números meiores que 10')