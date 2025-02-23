print('Que tal ver um tabuada?\n'
      'Siga o que for pedido.')

tabuada = int(input('Tabuada do número: '))
contador = 1
print(f'TABUADA DO NÚMERO {tabuada}')
while contador <= 10:
    print(f'{tabuada} x {contador} = {tabuada * contador}')
    contador += 1