import random
import time
import os


def clear_terminal(aleatoria, hits, emojis):
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    show_hits_game(aleatoria, hits, emojis)


def board(hits):
    aleatoria = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
    random.shuffle(aleatoria)
    emojis = [
        '🐶',
        '🐱',
        '🐭',
        '🐰',
        '🐼',
        '🐵',
        '🐯',
        '🐳'
    ]
    for index, item in enumerate(aleatoria):
        print(emojis[item], end=(
            '\n' if (index + 1) % 4 == 0 else '\t'
        ))

    clear_terminal(aleatoria, hits, emojis)

    return aleatoria, emojis


def show_hits_game(aleatoria, hits, emojis):
    for index, item in enumerate(aleatoria):
        print(
            emojis[item] if item in hits else index ,
            end=('\n' if (index + 1) % 4 == 0 else '\t')
        )

    show_Hits(aleatoria, emojis)


def show_Hits(aleatoria, emojis):
    erros = 1000
    hits = []

    while True:
        try:
            p1 = int(input("ESCOLHA UMA POSIÇÃO:"))

            if p1 > 15 or p1 < 0:
                raise Exception("Valor inválido")

        except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')

        try:
            p2 = int(input("ESCOLHA OUTRA POSIÇÃO:"))

            if p2 > 15 or p2 < 0:
                raise Exception("Valor inválido")

        except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')

        if p1 == p2:
            print("Valores iguais, tente novamente")

        elif aleatoria[p1] == aleatoria[p2]:
            print("ACERTOU")
            hits.append(p1)
            hits.append(p2)
            show_hits_game(aleatoria, hits, emojis)
        else:
            print("ERRRROOOOOOUUUUUU")
            erros -= 50
            if erros  < 900:
                break

    try:
        name = str(input("Digite seu nome:"))
    except BaseException as error:
        print(f'Ocorreu algum erro no sistema: {error}')

    read_file(erros, name)

    return hits,erros,name


def read_file(erros, name):
    try:
        file_ranking = open('ranking.txt', 'r')

        conteudo = file_ranking.read()
        informacoes = conteudo.split()
        lista_informaçoes = []
        for informacao in informacoes:
            nome, pontuacao = informacao.split(':')
            lista_informaçoes.append((nome, int(pontuacao)))

        lista_informaçoes.append((name, int(erros)))

        lista_ordenada = sorted(lista_informaçoes, key=lambda x: x[1], reverse=True)

    except BaseException as error:
        print(f'Ocorreu algum erro no sistema: {error}')

    finally:
        write_file(lista_ordenada)



def write_file(lista_ordenada):
    try:
        file_ranking = open('ranking.txt','w')
        nova_lista = ' '.join([f"{nome}:{pontos}\n"for nome,pontos in lista_ordenada])
        file_ranking.write(nova_lista)
    except BaseException as error:
        print(f'Ocorreu algum erro no sistema: {error}')

    finally:
        file_ranking.close()



def main():
    hits = []
    board(hits)

main()