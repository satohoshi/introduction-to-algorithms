
id = int(input())
x = str('')
rband = str()
rfoto = str()
if id >= 0 and id < 25:
    tvideo = int(input())
    print('*Que página de meme do Instagram você é?*')
    print('Qual a sua idade?')
    print(id)
    if tvideo >= 0 and tvideo <= 5:
        print('Quantos segundos são necessários para saber se um vídeo é bom?')
        print(tvideo)
        print('RESULTADO')
        print('Você deveria estar no TikTok')
    elif tvideo < 0:
        print('Quantos segundos são necessários para saber se um vídeo é bom?')
        print(tvideo)
        print("Erro: entrada inválida")
    else:        
        print('Quantos segundos são necessários para saber se um vídeo é bom?')
        print(tvideo)
        x = "@meltmemes"
elif id >= 25 and id <= 40:
    band = input()
    if band == 'A' or band == 'B':
        if band == 'A':
            rband = 'A) Matanza'
        else: 
            rband = 'B) Iron Maiden'
        x = "@badrockistamemes"
        print('*Que página de meme do Instagram você é?*')
        print('Qual a sua idade?')
        print(id)
        print('Qual banda você gosta mais?')
        print(rband)
    elif band == 'C' or band == 'D':
        if band == 'C':
            rband = 'C) Imagine Dragons'
        else:
            rband = 'D) BlackPink'
        rc = input()
        if rc == 'Não' or rc == 'Sim':
            if rc == 'Não':
                x = "@wrongchoicememes"
            elif rc == 'Sim':
                x = "@genteboamemes"
            print('*Que página de meme do Instagram você é?*')
            print('Qual a sua idade?')
            print(id)
            print('Qual banda você gosta mais?')
            print(rband)
            print("São as capivaras os melhores animais da Terra?")
            print(rc)
        else:
            print('*Que página de meme do Instagram você é?*')
            print('Qual a sua idade?')
            print(id)
            print('Qual banda você gosta mais?')
            print(rband)
            print("São as capivaras os melhores animais da Terra?")
            print(rc)
            print("Erro: entrada inválida")
    else:
        print('*Que página de meme do Instagram você é?*')
        print('Qual a sua idade?')
        print(id)
        print('Qual banda você gosta mais?')
        print(band)
        print("Erro: entrada inválida")

elif id > 40 and id <= 125:
    foto = input()
    if foto == 'A' or foto == 'B' or foto == 'C':
        if foto == 'A':
            rfoto = 'A) Bebê em roupa de flor'
            x = "@bomdiabebe"
        elif foto == 'B':
            rfoto = 'B) Gato'
            x = "@kittykatmsgs"
        elif foto == 'C':
            rfoto = 'C) Coração e rosas'
            x = "@bomdiaflordodia"
        print('*Que página de meme do Instagram você é?*')
        print('Qual a sua idade?')
        print(id)
        print("Que imagem de bom dia você manda no grupo da família?")
        print(rfoto)
    else:   
        print('*Que página de meme do Instagram você é?*')
        print('Qual a sua idade?')
        print(id)
        print("Que imagem de bom dia você manda no grupo da família?")
        print(foto)
        print("Erro: entrada inválida")
else:
    print('*Que página de meme do Instagram você é?*')
    print('Qual a sua idade?')
    print(id)
    print("Erro: entrada inválida")

if x != '':
    print('RESULTADO')
    print(f'Sua página de memes é: {x}')