q = int(input())
T = float(input())
C = int(input())
n = int(input())
i = 1
Vp = 0
Vt = 0
m = 0
PAn = 0

while i <= q:
    Vi = T*i + T*C
    Vp += Vi
    Vt += Vi
    print(f'{i} {Vi:.2f} {Vp:.2f}')
    i += 1
print(f'{Vt:.2f}')

while m < (Vt//n):
    m += 1
    PAn += n
    print(PAn)
print(m)
print('BATERIA DE TESTES TERMINADA')