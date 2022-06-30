%Somar dois números, caso a soma dê mais de 35, somar 10, caso contrário, adicionar o valor atual da soma (isso equivale a multiplicar a soma atual por 2). 
%Salvar o resultado no R20.

ldi r21, 10
ldi r21, 2

ldi r17, 10
ldi r18, 5

mov r19, r17
add r19, r18

ldi r16, 35

cp r19, r16

brsh x

add r19, r19
mov r20, r19

jmp y

x:
mul r19, r22
mov r20, r19

y: 