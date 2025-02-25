from utilitarios_bloco3 import linha, cabecalho,sucessor_antecessor

print('Digite um número inteiro e descubra os padrão oculto!')

contagem = 0
while True:
    if contagem < 3:
        try:
            valor_numerico = int(input('Digite o número inteiro: '))
        except:
            if contagem < 2:
                print(f'{linha(50)}\n'
                      f'Insira apenas valores inteiros.')
        else:
            print(f'{cabecalho('RESULTADO DA OPERAÇÃO',50)}\n'
                  f'{sucessor_antecessor(valor_numerico)}')
            break
        finally:
            contagem += 1
    else:
        print(f'{linha(50)}\n'
              f'Tentativas execedidas. Finalizando programa...')
        break







