print('digite um número para iniciar a contagem e outro número para finalizar.\n'
      'O programa mostrará todos os números múltipols de três nesse intervalo\n')

contagem_inicial = int(input('Digite o primeiro número inteiro: '))

contagem_final = int(input('Digite o segundo número inteiro: '))

contador = contagem_inicial
contagem = 0
mensgem_singular = 'Número múltiplo de 3'
mensagem_plural = 'Números múltiplos de 3'
mensagem_final = ''
while contador <= contagem_final:
    if contador != 0:
        if contador % 3 == 0:
            mensagem_final += f'{contador},'
            contagem += 1
    contador += 1

if contagem == 1:
    print(f'\n{mensgem_singular}: {mensagem_final[:-1]}')
else:
    print(f'\n{mensagem_plural}: {mensagem_final[:-1]}')