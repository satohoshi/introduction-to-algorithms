mtrx = []
nw_mtrx = []

def selecionar(x,y,l_s,a_s):
    nw_mtrx.clear()
    for j in range(y,y + a_s):
        linha = []
        for i in range(x,x + l_s):
            linha.append(mtrx[j][i])
        nw_mtrx.append(linha)
    return True


def recortar(x,y,l_s,a_s,x_cut,y_cut):
    for j in range(y,y + a_s):
        for i in range(x,x + l_s):
            mtrx[j][i] = '000'
    for j in range(y_cut,y_cut + a_s):
        for i in range(x_cut,x_cut + l_s):
            mtrx[j][i] = nw_mtrx[j-y_cut][i-x_cut]


def copiar(x_cpy,y_cpy,l_s,a_s):
    for j in range(y_cpy,y_cpy+ a_s):
        for i in range(x_cpy,x_cpy + l_s):
            mtrx[j][i] = nw_mtrx[j-y_cpy][i-x_cpy]


def rotacionar(x,y,l_s,a_s,lp,ap):
    mtrx_rot = []
    ysup = y + l_s
    xsup = x + a_s
    for i in range(l_s):
        linha = []
        for j in range(a_s-1,-1,-1):
            linha.append(nw_mtrx[j][i])
        mtrx_rot.append(linha)
    if ysup > ap:
        ysup = ap
    if xsup > lp:
        xsup = lp
    for j in range(y, ysup):
        for i in range(x, xsup):
            mtrx[j][i] = mtrx_rot[j-y][i-x]
    if l_s > a_s:
        for j in range(y,y+a_s):
            for i in range(x+a_s,x + l_s):
                mtrx[j][i] = '000'
    elif a_s > l_s:
        for j in range(y + l_s,y + a_s):
            for i in range(x,x + l_s):
                mtrx[j][i] = '000'    


def espelhamento_v(x,y,l_s,a_s):
    mtrx_esph = []
    for j in range(a_s - 1,- 1,-1):
        linha = []
        for i in range(l_s):
            linha.append(nw_mtrx[j][i])
        mtrx_esph.append(linha)
    for j in range(y,y + a_s ):
        for i in range(x,x + l_s):
            mtrx[j][i] = mtrx_esph[j-y][i-x]


def espelhamento_h(x,y,l_s,a_s):
    mtrx_espv = []
    for j in range(a_s):
        linha = []
        for i in range(l_s - 1,- 1,-1):
            linha.append(nw_mtrx[j][i])
        mtrx_espv.append(linha)
    for j in range(y,y + a_s ):
        for i in range(x,x + l_s):
            mtrx[j][i] = mtrx_espv[j-y][i-x]

aux = False
lxa = input().split()
n = int(input())
l = int(lxa[0])
a = int(lxa[1])
for i in range(a):
    linha = input().strip().split()
    mtrx.append(linha)
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'selecao':
        xp = int(cmd[1])
        yp = int(cmd[2])
        l_sp = int(cmd[3])
        a_sp = int(cmd[4])
        aux = selecionar(xp,yp,l_sp,a_sp)
    if not aux:
        nw_mtrx.clear()
        yp = 0
        xp = 0
        l_sp = l
        a_sp = a
        for j in range(a):
            linha = []
            for i in range(l):
                linha.append(mtrx[j][i])
            nw_mtrx.append(linha)
    else:
        selecionar(xp,yp,l_sp,a_sp)
    if cmd[0] == 'recorte':
        x_cutp = int(cmd[1])
        y_cutp = int(cmd[2])
        recortar(xp,yp,l_sp,a_sp,x_cutp,y_cutp)
    elif cmd[0] == 'copia':
        x_cpyp = int(cmd[1])
        y_cpyp = int(cmd[2])
        copiar(x_cpyp,y_cpyp,l_sp,a_sp)
    elif cmd[0] == 'rotacao':
        rotacionar(xp,yp,l_sp,a_sp,l,a)
    elif cmd[0] == 'espelhamento' and cmd[1] == 'v':
        espelhamento_v(xp,yp,l_sp,a_sp)
    elif cmd[0] == 'espelhamento' and cmd[1] == 'h':
        espelhamento_h(xp,yp,l_sp,a_sp)
for j in range(len(mtrx)):
    for i in range(len(mtrx[j])):
        if i != len(mtrx[j])-1:
            print(mtrx[j][i],end=' ')
        else:
            print(mtrx[j][i],end='')
    print()