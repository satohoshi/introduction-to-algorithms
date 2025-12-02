lista = []
res = []
i = 0
k = 0
n = input()
lista = n.split()
while lista[i] != '0':
    a = int(lista[i+1])
    b = int(lista[i + 2])
    res.append('')
    if lista[i] == '+':
        res[k] = a + b
    elif lista[i] == '-':
        res[k] = a - b
    elif lista[i] == '*':
        res[k] = a * b
    elif lista[i] == '/':
        res[k] = str(a//b) + ' ' + str(a%b)
    elif lista[i] == ';':
        if (a-b) == 0:
            res[k] = 0
        else:
            for c in range(1,abs(a-b)+1):
                if c == abs(a-b):
                    res[k] += str(c)
                elif (a-b)%c == 0:
                    res[k] += str(c) + ' '
    k += 1
    n = input()
    lista += n.split()
    i += 3
k = 0
while k < len(res):
    print(res[k])
    k += 1  