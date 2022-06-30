.def N = r16
.def i = r17
.def temp = r18
.def x = r20
.def m = r21

ldi N, 6
ldi x, 10
ldi m, 2

ldi r31, $1
ldi r30, $00

inicio_loop:

st Z+, x
inc x
cpi x, 16

brlo inicio_loop
fim_loop:

ldi r31, $1
ldi r30, $00

ldi i, 0

iloop:

ld temp, Z
add temp, m
inc i
st Z+, temp
cp i, N

brlo iloop
floop:
