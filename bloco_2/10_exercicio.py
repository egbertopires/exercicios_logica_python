print('Imprimindo todos os números primos de 2 a 99')
numeros_primos = 'Números primos: '
for numero in range (2, 99 + 1):
    e_primo = True
    for primo in range (2,  numero):
        if numero % primo == 0:
            e_primo = False
            break
    if e_primo:
        numeros_primos += f'{numero}, '

print(numeros_primos[:-2])



