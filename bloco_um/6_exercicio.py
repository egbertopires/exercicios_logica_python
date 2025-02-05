print('Vamos formar um triângulo?!\n'
      'Insira três números reais e descubra sua classificação.')

lado_um = float(input('Primeiro lado: '))
lado_dois = float(input('Segundo lado: '))
lado_tres = float(input('Terceiro lado: '))

soma_um = lado_um + lado_dois > lado_tres
soma_dois = lado_um + lado_tres > lado_dois
soma_tres = lado_dois + lado_tres > lado_um

print('\n'+ ('*' * 20) + ' RESULTADO ' + ('*' * 20) + '\n')
if soma_um and  soma_dois and soma_tres:
    if lado_um == lado_dois == lado_tres:
        print('Três lados iguais: Triângulo equilátero')
    else:
        if lado_um != lado_dois != lado_tres:
            print('Três lados diferentes: Triângulo escaleno')
        else:
            print('Dois lados iguais: Triângulo isósceles')
else:
    print('Os números reais inseridos não formam um triângulo')