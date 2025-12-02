count = {}
animal = {}
zoo = {}
use = {}
lst_dna = []
ftr_lst = []
prt_lst = []
n = int(input())
for i in range(n):
    ftrs = []
    animal_in = input().split()
    for x in animal_in[4:]:
        ftrs.append(x)
    animal['id'] = int(animal_in[0])
    animal['nome_cnt'] = animal_in[2]
    animal['ftrs'] = ftrs
    zoo[animal_in[1]] = animal.copy()
ndna = int(input())
for i in range(ndna):
    ftr = input()
    l1 = input()
    l2 = input()
    dna = []
    for j in range(len(l1)):
        dna.append(l1[j]+l2[j])
    ftr_lst.append(ftr)
    lst_dna.append(dna)
for i in range(ndna):
    c = 0
    for j in range(len(l1)):
        if lst_dna[i][j] > lst_dna[0][j]:
            c +=1   
    count[c] = i
a = sorted(count)
for i in range(len(sorted(count))-1,-1,-1):
    chrc = []
    for x in zoo.keys():
        if ftr_lst[count[a[i]]] in zoo[x]['ftrs'] and x not in use:
            use[x] = ftr_lst[count[a[i]]]
            chrc.append(x)
    prt_lst.append(chrc)
c = len(prt_lst)-1
for i in sorted(count):
    print(f'CARACTERÍSTICA: {ftr_lst[count[i]]}')
    for x in prt_lst[c]:
        print(zoo[x]['id'],end=' ')
        print(x,end=' ')
        print(zoo[x]['nome_cnt'])
    c -=  1