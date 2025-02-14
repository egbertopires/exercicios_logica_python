print('Calculando a média de todos os números pares de 1 até 100.\n')

somatorio_pares = 0

quantidade_pares = 0

for numeros in range (1, 100 + 1):

    if numeros % 2 == 0:

        somatorio_pares += numeros

        quantidade_pares += 1

print("RESULTADO DOS NÚMEROS PARES\n"
      f"Quantidade: {quantidade_pares}\n"
      f"Somatório: {somatorio_pares}\n"
      f"Média: {somatorio_pares / quantidade_pares}")