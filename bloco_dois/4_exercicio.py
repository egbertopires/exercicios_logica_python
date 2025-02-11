print('Digite dois números inteiros e descubra os padrões ocultos entre eles!')
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

contador_positivos = 0
somatorio_positivos = 0
contador_pares = 0
somatorio_pares = 0
contador_impar = 0
somatorio_impares = 0
intervalo_numerico = 'Intervalo numérico: '

for i in range(primeiro_numero, segundo_numero + 1):
    if i > 0:
        contador_positivos += 1
        somatorio_positivos += i
        if i % 2 == 0:
            contador_pares += 1
            somatorio_pares += i
        if i % 2 == 1:
            contador_impar += 1
            somatorio_impares += i

media_positivo =  somatorio_positivos / contador_positivos
media_pares = somatorio_pares / contador_pares
media_impar = somatorio_impares / contador_impar

print(f'\nRESULATADO\n'
      f'Quantidade de números inteiros e positivos: {contador_positivos}\n'
      f'Média: {media_positivo}\n'
      f'Quantidade de números pares: {contador_pares}\n'
      f'Média: {media_pares}\n'
      f'Quantidade de números impares: {contador_impar}\n'
      f'Média: {media_impar}')

