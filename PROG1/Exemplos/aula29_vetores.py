## Videoaula: Exercício 3

def lerDados( vetNomes, vetTelefones ):
    continuar = "S"
    while continuar == "S" :
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        vetNomes.append( nome )
        vetTelefones.append( telefone )

        continuar = input("Deseja continuar? ")
        continuar = continuar.upper()


def imprimirLetra( vetNomes, vetTelefones ):
    i = 0
    letra = input("Informe a letra para pesquisar: ")
    while i < len(vetNomes) :
        nome = vetNomes[i]
        if nome[0].upper() == letra.upper():
            print("Nome %s -  %s" %(vetNomes[i], vetTelefones[i]) )
        i = i + 1
      
    
##### PRINCIPAL ##########
vNomes = []
vTelefones = []
lerDados(vNomes, vTelefones)
imprimirLetra(vNomes, vTelefones)





