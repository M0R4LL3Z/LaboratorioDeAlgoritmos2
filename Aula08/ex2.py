#Escreva uma função que recebe dois nomes de arquivos e copia o conteúdo do primeiro arquivo para o segundo arquivo.
# Considere que o conteúdo do arquivo de origem é um texto.
# Sua função não deve copiar linhas comentadas (que começam com //)

My_origin_file = open('original.txt','r')
my_copy_file = open('copia.txt','w')

copy = My_origin_file.readlines()

for linha in copy:
    if not linha.startswith('//'):
        my_copy_file.write(linha)



My_origin_file.close()
my_copy_file.close()