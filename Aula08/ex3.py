#Faça um programa contendo uma função que recebe como
#argumentos os nomes de dois arquivos.
# O primeiro arquivo contém nomes de alunos e o segundo arquivo contém as notas dos alunos.
# No primeiro arquivo, cada linha corresponde ao nome de um aluno e no segundo arquivo,
# cada linha corresponde às notas dos alunos (uma ou mais).
# Assuma que as notas foram armazenadas como strings, e estão separadas umas das outras por espaços em branco.
# Leia os dois arquivos e gere um terceiro arquivo que contém o nome do aluno seguido da média de suas notas.

def average_students(note):
    total = 0
    quantidade = 0

    for nota in note:
        total += float(nota)
        quantidade += 1

        if quantidade > 0:
            return total / quantidade

        else:
            return 0

def generate_media(file_alunos,file_notas,file_media):
    for linha_alunos,linha_notas in zip(file_alunos,file_notas):
        student = linha_alunos.strip()
        note = linha_notas.split()
        media = average_students(note)
        file_media.write(f'{student}:{media}\n')

    file_alunos.close()
    file_notas.close()
    file_media.close()

def main():
    file_alunos = open('alunos.txt','r')
    file_notas = open('Notas.txt','r')
    file_media = open('Media_alunos.txt','w')
    generate_media(file_alunos,file_notas,file_media)

main()