print('Escolha um número inteiro positivo ou não e veja o que acontece')
numero_inteiro = int(input('Insira o número inteiro: '))

print('\n'+ ('*' * 22) + 'RESULTADO' + ('*' * 22) + '\n')
if 1 <= numero_inteiro <= 100:
    print(f'Pertence ao intervalo: 1 < {numero_inteiro} < 100')
else:
    if -100 <= numero_inteiro <= -1:
        print(f'Pertence ao intervalo: -100 < {numero_inteiro} < -1')
    else:
        print(f'O número {numero_inteiro} não tem intervalo definido.\n'
              'Fim...')
