print('Escolha dois números reais e siga as intruções.')

escolha_um = float(input('Primeiro número: '))
escolha_dois = float(input('Segundo número: '))

if escolha_um == 0 or escolha_dois == 0:
    print('Não existe divisão por zero...')
else:
    print('Escolha umas das operações abaixo:\n'
          '1 - Adição\n'
          '2 - Subtração\n'
          '3 - Multiplicação\n'
          '4 - Divisão')
    opcao = int(input('Código da operação: '))

    if opcao == 1:
        print(f'{escolha_um:.2f} + {escolha_dois:.2f} = {escolha_um + escolha_dois:.2f}')
    elif opcao == 2:
        print(f'{escolha_um:.2f} - {escolha_dois:.2f} = {escolha_um - escolha_dois:.2f}')
    elif opcao == 3:
        print(f'{escolha_um:.2f} x {escolha_dois:.2f} = {escolha_um * escolha_dois:.2f}')
    elif opcao == 4:
        print(f'{escolha_um:.2f} ÷ {escolha_dois:.2f} = {escolha_um / escolha_dois:.2f}')
    else:
        print('Opção inválida...')