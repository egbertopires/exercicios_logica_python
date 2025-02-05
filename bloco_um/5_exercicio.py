print('Prezado(a) cliente,\n'
      'Escolha o produto que deseja compar\n'
      '1 - Maçã\n'
      '2 - Laranja\n'
      '3 - Banana\n')
id_produto = int(input('Código do produto: '))
quantidade_produto = int(input('Quantidade de unidades desejada: '))

valor_produto = ''
produto_escolhido = ''
preco_unitario = 0
retorno = 'sim'
if id_produto == 1:
    produto_escolhido = 'MAÇÃ'
    preco_unitario = 2.30
else:
    if id_produto == 2:
        produto_escolhido = 'LARANJA'
        preco_unitario = 3.60
    else:
        if id_produto == 3:
            produto_escolhido = 'BANANA'
            preco_unitario = 1.85
        else:
            retorno = 'não'

valor_produto = quantidade_produto * preco_unitario
print('\n'+ ('*' * 10) + ' RECIBO ' + ('*' * 10) + '\n')
if retorno == 'sim':
    print(f'PRODUTO: {produto_escolhido}\n'
          f'{quantidade_produto}u x R${preco_unitario:.2f} = R${valor_produto:.2f}')
else:
    print("Código inexistente")