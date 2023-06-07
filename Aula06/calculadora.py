# Faça uma calculadora que forneça as seguintes opções para o usuário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8.


def numbers(memoria):
    num=0
    n1=0
    n2=0
    if memoria == 0:
        try:
            n1 = int(input('Digite o primeiro número:'))
        except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')
        try:
            n2 = int(input('Digite o segundo número:'))
        except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')

        menu(memoria, n1, n2, num)

    else:
        try:
            num = int(input('Número:'))
        except BaseException as error:
            print(f'Ocorreu algum erro no sistema: {error}')

        menu(memoria, n1, n2, num)

    return n1,n2,memoria,num

def sum(n1,n2,memoria,num):
    if memoria == 0:
        total1 = n1 + n2
        print(f'Soma:{total1}')
        memoria += total1
    else:
        total2 = memoria + num
        print(f'Soma:{total2}')
        memoria = total2

    print(memoria)
    return memoria, numbers(memoria)

def subtract(n1,n2,memoria,num):
    if memoria == 0:
        total1 = n1 - n2
        print(f'Subtração:{total1}')
        memoria = total1
    else:
        total2 = memoria - num
        print(f'Subtração:{total2}')
        memoria = total2
    print(memoria)
    return memoria, numbers(memoria)

def multiplication(n1,n2,memoria,num):
    if memoria == 0:
        total1 = n1 * n2
        print(f'Multiplicação:{total1}')
        memoria += total1
    else:
        total2 = memoria * num
        print(f'Multiplicação:{total2}')
        memoria = total2

    print(memoria)
    return memoria, numbers(memoria)

def division(n1,n2,memoria,num):
    if memoria == 0:
        total1 = n1 / n2
        print(f'Divisão:{total1}')
        memoria += total1
    else:
        total2 =  num / memoria
        print(f'Divisão:{total2}')
        memoria = total2

    print(memoria)
    return memoria, numbers(memoria)

def menu(memoria,n1,n2,num):
        while True:
            print('[1]-Somar')
            print('[2]-Subtrair')
            print('[3]-Multiplicar')
            print('[4]-Dividir')
            try:
                opc = int(input(':'))
                if opc > 4 or opc < 1:
                    raise Exception('Opção inválida')

                elif opc == 1:
                    sum(n1, n2, memoria,num)

                elif opc == 2:
                    subtract(n1, n2, memoria,num)

                elif opc == 3:
                    multiplication(n1, n2, memoria, num)

                elif opc == 4:
                    division(n1, n2, memoria, num)


            except BaseException as error:
                print(f'Ocorreu algum erro no sistema: {error}')



def main():
    memoria = 0
    numbers(memoria)

main()