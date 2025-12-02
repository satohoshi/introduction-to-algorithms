estoque = {}
prd = {}
stq = []
categorias = []
reposicao = []
saldo = 0


def estoque_ins(q):
    prd['qnt'] = q
    prd['categoria'] = produto[3]
    prd['preco'] = float(produto[4])
    prd['validade'] = produto[5]
    estoque[produto[1]] = prd.copy()
    if produto[3] not in categorias:
        categorias.append(produto[3])


def estoque_rmv(q):
    if produto[1] not in estoque or q > estoque[produto[1]]['qnt']:
        print('ERROR')
    elif q <= estoque[produto[1]]['qnt']:
        estoque[produto[1]]['qnt'] -= q
        print('SUCCESS')

    
def caixa(q,s):
    estoque[produto[0]]['qnt'] -= q
    s += q*estoque[produto[0]]['preco']
    return s


def encerrar(s):
    c = 0
    print('* ESTOQUE')
    for a in estoque:
        if estoque[a]['qnt'] == 0:
            reposicao.append(a)
            c += 1
    if c != len(estoque):
        for x in sorted(categorias):
            aux = 0
            for y in sorted(estoque):
                if estoque[y]['categoria'] == x and not estoque[y]['qnt'] == 0:
                    if  aux == 0:
                        print(f'- {x}')
                        aux += 1
                    c = estoque[y]['qnt']
                    print(f'{y} {c}')
    print(f'* SALDO {s:.2f}')
    if len(reposicao) > 0:
        print('* REPOSICAO')
        for x in reposicao:
            print(x)


def promocao(data):
    promocao = []
    d_dflt = int(data[0:2])
    m_dflt = int(data[2:4])
    a_dflt = int(data[4:])
    for x in sorted(estoque):
        d_p = int(estoque[x]['validade'][0:2])
        m_p = int(estoque[x]['validade'][2:4])
        a_p = int(estoque[x]['validade'][4:])
        if estoque[x]['qnt'] != 0:
            if (d_dflt+7)//32 == 1 and m_dflt != 2:
                m_dflt += 1
                nd_dflt = (d_dflt+7)%31
                if m_dflt//13 == 1:
                    a_dflt += 1
                if (nd_dflt >= d_p and m_dflt == m_p and a_dflt == a_p) or (d_dflt < d_p and m_dflt > m_p and a_dflt >= a_p):
                    promocao.append(x)
            elif (d_dflt+7)//29 == 1 and m_dflt == 2:
                m_dflt += 1
                nd_dflt = (d_dflt+7)%28
                if m_dflt//13 == 1:
                    a_dflt += 1 
                if (nd_dflt >= d_p and m_dflt == m_p and a_dflt == a_p) or (d_dflt < d_p and m_dflt > m_p and a_dflt >= a_p):
                    promocao.append(x)
            elif d_dflt+7 >= d_p and m_dflt == m_p and a_dflt == a_p:
                promocao.append(x)
            d_dflt = int(data[0:2])
            m_dflt = int(data[2:4])
            a_dflt = int(data[4:])
    if len(promocao) > 0:
        print('* PROMOCAO')
        for x in promocao:
            print(x)


mode = int(input())
while mode != 0:
    n = int(input()) 
    if mode == 1:
        for i in range(n):
            produto = input().split()
            produto[0] = int(produto[0])
            qnt = int(produto[2])
            if produto[0] == 0:
                estoque_ins(qnt)
            if produto[0] == 1:
                estoque_rmv(qnt)
    elif mode == 2:
        for i in range(n):
            produto = input().split()
            qnt = int(produto[1])
            saldo = caixa(qnt,saldo)
    mode = int(input())
d = input()
encerrar(saldo)
promocao(d)