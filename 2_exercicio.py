print("Prezado(a) colaborador(a),\n"
      "Informe o ano de sua contratação e seu salário para calcular sua bonificação.")

ano_contratacao = int(input('Qual seu ano de contratação: '))

salario = float(input('Qual o seu salário: '))

resultado = 2025 - ano_contratacao

resultado_saida = ''

if resultado < 2:
      resultado_saida = f"{resultado} ano"
else:
      resultado_saida = f"{resultado} anos"

if resultado >= 5:
      print(f'{"=" * 50}\n'
            f'Tempo de empresa: {resultado_saida}\n'
            f'Salário: R${salario:.2f}\n'
            f'Bonificação: R${salario * 0.2:.2f}\n'
            f'Salário bonificado: R${salario * 1.2:.2f}')
else:
      print(f'{"=" * 50}\n'
            f'Tempo de empresa: {resultado_saida}\n'
            f'Salário: R${salario:.2f}\n'
            f'Bonificação: R${salario * 0.1:.2f}\n'
            f'Salário bonificado: R${salario * 1.1:.2f}')