srh = [] #atributos de sarah vida / atk / dfs
csrh = [] #atributos de clone de sarah vida / atk / dfs
chmps = [] #atributos dos personagens sarah, clone sarah
nme= ['Sarah', 'O clone'] #nomes
on = True
k = 0

def rnd_num(x):
    '''Gera um número aletório'''
    global x0
    x0 = x
    xn = (7*x0 + 111)%1024
    print(f'MENSAGEM DEBUG - número gerado: {xn}')
    x0 = xn
    return xn

def soco(chmps):
    sc = chmps[k%2][1] - chmps[(k+1)%2][2]
    a = rnd_num(x0)
    if sc < 0:
        sc = 0
    else:
        sc = sc*(a%3)
    chmps[(k+1)%2][0] -= sc
    return sc

def arremesso_de_facas(chmps):
    armf = 0
    a = rnd_num(x0)
    nglps = a%6
    for i in range(1,nglps+1):
        armf += chmps[k%2][1]//(3**i)
    chmps[(k+1)%2][0] -= armf
    return armf

def invocacao_de_fada(chmps):
    a = rnd_num(x0)
    p = a%100 
    chmps[k%2][0] += p
    q = rnd_num(x0)
    print(f'{nme[k%2]} ganhou {p} pontos de vida!')
    if q%2 != 0 and q < 100:
        chmps[k%2][1] += q
        print(f'{nme[k%2]} ganhou {q} pontos de ataque!')
    elif q%2 == 0 and q < 100 and q != 0:
        chmps[k%2][2] += q   
        print(f'{nme[k%2]} ganhou {q} pontos de defesa!')  
    elif q >=  1019:
        if k%2 == 0:
            print("""O quê? A fada trouxe um monstro gigante com ela!
O Clone e o castelo foram destruídos,
e Sarah agora tem um novo pet.
FINAL SECRETO - PARABENS???""")
        if k%2 != 0:
            print("""O quê? A fada trouxe um monstro gigante com ela!
Sarah foi derrotada...""")
    if q >= 1019:
        return False
    else:
        return True

def vrfy(chmps):
    '''Verifica se a vida de algum personagem é <= 0'''
    if chmps[(k+1)%2][0] <= 0:
        if k%2 == 0:
            print('O clone foi derrotado! Sarah venceu!\nFIM - PARABENS')
        elif k%2 != 0:
            print('Sarah foi derrotada...')
        return False
    else:
        return True

srh = input().split() 
csrh = input().split()
x0 = int(input())

for i in range(3):
    srh[i] = int(srh[i])
chmps.append(srh)

for i in range(3):
    csrh[i] = int(csrh[i])
chmps.append(csrh)

while on:
    hbldd = input()
    if hbldd == 'soco' or hbldd == 'facas':
        if hbldd == 'soco':
            dmg = soco(chmps)
        elif hbldd == 'facas':
            dmg = arremesso_de_facas(chmps)
        print(f'{nme[(k+1)%2]} sofreu {dmg} pontos de dano!')    
        if dmg > 0:
            on = vrfy(chmps)
    elif hbldd == 'fada':
        on = invocacao_de_fada(chmps)
    k += 1