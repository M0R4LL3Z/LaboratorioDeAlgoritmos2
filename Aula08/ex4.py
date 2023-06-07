#Faça um programa para alterar uma das notas de um aluno (usando os arquivos do exercício anterior).
# O programa deve ter uma função que recebe o nome do aluno, a nota velha e a nova nota.
# A função deve fazer a alteração no arquivo.

def adjusting_media(file_media):
    media = file_media.readlines()
    new_media = {notas.rstrip('\n') for notas in media}
    name_note = input('Digite o nome do aluno e a nota:')
    new_note = input('Digite o nome do aluno e a nova nota que deseja adicionar:')
    for note in new_media.copy():
        if name_note == note:
            new_media.update(new_note)



    print(new_media)












def main():
    file_media = open('Media_alunos.txt','r+')
    adjusting_media(file_media)
    file_media.close()
main()