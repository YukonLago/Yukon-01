nome = 'João Victor Prado Lago'
print('Seja bem-vindo a Loja LG!\nAqui quem fala é João Victor Prado Lago.')
print("Farei uma análise de seu crédito conosco. Por favor responda as seguintes perguntas:")
limite = 0
idade = 0


def obter_limite():
    cargo =("Qual o seu cargo?")
    salario = 'Qual o seu salário? R$'
    ano = 'Qual o seu ano de nascimento?'
    print('Cargo:', cargo)
    print('Salário:', salario)
    print('Ano de nascimento:', ano)
    global idade
    idade = 30
    print('Sua idade é:', idade)
    global limite
    limite = 3000
    print('Seu limite é:', limite)
    return limite, idade


obter_limite()
preco_prod = 0


def verificar_produto():
    nome_prod =('Por favor digite o nome do produto:')
    global preco_prod
    preco_prod = float('Agora digite o preço do produto:')
    return preco_prod


n = 'Quantos produtos gostaria de cadastrar?'
i = 0
total = 0

print('O preço total dos produtos é: 100')


if total <= (limite * 60) / 100:
    print('Liberado!')
elif (limite * 60) / 100 < total <= (limite * 90) / 100:
    print('Liberado ao parcelar em até 2 vezes.')
elif (limite * 90) / 100 < total <= limite:
    print('Liberado ao parcelar em 3 ou mais vezes')
else:
    print('Bloqueado!')
if len(nome) <= total <= idade:
    print('Você recebeu um desconto de 4%')
    print('O preço final do produto com o desconto ficou:', preco_prod - (preco_prod * 0.04))