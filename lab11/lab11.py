qnt_pr = 0
cliques = 0
max_qtdLeitores = 0
max_qtdLeitores_final = 0
max_tempo = 0
cliques_tot = 0
ltr_tot = 0
med_qtdLeitores = 0
med_cliques = 0
med_qntpr = 0
ti_max_qtdLeitores = ""
ti_max_qtdLeitores_final = ""
lst_arq = []
n = int(input())
for i in range(n):
    nome_arq = input()
    lst_arq.append(nome_arq)

for x in lst_arq:
    info_arq = []
    s = ""
    with open(x, 'r') as arq:
        for linha in arq:
            a = linha.rstrip().split(':')
            if len(a) == 2:
                info_arq.append(a[1].strip())
            elif len(a) > 2:
                for i in range(1,len(a)):
                    if i == 1:
                        s += a[i]
                    else:
                        s += ":" + a[i]
                info_arq.append(s.strip())
            else:
                info_arq.append(a[0].strip())
    nome = "relatorio_" + info_arq[0] + ".txt"

    with open(nome, 'x') as arqn:
        arqn.write("nId: " + info_arq[0] + "\n")
        arqn.write("qtdLeitores: " + info_arq[2] + "\n")
        arqn.write("qtdLeitoresFinal: " + info_arq[3] + "\n")
        arqn.write("qtdCliques: " + info_arq[4] + "\n")
        arqn.write("tempo: " + info_arq[5])

    qtdLeitores = int(info_arq[2])
    titulo = info_arq[1]
    qtdLeitores_final = int(info_arq[3])
    cliques = int(info_arq[4])
    tempo = int(info_arq[5])
    ltr_tot += qtdLeitores
    cliques_tot += cliques
    qnt_pr += len(info_arq) - 6 #num de paragrafos

    if qtdLeitores > max_qtdLeitores:
        max_qtdLeitores = qtdLeitores
        ti_max_qtdLeitores = titulo

    if qtdLeitores_final > max_qtdLeitores_final:
        max_qtdLeitores_final = qtdLeitores_final
        ti_max_qtdLeitores_final = titulo

    if tempo > max_tempo:
        max_tempo = tempo

with open("relatorio_final.txt", 'w+') as relf:
    med_qtdLeitores = int(ltr_tot/n)
    med_cliques = int(cliques_tot/n)
    med_qntpr = int(qnt_pr/n)
    relf.write(str(med_qtdLeitores) + "\n")
    relf.write('"' + ti_max_qtdLeitores + '"' + ' ' + str(max_qtdLeitores) + "\n")
    relf.write('"' + ti_max_qtdLeitores_final + '"' + ' ' + str(max_qtdLeitores_final) + "\n")
    relf.write(str(med_cliques) + "\n")
    relf.write(str(max_tempo) + "\n")
    relf.write(str(med_qntpr))