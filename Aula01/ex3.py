#3.Ler uma lista
#de 4 números e mostre o menor e maior número da lista;

list = [1,2,3,4]

max = 0
min = 0

for i in range(len(list)):
    if i == 1:
        max = list[0]
        min = list[0]

    else:
        if max < list[i]:
            max = list[i]

        if min > list[i]:
            min = list[i]

print(f'Lista: {list}')
print(f'Maior = {max}  Menor = {min}')