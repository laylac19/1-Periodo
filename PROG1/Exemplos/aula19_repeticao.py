# MATRIZ - while aninhados

maxLinhas = int (input ("Total de linhas: ") )
maxColunas = int (input ("Total de colunas: ") )
lin = 1 		# Índice da linha
col = 1 		# Índice da coluna
while lin <= maxLinhas :
    col = 1
    while col <= maxColunas :
        print ("#" , end="")
        col = col + 1
    lin = lin + 1
    print()




