#4.Crie uma
#programa que crie uma lista de números aleatórios e exiba. O tamanho da lista
#deve ser informado pelo usuário;

import random

list = []
choice = int(input('Digite o tamanho da lista desejado: '))

for c in range(choice):
    numbers = random.randint(1, 10)
    list.append(numbers)

print(list)