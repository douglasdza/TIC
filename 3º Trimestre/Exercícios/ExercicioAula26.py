'''
3. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 7.5% para o Imposto de Renda, 8% para o INSS e 1% para o sindicato.
Faça um programa que nos dê:
    — salário bruto.
    — quanto pagou de imposto de renda (calcule sobre o salário bruto).
    — quanto pagou ao INSS (calcule sobre o salário bruto).
    — quanto pagou ao sindicato (calcule sobre o salário bruto).
    — o salário líquido (o que sobrou após os descontos).

+ Salário Bruto: R$
- IR (7.5%): R$
- INSS (8%): R$
- Sindicato (1%): R$
= Salário Líquido: R$

Obs.: apresente os descontos e o salário líquido, conforme o esquema acima.
'''

# Exercício 1 — Faça um Programa que peça dois números e imprima a soma deles.:

num1 = input("Digite um número: ")
num2 = input("Digite um número: ")
soma = int(num1) + int(num2)

if(num1 + num2):
    print("A soma de dois números é {}".format(soma))
###############################################################################

# Exercício 2 — Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius.:

farenheit = input("Digite a temperatura em graus Farenheit")
num = 5
num2 = 32
num3 = 9
celsius = num*(farenheit-num2)/num3

if(num*(farenheit-num2)/num3)
    print("A temperatura em Celsius é {}".format(celsius))
