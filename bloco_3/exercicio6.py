from utilitarios_bloco3 import linha, validaInteiro,cabecalho
print('Insira 10 números inteiros e positivos e descubra os padrões ocultos.')

numeros_aleatorios = []
crescer = ''
diminuir = ''
while True:
    if len(numeros_aleatorios) < 10:
        print(linha(50))
        numero_aleatorio = validaInteiro(50, "Digite um número")
        if numero_aleatorio == "não":
            print(f"{linha(50)}\nPrograma encerrado por execesso de tentativas.")
            break
        numeros_aleatorios.append(numero_aleatorio)
    else:
        numeros_aleatorios.sort()
        inverso = numeros_aleatorios[:]
        inverso.reverse()
        for crescente in numeros_aleatorios:
            crescer += f'{crescente}, '
        for decrescente in inverso:
            diminuir += f'{decrescente}, '
        print(f"{cabecalho("RESULTADO", 50)}\n"
              f"Ordem crescente: {crescer[:-2]}\n"
              f"Ordem decrescente: {diminuir[:-2]}\n"
              f"Maior número: {max(numeros_aleatorios)}\n"
              f"Menor número: {min(numeros_aleatorios)}\n"
              f"Soma de todos os números: {sum(numeros_aleatorios)}\n"
              f"Média: {sum(numeros_aleatorios) / len(numeros_aleatorios):.2f}")
        break


