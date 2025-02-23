print('Apresentando as tabuadas de 1 até 10.')

for tabuada in range (1, 10 + 1):
    print(f'TABUADA DO NÚMERO {tabuada}')
    for multiplicando in range (1, 10 + 1):
        print(f'{tabuada} x {multiplicando} = {tabuada * multiplicando}')