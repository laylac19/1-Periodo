#QUESTÃO 1
num1 = int (input ("Insira o primeiro número: "))
num2 = int (input ("Insira o segundo número: "))

if num1 > num2 :
    print("O número %d é o maior." %num1)
else :
    print("O número %d é o maior." %num2)


#QUESTÃO 2
letra = str (input ("Informe o seu sexo com a letra F ou M: "))

if letra == "F" :
    print("F - Feminino")
elif letra == "M" :
    print("M - Masculino")
else :
    print("Sexo Inválido")


#QUESTÃO 3
nota1 = float (input ("Insira sua primeira nota: "))
nota2 = float (input ("Insira sua segunda nota: "))

media = (nota1 + nota2)/2

if media == 10 :
    print ("Aprovado com Distinção.")  
elif media >= 7 and media < 10 :
    print ("Aprovado.")
else :
    print ("Reprovado.")


#QUESTÃO 4
hora = float (input ("Informe a hora atual: "))

if hora >= 0 and hora < 5 :
    print("Vai Dormir.")
    
elif hora >= 5 and hora < 12 :
    print ("Bom Dia.")
    
elif hora >= 12 and hora < 18 :
    print ("Boa Tarde.")

elif hora >= 18 and hora < 24 :
    print ("Boa Noite.")

else :
    print("HORA INVÁLIDA.")


#QUESTÃO 5
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

            #Achar num maior
if num1 > num2 and num1 > num3 :
   print ("O número %d é o maior número." %num1)
elif num2 > num1 and num2 > num3 :
   print ("O número %d é o maior número." %num2)
elif num3 > num1 and num3 > num2 :
   print ("O número %d é o maior número." %num3)

            #Achar num menor
if num1 < num2 and num1 < num3 :
   print ("O número %d é o menor número." %num1)
elif num2 < num1 and num2 < num3 :
   print ("O número %d é o menor número." %num2)
elif num3 < num1 and num3 < num2 :
   print ("O número %d é o menor número." %num3)

            #Ordem decrescente
if num1 > num2 > num3 :
   print ("%d, %d, %d" %(num1, num2, num3))
elif num1 > num3 > num2 :
   print ("%d, %d, %d" %(num1, num3, num2))
elif num2 > num1 > num3 :
   print ("%d, %d, %d" %(num2, num1, num3))
elif num2 > num3 > num1 :
   print ("%d, %d, %d" %(num2, num3, num2))
elif num3 > num1 > num2 :
   print ("%d, %d, %d" %(num3, num1, num2))
elif num3 > num2 > num1 :
   print ("%d, %d, %d" %(num3, num2, num1))
   

#QUESTÃO 6
tipo = str (input ("Tipo de combústivel A: álcool G: gasolina: "))
litro = float (input ("Número de litros vendidos: "))

if tipo == "A" :
   valor = 3.20
   total = litro * valor
  
if tipo == "G" :
   valor = 3.90
   total = litro * valor

      #PREÇO ÁLCOOL
if litro <=20 and tipo == "A" :
   desc = total * (3/100)
   valorF = total - desc
   print ("Total a pagar: R$ %.2f" %valorF)
elif litro > 20 and tipo == "A" : 
   desc = total * (5/100)
   valorF = total - desc
   print ("Total a pagar: R$ %.2f" %valorF)
   
      #PREÇO GASOLINA
if litro <=20 and tipo == "G" :
   desc = total * (4/100)
   valorF = total - desc
   print ("Total a pagar: R$ %.2f" %valorF)
elif litro > 20 and tipo == "G" : 
   desc = total * (6/100)
   valorF = total - desc
   print ("Total a pagar: R$ %.2f" %valorF)


#QUESTÃO 7
import math

m = float (input ("Metros Quadrados da Área a Ser Pintada: "))
precoLata = 80.0
lata = 18

litros = m / 3

if lata < 18 :
   lata = 1
   print ("Qantidade de latas de tinta a serem compradas: %d" %lata)
   print ("Total a pagar: R$ %.2f" %precoLata)

elif litros > 18 :
   latas = litros / 18
   qtde = math.ceil (latas)
   total = qtde * precoLata
   print ("Qantidade de latas de tinta a serem compradas: %d" %qtde)
   print ("Total a pagar: R$ %.2f" %total)


#QUESTÃO 8
nome = str (input ("Nome da giasta: "))
nota1 = float (input ("Nota do jurado 1:"))
nota2 = float (input ("Nota do jurado 2:"))
nota3 = float (input ("Nota do jurado 3:"))
nota4 = float (input ("Nota do jurado 4:"))
nota5 = float (input ("Nota do jurado 5:"))

         #Melhor nota
if nota1 > nota2 and nota1 > nota3 and nota1 > nota4 and nota1 > nota5 :
   maior = nota1
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4 and nota2 > nota5 :
   maior = nota2
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4 and nota3 > nota5 :
   maior = nota3
elif nota4 > nota1 and nota4 > nota2 and nota4 > nota3 and nota4 > nota5 :
   maior = nota4
elif nota5 > nota1 and nota5 > nota2 and nota5 > nota3 and nota5 > nota4 :
   maior = nota5

         #Pior Nota
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4 and nota1 < nota5 :
   menor = nota1
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4 and nota2 < nota5 :
   menor = nota2
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4 and nota3 < nota5 :
   menor = nota3
elif nota4 < nota1 and nota4 < nota2 and nota4 < nota3 and nota4 < nota5 :
   menor = nota4
elif nota5 < nota1 and nota5 < nota2 and nota5 < nota3 and nota5 < nota4 :
   menor = nota5

media = ((nota1 + nota2 + nota3 + nota4 + nota5) - maior - menor)/3

print ("Atleta: %s" %nome)
print ("Média de notas: %.2f" %media)
print ("Maior Nota: %.2f" %maior)
print ("Menor Nota: %.2f" %menor)


#QUESTÃO 9
cod = int (input ("Código do produto: "))
qtde = int (input ("Quantidade do produto: "))

         #preço unitário
if cod >= 1 and cod <= 10 :
   valor = 10
   
elif cod >= 11 and cod <= 20 :
   valor = 15
   
elif cod >= 21 and cod <= 30 :
   valor = 20
   
else :
   valor = 30  
print ("Valor unitário: R$ %.2f" %valor)

         #valor total da nota
total = qtde * valor
print ("Valor Total: R$ %.2f" %total)

         #valor do desconto
if total < 250 :
   desc = total * (5/100)

elif 250 <= total <= 500 :
   desc = total * (10/100)
   
else :
   desc = total * (15/100)  
print ("Valor Desconto: R$ %.2f" %desc)

         #valor final
valorF = total - desc
print ("Valor Total Final: R$ %.2f" %valorF)


#QUESTÃO 10
nome = str (input ("Insira o nome do paciente: "))
idade = int (input ("Insira a idade do paciente: "))
peso = int (input ("Insira a peso do paciente: "))

      #Adultos/Adolescentes
if idade >= 12 and peso >= 60 :
   med = 1000
elif idade >= 12 and peso < 60 :
   med = 875.0
   
      #Crianças/Adolescentes
elif idade < 12 :
   if peso >= 5 and peso <= 9 :
      med = 125
      
   elif peso >= 9.1 and peso <= 16 :
      med = 250
      
   elif peso >= 16.1 and peso <= 24 :
      med = 375
      
   elif peso >= 24.1 and peso <= 30 :
      med = 500
      
   elif peso > 30 :
      med = 750

dose = med / 500 * 20

print ("    RECEITA")
print ("Paciente: %s" %nome)
print ("Quantidade de gotas do medicamento por dose: %.1f" %dose)




