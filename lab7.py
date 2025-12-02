if __name__ == "__main__":
    lista_p = ['HA','CR','CC']
    lista_org = [[],[],[]]
    lista_aux = []

    def consecutivos():
        '''Devolve o item que mais se repetiu e qnts vezes se repetiu'''
        ele_rept = ''
        qnt_consec = 1
        qnt_consec_aux = 0
        for i in range(len(lista)-1):
            if lista[i] == lista[i+1]:
                qnt_consec += 1
            else:
                qnt_consec = 1
            if qnt_consec > qnt_consec_aux:
                qnt_consec_aux = qnt_consec
                ele_rept = lista[i]
        return ele_rept + ' ' + str(qnt_consec_aux)

    def unicos():
        '''Calcula a quantidade de itens unicos e gera um lista com itens unicos'''
        cont = 0
        for x in lista[:len(lista)-1]:
            if x not in lista_aux:
                lista_aux.append(x)
                cont += 1
        return cont

    def remover(rmv):
        while rmv in lista_aux:
            lista_aux.remove(rmv)

    def ajuste():
        for i in range(len(lista_aux)):
            lista_aux[i] = lista_aux[i].replace(' ','-')
        for i in range(len(lista_aux)):
            lista_aux[i] = lista_aux[i][:3] + lista_aux[i][3:].lower()

    def organizar():
        for x in lista_aux:
            for j in range(3):
                if x[:2] == lista_p[j]:
                    lista_org[j].append(x)
        for j in range(3):
            print(lista_org[j])

    lista = input().split(', ')
    ult = lista.pop()
    lista += ult.split("/ ")
    print(consecutivos())
    print(unicos())
    remover(lista[len(lista)-1])
    ajuste()
    organizar()