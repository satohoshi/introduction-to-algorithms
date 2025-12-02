from decimal import getcontext, Decimal
from recipes_decimal import pi

PI = pi()
ERRO = Decimal(10**-32)
getcontext().prec = 36

def zeta(s):
    '''Funcao Zeta'''
    soma = 0
    for i in range(1,101):
        soma += (Decimal(1)/Decimal(i))**(s)
    return soma


def y(x,a,b,c,d):
    '''Funcao que calcula a distancia em funcao do combustivel'''
    y = ((PI + a * (Decimal(x).exp()) - Decimal(zeta(b*x + PI)))/(Decimal(-Decimal(c * x).sqrt()).exp() + d * (Decimal(2) * (PI ** Decimal(3)) - x)))
    return y


def busca(dist,a,b,c,d):
    '''Faz a busca binaria'''
    e = 0
    d2 = 50
    while Decimal(abs(e-d2)) >= ERRO:
        m = Decimal((e + d2) / 2)
        y_ = Decimal(y(m,a,b,c,d))
        if abs(y_ - dist) < ERRO:
            return m 
        if y_ < dist:
            e = m
        elif y_ > dist:
            d2 = m
    return m


def main():
    '''Execucao principal'''
    resp = {}
    n = int(input())
    while n != 0:
        grau = True
        conjunto = {}
        parametros = [] # a,b,c,d
        for i in range(n):
            plnt = input()
            dist = Decimal(input())
            conjunto[dist] = plnt
        for i in range(4):
            parametros.append(Decimal(input()))
        max_dist = y(Decimal(50),parametros[0],parametros[1],parametros[2],parametros[3])
        for j in sorted(conjunto, reverse=True):
            if j <= max_dist:
                ind = busca(Decimal(j),parametros[0],parametros[1],parametros[2],parametros[3])
                grau = False
                resp[conjunto[j]] = ind
                break
        if grau == True:
            resp[conjunto[j]] = 'GRAU~~'
        n = int(input())
        
    for j in resp:
        if resp[j] == 'GRAU~~':
            print('GRAU~~')
        else:
            print(j)
            comb = resp[j]
            print(f'{comb:.28f}')

if __name__ == "__main__":
    main()