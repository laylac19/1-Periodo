.def N = r16
.def i = r17
.def temp = r18
.def temp2 = r19

ldi N, 5

ldi r31, $1
ldi r30, $00

ldi temp, 13
sts $100, temp
ldi temp, 10
sts $101, temp
ldi temp, 8
sts $102, temp
ldi temp, 7
sts $103, temp
ldi temp, 2
sts $104, temp

clr temp
clr temp2
ldi i, 0
inicio_loop:
ld temp2, Z+
add temp, temp2
inc i
cp i, N
brlo inicio_loop
fim_loop:

st Z, temp