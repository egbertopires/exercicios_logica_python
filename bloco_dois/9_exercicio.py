print('Para encerrar o programa digite um número inteiro negativo ou zero.')

while True:
    idade = int(input('Informe sua idade: '))

    if idade <= 0:
        print('Programa encerrado...')
        break
    else:
        tentativa = 0
        while True:
            genero = str(input('Qual seu gênero? [Inserir: F | M]: '))
            tentativa += 1
            if tentativa == 3:
                break
            else:
                if genero == 'F' or genero == 'f':
                    print(f"Boa noite, senhora. Sua idade é {idade}")
                    break
                elif genero == 'M' or genero == 'm':
                    print(f"Boa noite, senhor. Sua idade é {idade}")
                    break
                else:
                    print('Digite "F" para feminino e "M" para masculino.')
        if tentativa == 3:
            print('\nTentativas excedidas. Programa encerrado...')
            break
        elif genero == 'F' or genero == 'f' or genero == 'M' or genero == 'm':
            break






