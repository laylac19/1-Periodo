ldi r17, 5
ldi r18, 3

mov r19, r17
add r19, r18

ldi r20, 30

cp r19, r20
brsh x
mov r25, r19
jump : y
x :
mov r26, r19