# 18 de setembro de 2018
# Não é necessário colocar ponto e vírgula no código pois Python não exige.

# Este é um comentário.
print("Olá mundo :D") # Exemplo de print.

print("Olá Hueco Mundo")

'''
Um comentário em bloco é definido com três aspas.
As aspas podem ser simples ou duplas.
'''

# Variáveis não necessitam definição de tipo
# Podem assumir qualquer valor/tipo.
num = 10
num = "Douglas"
num = 10.98

a = num * 10

# Jeito simples separando os parâmetros por vírgula. Fazendo isso, a vírgula fica separado com número.
print("O resultado é", num, ", certo?")

# Usando uma função para formatar a string. Ou seja, a vírgula fica junto com número.
print("O resultado é {}, certo?".format(num))

# É possível fazer desse jeito:
nome = "Douglas"
print("{}, o resultado é {}, certo?".format(nome,num))

#DICA: Use sempre o sinal {} que representa o valor de uma variável.

# Operador de potência é representado pelo símbolo **:
num = 5 ** 2 # 5 ao quadrado
num = 5 ** 3 # 5 ao cubo
num = 10 ** 8 # 10 elevado a 8

# Prioridade de operadores:
# **, *, /, + e -.

# Calculando raiz:
num = 9 ** 1 / 2 # Isso é 4,5
num = 9 ** (1/2) # Isso é raiz = 3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# A identação define que o código pertence a quem.

# Condicionais
if(num % 2 == 0): # Finaliza com dois pontos
    print("O número {} é par!".format(num))
    # Coisas do IF devem ficar identadas.
    # ...
    if(True): # True ou False sempre começa com a primeira letra em maiúscula
            # Cuide da identação!
            print("Pertence ao IF interno")

            while(True):
                print("Código do while!")

                break
# Fim do IF
else:
    print("O número {} é impar!".format(num))

# Condcionais compostas:
# && --> Em Pyhton é --> and
# || --> Em Python é --> or

'''
# Tabuada
i = 0
num = 7
while(i <= 10):
    res = i * num
    print("{} x {} = {}".format(num, i, res))
    # Não existe i++ ou i--
    # Acrescenta 1 ao valor de i
    i+= 1 # É igual a i = i + 1
'''

# Tabuada

# Toda entrada do input é string
num = input("Digite um nímero: ")
# Conversão para int() ou float()
num = int(num)

# Variável de controle
i = 0
while(i <= 10):
    res = i * num
    print("{} x {} = {}".format(num, i, res))
    # Não existe i++ ou i--
    # Acrescenta 1 ao valor de i
    i+= 1 # É igual a i = i + 1
# Fim do WHILE

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Listas, vetor, array
vetor = []

# Adicionar algo ao vetor
vetor.append(10)
vetor.append(3)
vetor.append(7)
vetor.append(8)

# Criando um vetor já preenchido
vetor = [10, 5, 19, 53, 48, 9]

# Cria vetor vazio com tamanho N
vetor = [""] * 10
vetor[0] = 19
vetor[1] = 5
vetor[9] = 12

# Pedindo para o usuário os valores...
vetor = [""] * 4
i = 0

# O len() calcula o tamanho de algo
while( i <= len(vetor) ):
    # Pede um valor, converte para int e armazena na posição
    vetor[i] = int( input("Número: ") )

    # Incremento da posição
    i = i + 1

# Mostrando o vetor
print(vetor)

# Percorrendo o vetor com o FOREACH
for x in vetor:
    print( "O vetor tem o valor {}".format(x))

    soma = soma + x

print("A soma do vetor é {}.".format(soma))

media = soma / len(vetor)

print("A média do vetor é {}.".format(media))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Funções e Classes

# Não precisa especificar tipo de parâmetro e de retor
# def nome(parâmetro):
# ...

def somar(a, b, c):
    print(a+b+c)
    # O retorno é opcional.
# Fim da função

# Classe é a mesma coisa
# class Nome(Herença)
class Aluno():
    nome = "Douglas"

    def metodo():
        return ""


#class Aluno(Pessoa):
    # A classe Aluno "extens" a classe Pessoa
    # Código da classe
