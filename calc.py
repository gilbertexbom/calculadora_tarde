# Interface da calculadora
import mat

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora --\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Sair')

    # Ler a opção do usuário
    op = int(input('\nOpção: '))

    if op == 1:
        # Entrada
        v1 = int(input('Informe v1: '))
        v2 = int(input('Informe v2: '))

        # Processamento
        total = mat.soma(v1, v2)

        # Saída
        print('\n{} + {} = {}'.format(v1, v2, total))
    elif op == 2:
        # Entrada
        v1 = int(input('Informe v1: '))
        v2 = int(input('Informe v2: '))

        # Processamento
        total = mat.sub(v1, v2)

        # Saída
        print('\n{} - {} = {}'.format(v1, v2, total))
    elif op == 3:
        print('Forte abraço!')
        break
    else:
        print(f'Opção {op} incorreta!')