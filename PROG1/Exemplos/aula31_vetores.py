# Videoaula Pesquisar e excluir


## Ler vários nomes e ARMAZENA em um vetor
def lerNomes( vetor ):
    nome = input("Nome: ")
    while nome.upper() != "FIM" :
        vetor.append( nome )
        nome = input("Nome: ")


def pesquisarNome (vetor, pesq):
    for i, e in enumerate(vetor) :
        if e.upper() == pesq.upper():
            return i;
    return -1	


### PRINCIPAL ####

vNomes = []	# Cria o vetor vazio
print("Informe os nomes e digite 'FIM' para terminar")
lerNomes(vNomes)

while True:
    pesq = input("Nome para pesquisar: ")
    pos = pesquisarNome (vNomes, pesq)

    if pos >= 0:
        print("Nome encontrado e excluído: %s" %vNomes[pos] )
        del ( vNomes[pos] )   # remover do vetor
        
    else:
        print("Nome não encontrado.")
