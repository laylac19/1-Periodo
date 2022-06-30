.def x = r20

ldi x, 1

ldi r31, $1
ldi r30, $00
inicio_loop:
st Z+, x
inc x
cpi x, 11
brlo inicio_loop
fim_loop: