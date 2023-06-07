#  Faça um programa que leia um número N e gere um arquivo com N nomes e idades aleatórios
# Faça uso de duas listas criadas na mão: uma que contenha 20 nomes e outra que contenha 20 sobrenomes
# Cada linha do arquivo resultante deve conter um nome completo e a sua idade
# 2. Estenda o exemplo do cadastro para considerar também a altura da pessoa
import random
my_file = open('arquivo.txt','a')

first_name = ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Fernanda", "Rafael", "Carolina", "Gabriel",
         "Mariana", "Diego", "Camila", "Gustavo", "Larissa", "Rodrigo", "Beatriz", "Felipe", "Amanda", "Ricardo"]

last_name = ["Silva", "Santos", "Souza", "Oliveira", "Pereira", "Almeida", "Fernandes", "Rodrigues", "Costa",
              "Gomes", "Martins", "Rocha", "Ribeiro", "Cardoso", "Nascimento", "Melo", "Carvalho", "Araujo", "Moreira", "Cavalcanti"]

def main():
    amount = int(input("Digite quantos nomes quer criar:"))

    for i in range(amount):
        name = first_name[random.randint(0,19)]
        lname = last_name[random.randint(0,19)]
        age = random.randint(0,118)
        size = random.uniform(0.56,2.71)
        my_file.write(f'{name} {lname} {age} anos e {size:.2f}\n')

    my_file.close()

main()