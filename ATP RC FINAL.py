nome = 'João Victor Prado Lago'
print('Seja bem-vindo a Loja LG!\nAqui quem fala é João Victor Prado Lago.')
print("Farei uma análise de seu crédito conosco. Por favor responda as seguintes perguntas:")
limite = 0
idade = 0


def obter_limite():
    cargo = input("Qual o seu cargo?")
    salario = float(input('Qual o seu salário? R$'))
    ano = float(input('Qual o seu ano de nascimento?'))
    print('Cargo:', cargo)
    print('Salário:', salario)
    print('Ano de nascimento:', ano)
    global idade
    idade = idade + (2020 - ano)
    print('Sua idade é:', idade)
    global limite
    limite = limite + float((salario * (idade / 1000) + 100))
    print('Seu limite é:', limite)
    return limite, idade


obter_limite()
preco_prod = 0


def verificar_produto():
    nome_prod = input('Por favor digite o nome do produto:')
    global preco_prod
    preco_prod = float(input('Agora digite o preço do produto:'))
    return preco_prod


n = int(input('Quantos produtos gostaria de cadastrar?'))
i = 0
total = 0
for i in range(1, n+1):
    verificar_produto()
    i += 1
    total += preco_prod

print('O preço total dos produtos é: {}'.format(total))


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