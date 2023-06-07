
def menu(bank):
    while True:
        print('----- AGENDA -----')
        print('1 - Depositar')
        print('2 - Sacar')
        print('3 - Consultar saldo')
        print('4 - Consultar historico')
        print('5 - Sair')
        try:
            opc = int(input(':'))

            if opc > 5 or opc < 1:
                raise  Exception('Número inválido')

            elif opc == '1':
                deposit(bank)

            elif opc == '2':
                withdraw(bank)

            elif opc == '3':
                balance(bank)

            elif opc == '4':
                historic(bank)


            elif opc == '5':
                break

        except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')


def deposit(bank):
    try:
        deposito = float(input('Valor para deposito:'))

        if deposito >= 0:
            bank['balance'] += deposito
            bank['historic'].append(f'Deposito de R$ {deposito}')


        else:
            raise  Exception('O valor depositado é inválido')


    except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')

    return bank

def withdraw(bank):
    password = input('Digite a senha:')

    if bank['password'] == password:
        try:
            saque = float(input('Digite o valor que quer sacar:'))

            if saque > bank['balance'] or saque > bank['limit'] or saque < 0:
                raise  Exception('Valor inválido')

            else:
                bank['balance'] -= saque
                bank['historic'].append(f'Saque de R$ {saque}')


        except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')


    return bank

def balance(bank):
    print(f'Seu saldo é de {bank["balance"]} reais')

def historic(bank):
    print('Extrato')
    print(bank['historic'])



def main():
    bank_account = {
        'name': 'John McClane',
        'balance': 500.40,
        'limit': 300,
        'password': '1122',
        'historic': []
    }
    menu(bank_account)


main()