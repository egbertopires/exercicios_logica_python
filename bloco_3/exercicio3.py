from utilitarios_bloco3 import somar_intervalo,validaInteiro, linha, cabecalho

print('Digite dois valores inteiros e positivos para calcular o somatório do intervalo entre eles.')

print(linha(50))

primeiro_valor = validaInteiro(50,'Primeiro valor')

if primeiro_valor == 'não':

    print("Excesso de tentativas. Programa encerrado.")

else:

    print(linha(50))

    segundo_valor = validaInteiro(50,'Segundo valor')

    if segundo_valor == "não":

        print(linha(50))

        print("Excesso de tentativas. Programa encerrado.")

    elif segundo_valor < primeiro_valor:

        print(linha(50))

        print("O segundo valor é menor que o primeiro. Programa encerrado.")

    else:

        print(cabecalho('RESULTADO DA OPERAÇÃO',50))

        print(f'A soma de todos os valores de {primeiro_valor} a {segundo_valor} é igual a {somar_intervalo(primeiro_valor,segundo_valor)}.')
