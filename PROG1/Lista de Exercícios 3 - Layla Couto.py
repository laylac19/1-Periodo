#QUESTÃO 1
nomeU = str (input ("Nome de Usuário: "))
senha = str (input ("Senha: "))

while senha == nomeU :
   print ("ERRO! A senha não pode ser igual ao nome do usuário.")
   senha = str(input ("Senha: "))

   if (len(senha)) <= 6: 
      print("ERRO! A senha deve ter mais de 6 caracteres")
      senha = str(input ("Senha: "))

print ("Seu nome de usuário é %s e sua senha é %s." %(nomeU, senha))


#QUESTÃO 2
print ("    Realizar Cadastro    ")

continuar = "N"
while continuar == "N" :

   nome = str (input ("Nome: "))
   while (len(nome)) <= 3: 
      print("ERRO! O nome deve ser maior que 3 caracteres")
      nome = str (input ("Nome: "))

   idade = int (input ("Idade: "))
   while idade >= 0 and idade >= 150 :
      print ("ERRO! Insira novamente.")
      idade = int (input ("Idade: "))

   salario = float (input ("Salário: "))
   while salario <= 0 :
      print ("ERRO! Insira novamente.")
      salario = float (input ("Salário: "))
      
   sexo = input ("Sexo (F: Feminino/ M: Masculino): ")
   sexo = sexo.upper()
   while sexo != "F" and sexo != "M" :
      print ("ERRO! Insira novamente.") 
      sexo = input ("Sexo (F: Feminino/ M: Masculino): ")
      sexo = sexo.upper()

   estadoCivil = input ("Estado Civil: (S-Solteiro/ C-Casado/ V-Viúvo/D-Divorciado): ")
   estadoCivil = estadoCivil.upper()
   while estadoCivil != "S" and estadoCivil != "C" and estadoCivil != "V" and estadoCivil != "D" :
      print ("ERRO! Insira novamente.") 
      estadoCivil = input ("Estado Civil: (S-Solteiro/ C-Casado/ V-Viúvo/D-Divorciado): ")
      estadoCivil = estadoCivil.upper()

   continuar = input ("Deseja concluir o cadastro? (S/N) ")
   continuar = continuar.upper()
   
print ("    Dados    ")
print ("Nome: %s" %nome)
print ("Idade: %d" %idade)
print ("Salário: R$ %.2f" %salario)
print ("Sexo: %s" %sexo)
print ("Estado Civil: %s" %estadoCivil)


#QUESTÃO 3
nome = input ("Nome do aluno: ")
 
n1 = float (input ("Nota 1:"))
while n1 < 0 or n1 > 10 :
   print ("Nota inválida")
   n1 = float (input ("Nota 1:"))

n2 = float (input ("Nota 2:"))
while n2 < 0 or n2 > 10 :
   print ("Nota inválida")
   n2 = float (input ("Nota 2:"))

n3 = float (input ("Nota 3:"))
while n3 < 0 or n3 > 10 :
   print ("Nota inválida")
   n3 = float (input ("Nota 3:"))

media = (n1 + n2 + n3)/3

if media >= 7 :
    print ("O aluno %s foi Aprovado." %nome)  
elif media < 6 :
    print ("O aluno %s foi Reprovado." %nome)
elif 6 < media < 7 :
    print ("O aluno %s está de PROVA FINAL" %nome)

            #Ordem decrescente
if n1 > n2 > n3 :
   print ("%d, %d, %d" %(n1, n2, n3))
elif n1 > n3 > n2 :
   print ("%d, %d, %d" %(n1, n3, n2))
elif n2 > n1 > n3 :
   print ("%d, %d, %d" %(n2, n1, n3))
elif n2 > n3 > n1 :
   print ("%d, %d, %d" %(n2, n3, n1))
elif n3 > n1 > n2 :
   print ("%d, %d, %d" %(n3, n1, n2))
elif n3 > n2 > n1 :
   print ("%d, %d, %d" %(n3, n2, n1))


#QUESTÃO 4
num = 1
maiorNum = -1
totalNPar = 0
totalNImpar = 0
somaPar = 0
mediaPar = 0
somaImpar = 0
mediaImpar = 0
somaNum = 0

while num != -1:
    if (num >= 1) and (num <= 1000):
        num = int(input("Digite qualquer número entre 1 e 1000. Para parar a repetição digite -1: "))
        somaNum = somaNum + num

        if (num % 2) == 0 :
            totalNPar = totalNPar + 1
            somaPar = somaPar + num
        else:
           totalNImpar = totalNImpar + 1
           somaImpar = somaImpar + num

        if num == -1:
            totalNImpar = totalNImpar - 1
            somaImpar = somaImpar + 1
            
        if num > maiorNum:
            maiorNum = num

mediaPar = somaPar/totalNPar
mediaImpar = somaImpar/totalNImpar
somaNum = somaNum + 1

print ("O maior número: %d" %maiorNum)
print ("A quantidade de números pares: %d" %totalNPar)
print ("A quantidade de números ímpares: %d" %totalNImpar)
print ("A média dos números pares: %d" %mediaPar)
print ("A média dos números ímpares: %d" %mediaImpar)
print ("A soma total de todos os números lidos: %d" %somaNum)

   

#QUESTÃO 5
popA = 80000
popB =  200000
anos = 0 

taxacA = 3/100
taxacB = 1.5/100

while popA <= popB :
   anos = anos + 1
   popA = taxacA + (popA * taxacA)
   popB = taxacB + (popB * taxacB)
   
print("Número de anos necessários para que a população do país A ultrapasse/iguale a população do país B: %.0f" %anos)


#QUESTÃO 6
mdc = num1
cont = 1

num1 = int (input ("Insira um número: "))
num2 = int (input ("Insira outro número: "))

while (num1 % mdc) !=0 or (num2 % mdc) != 0:
      mdc = mdc -1
      
print ("O máximo divisor comum entre os numeros inseridos é %d: " %mdc)


#QUESTÃO 7
num = int (input ("Insira um número: "))

cont = 1
ante = 0
prox = 1

print(prox)

while cont < num:
    sequencia = ante + prox
    
    print(sequencia)
    ante = prox
    prox = sequencia
    cont = cont + 1


#QUESTÃO 8
soma = 0
cont = 1
continuar =  "S"

while continuar != "N" :
   
   valor = float (input ("Digite o valor do produto ou 0 para finalizar compra: R$ "))
   print ("Produto ",cont,": R$ ", float(valor))
   while valor > 0:
      soma = soma + valor
      cont = cont + 1
      valor = float (input ("Digite o valor do produto ou 0 para finalizar compra: R$ "))
      produto = print ("Produto ",cont,": R$ ", float(valor))

   print("  Lojas Tabajara")
   print ("Total: R$ %.2f" %soma)
   formaPg = float (input ("Dinheiro: R$ "))

   troco = formaPg - soma

   print ("Troco: R$ %.2f" %troco)

   continuar = input ("Registrar próxima compra (S/N)?")


#QUESTÃO 9
codMA =  -1   #MAIS ALTO
alturaMA = -1 

codMB = 9999 #MAIS BAIXO
alturaMB = 9999

codMG = -1    #MAIS GORDO
pesoMG = -1

codMM = 9999  #MAIS MAGRO
pesoMM = 9999

somaA = 0
somaP = 0
cont = 0
finalizar = "S"

while finalizar == "S":
   cod = int (input ("Insira seu código: "))
   altura = float (input ("Insira sua altura: "))
   peso = float (input ("Insira seu peso: "))
 
   if altura > alturaMA : #alto
      alturaMA = altura
      codMA = cod
 
   if altura < alturaMB : #baixo
      alturaMB = altura
      codMB = cod
 
   if peso > pesoMG : #gordo
      pesoMG = peso
      codMG = cod
 
   if peso < pesoMM : #magro
      pesoMM = peso
      codMM = cod   
 
   somaA = somaA + altura
   somaP = somaP + peso
   cont = cont + 1

   finalizar = str (input ("Deseja continuar cadastros (S/N)? "))
   finalizar = finalizar.upper()
 
if cont != 0:
   mediaA = somaA / cont
   mediaP = somaP / cont
   print ("A média dos pesos dos clientes é: %.2f" %mediaP)
   print ("A média das alturas dos clientes é: %.2f" %mediaA)
   print ("O clinete %s é o mais ALTO com %.2f m" %(codMA,alturaMA,))
   print ("O clinete %s é o mais BAIXO com %.2f m" %(codMB,alturaMB,))
   print ("O clinete %s é o mais GORDO com %.2f Kg" %(codMG,pesoMG,))
   print ("O clinete %s é o mais MAGRO com %.2f Kg" %(codMM,pesoMM,))

   
#QUESTÃO 10
#Gabarito
gab01 = "A"
gab02 = "B"
gab03 = "C"
gab04 = "D"
gab05 = "E"
gab06 = "A"
gab07 = "B"
gab08 = "C"
gab09 = "D"
gab10 = "E"
 
nota = int()
acertos = int()
maiorNota = -1
menorNota = 11
proximo = "S"
cont = 1
somaNotas = 0
media = float(0)

while proximo == "S":
    resposta01 = input("Questão 01: ")
    resposta01 = resposta01.upper()
    if resposta01 == gab01:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta02 = input("Questão 02: ")
    resposta02 = resposta02.upper()
    if resposta02 == gab02:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta03 = input("Questão 03: ")
    resposta03 = resposta03.upper()
    if resposta03 == gab03:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta04 = input("Questão 04: ")
    resposta04 = resposta04.upper()
    if resposta04 == gab04:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta05 = input("Questão 05: ")
    resposta05 = resposta05.upper()
    if resposta05 == gab05:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta06 = input("Questão 06: ")
    resposta06 = resposta06.upper()
    if resposta06 == gab06:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta07 = input("Questão 07: ")
    resposta07 = resposta07.upper()
    if resposta07 == gab07:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta08 = input("Questão 08: ")
    resposta08 = resposta08.upper()
    if resposta08 == gab08:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta09 = input("Questão 09: ")
    resposta09 = resposta09.upper()
    if resposta09 == gab09:
        nota = nota + 1
        acertos = acertos + 1
 
    resposta10 = input("Questão 10: ")
    resposta10 = resposta10.upper()
    if resposta10 == gab10:
        nota = nota + 1
        acertos = acertos + 1

    cont = cont + 1
    
    if cont == 1 :
       nota = maiorNota
       nota = menorNota
 
    if nota > maiorNota :
        maiorNota = nota
 
    if nota < menorNota :
        menorNota = nota
 
    print("Total Acertos: %d" %acertos)
    print("Nota Final: %d" %nota)

    somaNotas = somaNotas + nota

    proximo = input("Outro aluno vai usar o sistema (S/N)? ")
    proximo = proximo.upper()
    nota = 0
    acertos = 0
    
media = somaNotas / (cont - 1) 

print ("Maior nota: %d" %maiorNota)
print ("Menor nota: %d" %menorNota)
print ("Total de alunos que utilizaram o sistema: ",(cont-1))
print ("Média das notas da turma: %.2f " %media)



    
   






