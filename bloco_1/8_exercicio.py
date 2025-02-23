print('Prezado(a) colaborador(a), seja bem-vindo(a)!\n'
      'Para dar continuidade, siga atentamente os passos solicitados')

valor_da_compra = float(input('Valor da compra: '))

if 0 < valor_da_compra < 200:
    print('\n' + ('*' * 22) + ' RECIBO ' + ('*' * 22) + '\n'
          f'Valor da compra: R${valor_da_compra:.2f}\n'
          f'Juros:R$0.00\n'
          f'Total a pagar: R${valor_da_compra:.2f}\n')


else:
    ehValido = 'sim'
    if valor_da_compra == 0:
        print(f'\n'+ ('*' * 22) + ' RECIBO ' + ('*' * 22) + '\n')
        print('Operação inválida...')

    else:
        if valor_da_compra >= 200:

            print('Escolha uma opção:\n'
                  '1 - Pagamento à vista\n2 - Pagamento em 3X\n'
                  '3 - Pagamento em 5X\n4 - Pagamento em 10X')

            forma_de_pagamento = int(input('Informe a opção do pagamento: '))

            if 0 < forma_de_pagamento < 5:
                juros = 0
                parcelamento = ''
                numero = 0

                if forma_de_pagamento == 1:
                    numero = 0

                elif forma_de_pagamento == 2:
                    numero = 3


                elif forma_de_pagamento == 3:
                    juros = valor_da_compra * 0.02
                    numero = 5


                elif forma_de_pagamento == 4:
                    juros = valor_da_compra * 0.08
                    numero = 10


            else:
                ehValido = 'não'
                print('\n'+ ('*' * 22) + ' RECIBO ' + ('*' * 22) + '\n'
                      'Operação inválida...')

            if ehValido == 'sim':
                total_compra = valor_da_compra + juros
                if numero == 0:
                    parcelamento = 'Sem parecelas'
                else:
                    parcelamento = f'{numero} parcelas de R${total_compra / numero:.2f}'
                print('\n'+ ('*' * 22) + ' RECIBO ' + ('*' * 22) + '\n'
                      f'Valor da compra: R${valor_da_compra:.2f}\n'
                      f'Juros:R${juros:.2f}\n'
                      f'Total a pagar: R${total_compra:.2f}\n'
                      f'Parcelamentos: {parcelamento}')
