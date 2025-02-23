print('Prezado(a) aluno(a) do curso técnico de enfermagem,\n'
      'Insira as notas das seguintes matérias e descubra sua situação:')

materia_um = float(input('Anatomia e Fisiologia: '))
materia_dois = float(input('Procedimentos de Enfermagem: '))
materia_tres = float(input('Ética e Legislação em Enfermagem : '))

media = (materia_um + materia_dois + materia_tres) / 3
situacao = ''
if materia_um >= 7 and materia_dois >= 7 and materia_tres >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'

print('\n'+ ('*' * 22) + 'BOLETIM' + ('*' * 22) + '\n\n'
      f'Anatomia e Fisiologia {"-" * 21} {materia_um:.2f}\n'
      f'Procedimentos de Enfermagem {"-" * 15} {materia_dois:.2f}\n'
      f'Ética e Legislação em Enfermagem {"-" * 10} {materia_tres:.2f}\n\n'
      f'Situação: {situacao}')
