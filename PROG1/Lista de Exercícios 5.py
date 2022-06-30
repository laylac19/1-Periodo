#QUESTÃO 1
import random

def gerarNumAleatorio(min,max) : 
    return random.randint(min,max)

def lerVetNum(vetor) :
    count = 0
    p = 0
    im = 0
    while count < 50 :
        num = gerarNumAleatorio(1,100)
        vetor.append(num)
        if (num % 2) == 0 :
            p = p + 1
        else:
           im = im + 1
        count = count + 1
    print ("Quantidade de números pares: %d" %p)
    print ("Quantidade de números impares: %d" %im)

def imprimir(vetor) :
    i = 0
    while i < len(vetor) :
        print ("Número %d = %.0f" %(i, vetor[i]))
        i = i + 1

### PRINCIPAL ###
vetNum = [ ]
lerVetNum(vetNum)
imprimir(vetNum)


#QUESTÃO 2
import random

def gerarNumAleatorio(min,max) : 
    return random.randint(min,max)

def lerVetNum(vetor, pares, impares) :
    count = 0
    while count < 50 :
        num = gerarNumAleatorio(1,100)
        vetor.append(num)
        if (num % 2) == 0 :
            pares.append(num)
        else:
           impares.append(num)
        count = count + 1

def imprimir(vetor) :
    i = 0
    while i < len(vetor) :
        print ("Número = %d" %vetor[i])
        i = i + 1

### PRINCIPAL ###
vetNum = [ ]
vetpar = [ ]
vetimpar = [ ]
lerVetNum(vetNum, vetpar, vetimpar)
imprimir(vetNum)
print ("\n----------Pares-----------\n")
imprimir(vetpar)
print ("\n--------Impares-----------\n")
imprimir(vetimpar)


#QUESTÃO 3
import random

def gerarNumAleatorio() :
    return random.randint(0,20)

def lerVetNum(v1) :
    cont = 0
    while cont < 20 :
        num1 = gerarNumAleatorio()
        v1.append( num1 )
        cont = cont + 1

def lerVetNum(v2) :
    cont = 0
    while cont < 20 :
        num2 = gerarNumAleatorio()
        v2.append( num2 )
        cont = cont + 1

def lerVetNum3(v1, v2, v3) :
    v3 = v1 + v2
    return v3

def imprimir(v1) :
    i = 0
    while i < len(v1) :
        print ("Número %d = %.0f" %(i, v1[i]))
        i = i + 1

### PRINCIPAL ###
vetNum1 = [ ]
vetNum2 = [ ]
vetNum3 = [ ]

lerVetNum(vetNum1)
lerVetNum(vetNum2)
vet3 = lerVetNum3(vetNum1, vetNum2, vetNum3)

imprimir(vetNum1)
print ("\n---------------------\n")
imprimir(vetNum2)
print ("\n---------------------\n")
imprimir(vet3)

    
#QUESTÃO 4




#QUESTÃO 5
def lerDados( vetNomes, vetMedias ):
    encerrar = "N"
    while encerrar == "N" :
        count = 0
        soma = 0
        
        nome = input ("Nome: ")
        vetNomes.append( nome )
        
        while count < 3 :
            nota = float (input ("Nota: "))
            soma = soma + nota
            count = count + 1
            
            media = soma / count
            vetMedias.append( media )

        if media >= 7 :
            print ("Média do aluno(a): %.1f" %media)

        encerrar = input ("Deseja encerrar? ")
        encerrar = encerrar.upper()

### PRINCIPAL ###
vNomes = [ ]
vMedia = [ ]
lerDados(vNomes, vMedia)


#QUESTÃO 6
def lerDados( vetPeso, vetAltura ) :
    p = float (input ("Insira o peso: "))
    while p <= 0 :
        print ("Peso Informado é Invalido!\nInsira Novamente.")
        p = float (input ("Insira o peso: "))
    vetPeso.append( p )
        
    a = float (input ("Insira a altura: "))
    while a <= 0 :
        print ("Altura Informada é Invalida!\nInsira Novamente.")
        a = float (input ("Insira a altura: "))
    vetAltura.append( a )

def calcularIMC( vetPeso, vetAltura, vetIMC) :
    for i in range(len(vetPeso)):
        imc = vetPeso[i] / (vetAltura[i] * vetAltura[i])
        vetIMC.append( imc )

def imprimirIMC (vetIMC) :
    i = 1
    while i < len(vetIMC)  :
        print ("IMC %d = %.2f" %(i, vetIMC[i]))
        i = i + 1
        
### PRINCIPAL ###
vPeso = [ ]
vAltura = [ ]
vIMC = [ ]

continuar = "S"
while continuar == "S" :
    lerDados( vPeso, vAltura )
    calcularIMC( vPeso, vAltura, vIMC )

    continuar = input("Deseja continuar? ")
    continuar = continuar.upper()

imprimirIMC (vIMC)


#QUESTÃO 7
votos = [0] * 25 # vetor com 25 posicoes com início vazio
numCamisa = -1
total = 0
print ("Enquete: Quem foi o melhor jogador? ")
i = 1
while numCamisa != 0 :
    numCamisa = int (input ("Numero do jogador (0=fim): "))
    
    if numCamisa < 0 or numCamisa > 25 :
        print ("Informe um número (entre 1 e 25) ou 0 para sair!")
        votos[i - 1] -= 1
        total -= 1
    else :
        votos[numCamisa - 1] += 1
        total += 1
        
print ("\n")
print ("Resultado da votação:")
print ("\n")
print ("Foram computados %d votos" %total)
print ("\n")
print ("Jogador \t Votos \t %%")

count = 1
jogadorM = 0

for i in range (len (votos)) :
    if len (votos) > 0 :
        
        if votos[i] > 0 :
            print ("%d \t %d \t %.1f%%" %(count, votos[i], (votos[i] / float ( total ) * 100 )))

    if votos[i] == 1 :
        count = jogadorM
                    
    if  votos[i]  > jogadorM:
        jogadorM = count

    count = count + 1

print ("O melhor jogador foi o numero %d, com %d votos, correspondendo a %.1f%% do total de votos"  %( jogadorM, (votos[jogadorM] + 1), ( (votos[jogadorM] + 1)/ float ( total  ) * 100 ) ))
