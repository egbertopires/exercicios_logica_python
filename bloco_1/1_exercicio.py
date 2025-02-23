ano_usuario = int(input('Qual o seu ano de nascimento? '))
ano_atual = int(input('Informe o ano atua: '))
maior_de_iadade = ano_atual - ano_usuario

if maior_de_iadade >= 18:
    print(f"Você possui {maior_de_iadade} anos já pode solicitar a  carteira de habilitação")
else:
    print(f"Ops! Sua idade é  {maior_de_iadade} anos. Espere mais um pouco.")
