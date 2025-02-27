from utilitarios_bloco3 import validaInteiro, linha

print('Insira números inteiros e positivos e veja a ordem crescente e decrescente.\n'
      'Digite 0 para exibir o resultado e encerrar o programa.')

lista_de_numeros = []
while True:
    print(linha(50))
    pergunta = validaInteiro(50,'Insira um valor')
    if pergunta == 'não':
        print(linha(50))
        print('programa encerrado')
        break
    elif pergunta == 0:
        lista_de_numeros.sort()

        referencia = lista_de_numeros[:]

        referencia.reverse()

        texto_final_um,texto_final_dois = '',''

        for ordem_um in lista_de_numeros:
            texto_final_um += f'{ordem_um}, '

        for ordem_dois in referencia:
            texto_final_dois += f'{ordem_dois}, '

        print(linha(50))
        print(f'Ordem crescente: {texto_final_um[:-2]}')

        print(f'\nOrdem decrescente: {texto_final_dois[:-2]}')
        break
    else:
        lista_de_numeros.append(pergunta)
