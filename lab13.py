pastas = {}

def imprimir(key,texto):
    '''devolve as linhas de texto a serem impressas recursivamente'''
    if key in pastas:
        return imprimir(pastas[key],texto)  + "_" + key
    else:
        return texto


a = input().split()
for i in range(int(a[1])):
    txt = input().split()
    pastas[txt[0]] = txt[1]
    print(imprimir(txt[0],a[0]))