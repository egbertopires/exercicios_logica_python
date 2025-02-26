from utilitarios_bloco3 import contar_string
print("Reponda as perguntas e veja o pradão oculto")

texto = input('Digite um texto: ').upper().strip()
verificar = input('Qual letra deseja contar? ').upper().strip()
while len(verificar) > 1:
    print('Somente uma letra é aceita.')
    verificar = input('Qual letra deseja contar? ').upper().strip()

print(contar_string(texto, verificar))