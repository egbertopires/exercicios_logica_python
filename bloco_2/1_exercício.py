print('digite um número para iniciar a contagem e outro número para finalizar.\n'
      'O programa mostrará todos os números pares nesse intervalo')

contagem_inicial = int(input('Digite o primeiro número inteiro: '))

contagem_final = int(input('Digite o segundo número inteiro: '))

contador = contagem_inicial

mensagem = "Números pares: "
while contador <= contagem_final:
      if contador % 2 == 0:
            mensagem += f'{contador},'
      contador += 1
print(mensagem[:-1])