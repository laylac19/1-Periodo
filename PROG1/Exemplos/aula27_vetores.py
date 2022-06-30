# Videoaula - Exercício 1

## Ler e validar UMA nota entre 0 e 10
def lerNota() :
    n = float( input("Digite uma nota: "))
    while n < 0 or n > 10 :
        print("Nota inválida!") 
        n = float( input("Digite uma nota: "))
    return n



## Ler várias notas e ARMAZENA em um vetor
def lerVetorNotas( vetNotas ):
    continuar = "S"
    while continuar == "S" :
        nota = lerNota()
        vetNotas.append( nota )
        continuar = input("Deseja continuar? ")
        continuar = continuar.upper()



## Calcular a média das notas armazenadas no vetor
def calcularMedia( vetor ):
    soma = 0
    i = 0
    while i < len(vetor) :
        soma = soma + vetor[i]
        i = i + 1
    media = soma/len(vetor)
    return media 



def imprimir( vetor ):
   i = 0
   while i < len(vetor) :
      print("Nota %d = %.1f" %(i, vetor[i]))
      i = i + 1



    
#######################
notasAluno = []	 # Cria o vetor vazio
lerVetorNotas(notasAluno)
media = calcularMedia (notasAluno)
print("Média %2.1f" %media)
imprimir(notasAluno)


















