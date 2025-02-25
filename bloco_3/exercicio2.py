from utilitarios_bloco3 import linha, cabecalho, fatorial, validaInteiro

print('Digite um número interio e calcule seu fatorial.\n')

operacao = validaInteiro(50)

if operacao == 'não':
    print(linha(50))
    print('Programa encerrado...')
else:
    print('\n' + cabecalho(f'FATORIAL DO NÚMERO {operacao}', 50) + '\n')
    print(fatorial(operacao))
