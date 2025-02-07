print('Insira um número inteiro para verificar se é par ou ímpar.\n')

verificar_numero = int(input('Digite um número inteiro: '))

print('\n'+ ('*' * 22) + 'RESULTADO' + ('*' * 22) + '\n')

if verificar_numero % 2 == 0:
    print(f"O número {verificar_numero} é par")
else:
    print(f"O número {verificar_numero} é ímpar")