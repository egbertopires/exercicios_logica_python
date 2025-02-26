#Funções exercícios1:
def sucessor_antecessor(numero):
    intervalo_numerico = 'Intervalo numérico: {'
    for intervalo in range (numero - 2, numero+3):
        intervalo_numerico += f'{intervalo}, '
    return f'{intervalo_numerico[:-2]}' + "}"

def linha(quantidade = 10):
    return "=" * quantidade

def cabecalho(texto,quantidade = 10):
    return (f'{linha(quantidade)}\n'
            f'{texto.center(quantidade)}\n'
            f'{linha(quantidade)}')

############################################################
#Funções exercícios2:
def fatorial(numero = 0):
    if numero == 0:
        return "0! = 1"
    else:
        intervalo = f'{numero}! = '
        resultado = 1
        for fator in range (numero, 0,-1):
            intervalo += f'{fator} x '
            resultado *= fator
        return f'{intervalo[:-2]}= {resultado}'

def validaInteiro(quantidade = 0, texto1 = 'Digite o número inteiro'):
    tentativa = 0
    while tentativa < 3:
        try:
            valor_numerico = int(input(f'{texto1}: '))
            if valor_numerico >= 0:
                return valor_numerico
                break
            else:
                if tentativa < 2:
                    print(linha(quantidade))
                    print('Apenas valores positivos')
        except:
            if tentativa < 2:
                print(linha(quantidade))
                print('Insira apenas valores númericos inteiros.')
                continue
        finally:
            tentativa += 1


    if tentativa >= 3:
        return 'não'

###################################################
#funções do exercício três

def somar_intervalo(numero_um,numero_dois):
    somatorio = 0
    for numero in range (numero_um, numero_dois + 1):
        somatorio += numero
    return somatorio

def intervalo_numerico (numero_um,numero_dois):
    intervalo = '{'
    for numero in range (numero_um, numero_dois + 1):
        intervalo += f'{numero},'
    return f'{intervalo[:-2]}' + "}"

###################################################
#Funções do exercício quatro
def contar_string(texto,letra):
    string = texto
    contador = 0
    for l in string:
        if l == letra:
            contador+=1
    return contador