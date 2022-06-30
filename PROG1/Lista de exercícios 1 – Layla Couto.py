#QUESTÃO 1

numero1 = int(input ("Informe um número: ") )
numero2 = int(input ("Informe um número: ") )

soma = numero1 + numero2
print("A soma dos números é: %d" %soma)

#QUESTÃO 2

nome = input("Informe seu nome: ")
nota1 = float( input ("Informe sua nota 1: ") )
nota2 = float( input ("Informe sua nota 2: ") )
nota3 = float( input ("Informe sua nota 3: ") )
nota4 = float( input ("Informe sua nota 4: ") )

media = (nota1 + nota2 + nota3 + nota4)/4
print("%s, sua média no bimestre é: %.1f" %(nome,media))

#QUESTÃO 3

d = int (input ("Quantos Dias: ") )
h = int (input ("Quantas Horas: ") )
m = int (input ("Quantos Minutos: ") )
s = int (input ("Quantos Segundos: ") )

segundos = s + ((m*60) + (h*3600) + (d*86400))
print("O Total de Segundos é: %d" %segundos)

#QUESTÃO 4

sal = float (input ("Insira o Valor do Salário: "))
por = float (input("Insira o Percentual do Aumento: "))

aumento = sal* (por/100)
novoSal = sal + aumento
print("O Valor do aumento será de R$%.2f. O novo salário é R$%.2f" %(aumento,novoSal))


#QUESTÃO 5

prod = input("Nome do Produto: ")
qtde = int ( input("Quantidade do Produto: "))
preco = float ( input("Preço do Produto: "))
por = float ( input ("Desconto: "))

valor = qtde * preco
desc = valor * (por/100)
valorpg = valor - desc

print("%s possui R$%.2f de desconto. O valor a ser pago é de R$%.2f" %(prod,desc,valorpg))

#QUESTÃO 6

print("Calcular Tempo De Viagem")
d = float(input ("Qual a Distância a Percorrida em km? "))
v = float(input ("Qual a Velocidade Média da Viagem? "))

tempo = d / v

print ("Tempo de viagem em horas foi %.2f" %tempo)

#QUESTÃO 7

C = float (input("Informe a temperatura em Celsius: "))
F = (9 *(C/5)+ 32)

print("A temperatura em  Fahrenheit é %.f" %F)

#QUESTÃO 8

F = float (input("Informe a temperatura em Fahrenheit: "))

C = (F - 32)* 5/9
print("A temperatura em   Celsius é %.f" %C)

#QUESTÃO 9

km = float (input("Infome a quantidade de km percorridos: "))
dias = int (input("Por quantos dias o carro ficou alugado? "))

valorPg = (60*dias) + (0.15*km)

print("O valor a pagar é de R$ %.2f" %valorPg)

#QUESTÃO 10

qtdeC = int (input("Informe a quantidade de cigarros fumados por dia: "))
qtdeAnos = int (input("Informe quantos anos já fumou: "))

totalC = (qtdeAnos * 365) * qtdeC
diasP = (totalC * 10)/24

print ("Dias perdidos: %d" %diasP)

#QUESTÃO 11

num = str(int(2**1000000))
print('A quantidade de digitos é: %s' %len(num))
