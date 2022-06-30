%Multiplicar um número por 5 e salvar o valor no registrador R20. Coloque um valor pequeno na entrada, máximo 15 para evitar overflow.
%Não vale utilizar nesta atividade a instrução de multiplicação. E você deverá utilizar um loop de repetição.

.def x = r19
.def r = r20

ldi x, 1

ldi r17, 4 
ldi r18, 5 

inicio_loop:
inc x

add r21, r17

cpi x, 6
brlo inicio_loop

fim_loop:

mov r20, r21

