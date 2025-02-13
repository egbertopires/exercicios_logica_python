print('Por favor, insira apenas números inteiros.')

tabuada = int(input('Digite o número para calcular a tabuada: '))


tentativas = 0

while True:
    final_tabuada = int(input('Até qual número deseja calcular a tabuada? '))
    tentativas += 1
    if tentativas == 3:
        print('\nNúmero máximo de tentativas atingido. Encerrando o programa....')
        break
    if final_tabuada > 0:
        print(f'\nTabuada do número {tabuada}')

        for i in range(0 , final_tabuada + 1):

            print(f'{tabuada} X {i} = {tabuada * i}')

        break
    else:
        print("Por favor, insira um número positivo")





