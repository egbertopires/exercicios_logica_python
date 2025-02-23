print('Digite números inteiros e descubra os padrões ocultos entre eles!\n'
      'Obeservação: "0 (zero)" encerra o programa.\n')

contar_numero = 0
somar_numero = 0
linha = '*' * 20
while True:

    numero = int(input('Número: '))

    if numero >= 0:
        if numero:
            contar_numero += 1
            somar_numero += numero
        else:
            if contar_numero > 0:
                print(f'{linha}\n'
                      f'Números inetiros maiores que zero.\n'
                      f'Quantidade: {contar_numero}\n'
                      f'Somatório: {somar_numero}\n'
                      f'Media: {somar_numero/contar_numero:.2f}')
                break
            else:
                print(f"{linha}\n"
                      f"Não foram digitados números inetiros maiores que zero.\n"
                      "Programa enecerrado...")
                break


