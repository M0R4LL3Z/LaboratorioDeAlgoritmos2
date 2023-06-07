#Escreva um programa para armazenar uma agenda de telefones em um dicionário.
# Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa.
# Seu programa deve ter as seguintes funções: ­
#createContact – essa função acrescenta um novo nome na agenda, com um ou mais telefones.
# Ela deve receber como argumentos o nome e ostelefones. ­
#includePhone– essa função acrescenta um telefone em um nome existente na agenda.
# Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-­lo.
# Caso a resposta seja afirmativa, use a funçãoanterior para incluir o novo nome. ­
#deletePhone – essa função exclui um telefone de uma pessoa que já está naagenda.
# Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. ­
#deleteContact – essa função exclui uma pessoa da agenda. ­
#getFones – essa função retorna os telefones de uma pessoa na agenda.

def menu(agenda):
    while True:
        print('----- AGENDA -----')
        print('1 - Criar contato')
        print('2 - Adicionar número')
        print('3 - Excluir número')
        print('4 - Excluir contato')
        print('5 - Mostrar números salvos')
        print('6 - Sair')
        opc = str(input(':'))

        if opc == '1':
            createContact(agenda)

        elif opc == '2':
            includePhone(agenda)

        elif opc == '3':
            deletePhone(agenda)

        elif opc == '4':
            deleteContact(agenda)

        elif opc == '5':
            getFones(agenda)

        elif opc == '6':
            print(agenda)
            break

    return opc

def createContact(agenda):
    name = input('NOME:')
    phone = input('NÚMERO DO TELEFONE:')
    agenda[name] = [phone]

    return agenda

def includePhone(agenda):
    name = input('Digite o nome em que o número está salvo: ')
    for nome in agenda:
        if name in agenda:
            new_number = input('Adicione mais um número:')
            agenda[name].append(new_number)
            return

        else:
            print('Nome não encontrado, deseja inclui-lo?')
            print('1 - Sim')
            print('2 - Não')
            opc = input(':')
            if opc == '1':
                createContact(agenda)
                return
            else:
                return


    return agenda

def deletePhone(agenda):
    name = input('Digite o nome onde o número que você quer excluir está salvo: : ')
    for nome in agenda:
        if name in agenda:
            if len(agenda[name]) > 1:
                number = input('Digite o número que quer excluir: ')
                agenda[name].remove(number)

            else:
                print(f'O contato {name} será excuido da lista de contatos')
                print('1 - SIM')
                print('2 - NÃO')
                opc = input(':')
                if opc == '1':
                    del agenda[name]
                    return
                else:
                    return
        else:
            print('Nome não encontrado')


    return agenda

def deleteContact(agenda):
    name = input('Digite o nome do contato que deseja excluir: ')
    for nome in agenda.copy():
        if name in agenda:
            print('Nome deletado')
            del agenda[name]
            return

        else:
            print('Nome não encontrado')

    return agenda

def getFones(agenda):
    name = input('Digite o nome do contato que deseja ver o número: ')
    for nome in agenda:
        if name in agenda:
            print(f'O contato {name} tem {agenda[name]} salvo na agenda')
            return

        else:
            print('Nome não encontrado')
            return


def main():
    agenda = {}
    opc = menu(agenda)


main()

