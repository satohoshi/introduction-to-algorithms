#con_salas - salas conectadas a sala em questao
#item_sala - item atribuido a sala
# it - recebe o input de sala + item
# it_aux - lista com todos os input sala + item
# sala - objeto sala
# num itens - qnt de itens no game
# seq_sala - sequencia de salas a serem seguidas
# qnt itens - tamanho do inventario

class Salas:
    '''Define as salas relacionadas e o tem contido em uma sala'''
    def __init__(self, con_salas, item_sala = None):
        '''Define os atributos'''
        self._con_salas = con_salas
        self._item_sala = item_sala
    
    @property
    def con_salas(self):
        '''metodo pra acessar e retornar o atributo _con_salas'''
        return self._con_salas

    @property
    def item_sala(self):
        '''metodo pra acessar e retornar o atributo _item_sala'''
        return self._item_sala
    
    @item_sala.setter
    def item_sala(self, item_sala):
        '''metodo pra modificar o atributo _item_sala'''
        self._item_sala = item_sala

class Mapa:
    '''Define as salas do bot e do clone'''
    def __init__(self, sala_clone, sala_bot):
        self._sala_clone = sala_clone
        self._sala_bot = sala_bot
   
    @property
    def sala_clone(self):
        '''metodo pra acessar e retornar o atributo _sala_clone'''
        return self._sala_clone

    @property
    def sala_bot(self):
        '''metodo pra acessar e retornar o atributo _sala_bot'''
        return self._sala_bot

    @sala_bot.setter
    def sala_bot(self, sala_bot):
        '''metodo pra modificar o atributo _sala_bot'''
        self._sala_bot = sala_bot

class Bot:
    def __init__(self,invent = []):
        '''define o inventario''' 
        self._invent = invent

    @property
    def invent(self):
        '''metodo pra acessar e retornar o atributo _invent'''
        return self._invent

    @invent.setter
    def invent(self, invent):
        '''metodo pra modificar o atributo _invent'''
        self._invent = invent

    def add(self,a):
        '''metodo pra adicionar um item no inventário'''
        self._invent.append(a)


sala = []
it_aux = []
a = True
cont = 0
bot = Bot()

num_sala = int(input())
for i in range (num_sala):
    sl = input().split()
    for j in range(5):
        sl[j] = int(sl[j])
    sala.append(Salas(sl[1:]))

num_itens = int(input())
for i in range (num_itens):
    it = input().split()
    it[0] = int(it[0])
    it_aux.append(it)

map = Mapa(sala_clone = int(input()),sala_bot = int(input()))
qnt_itens = int(input())
seq_sala = input().split()
for i in range (len(seq_sala)):
    seq_sala[i] = int(seq_sala[i])

for i in range(num_sala):
    for j in range(num_itens):
        if i == it_aux[j][0]:
            sala[i].item_sala = it_aux[j][1]

print("""Bem-vindo as Aventuras de Sarah 2.0
Sarah acorda no saguão do antigo castelo de sua família,ela tem a oportunidade única de derrotar o seu clone maligno que se apoderou do reino.
Para isso ela deve encontrar o baú da sua família que contém a espada mágica que apenas a verdadeira herdeira pode utilizar.
Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?""")
print(f"DEBUG - O clone está na sala: {map.sala_clone}")
while a and cont <= len(seq_sala):
    if sala[map.sala_bot].item_sala != None:
        print(f"Você está na sala de número {map.sala_bot} ela contém um baú com {sala[map.sala_bot].item_sala} e dela você pode ir para as salas {sala[map.sala_bot].con_salas}")
        print(f"Pegar {sala[map.sala_bot].item_sala}")
        if len(bot.invent) < qnt_itens:
            print(f"{sala[map.sala_bot].item_sala} adicionado ao inventário")
            bot.add(sala[map.sala_bot].item_sala)
            if sala[map.sala_bot].item_sala == "poção":
                print("Você pegou a poção da morte e virou pó instantaneamente. Tente novamente...")
                a = False
            sala[map.sala_bot].item_sala = None
        else:
            print("Inventário cheio!")
    else:
        print(f"Você está na sala de número {map.sala_bot} e dela você pode ir para as salas {sala[map.sala_bot].con_salas}")
    print(f"Mover para sala {seq_sala[cont]}")
    map.sala_bot = seq_sala[cont]
    if map.sala_bot == map.sala_clone:
        if "espada" in bot.invent:
            print("Você derrotou o clone maligno com a espada mágica! Com a Sarah no reino o mundo pode voltar ao equilíbrio.\nPARABÉNS!")
        else:
            print("Infelizmente você encontrou o clone sem a espada das fadas e foi derrotado. Tente novamente...")
        a = False
    cont += 1