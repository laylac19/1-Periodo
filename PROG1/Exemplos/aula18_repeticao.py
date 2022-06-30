# Desenvolver um programa que leia o nome e a altura de um grupo de pessoas.
# Este programa deverá calcular e mostrar:
#    a) A altura média do grupo;
#    b) A menor altura do grupo e o nome da pessoa;
#    c) A maior altura do grupo e o nome da pessoa;


maiorAltura = 0     # Armazena a MAIOR altura
nomeMaior = ""      # Armazena o nome da pessoa com a MAIOR altura

menorAltura = 0     # Armazena a MENOR altura
nomeMenor = ""      # Armazena o nome da pessoa com a MENOR altura

cont = 0            # Contador de pessoas
somaAltura = 0      # Soma todas as alturas para tirar a média

continuar = "S"
while continuar == "S" :
    #Ler o nome
    nome = input("Nome: ")
    
    #Ler e validar a altura
    altura = float (input("Altura: "))
    while altura <= 0 or altura > 3 :
        print("Altura inválida!")
        altura = float (input("Altura: "))

    somaAltura = somaAltura + altura
    cont = cont + 1

    if cont == 1:
        maiorAltura = altura
        menorAltura = altura
        nomeMaior = nome
        nomeMenor = nome

    #Testar MAIOR
    if altura > maiorAltura :
        maiorAltura = altura
        nomeMaior = nome

    #Testar MENOR
    if altura < menorAltura :
        menorAltura = altura
        nomeMenor = nome
    
    continuar = input("Deseja continuar? (S/N)")
    continuar = continuar.upper()


#Calcular a média
media = somaAltura / cont
    
#Imprimir as mensagens
print("A altura média do grupo é %.2f"  %media)
print("%s possui %.1f e é a MENOR altura do grupo" %(nomeMenor,menorAltura))
print("%s possui %.1f e é a MAIOR altura do grupo" %(nomeMaior,maiorAltura))
