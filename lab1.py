fds = ['sábado','domingo']
dias = ['terça-feira','quarta-feira','quinta-feira','sexta-feira']
dia = int(input())
dia_sem = str(input()).strip().lower() 
vlr_c = float(input())

if dia%7 == 0:
    vlr_p = vlr_c*0.5
else: 
    if dia_sem == 'sexta-feira':
        vlr_p = vlr_c*0.75
    else:
        vlr_p = vlr_c - dia
        if vlr_p < 0:
            vlr_p = 0

print(f'{vlr_p:.2f}')
if dia_sem in dias:
    print(f'Agradecemos a preferência, tenha uma ótima {dia_sem}!')
elif dia_sem in fds:
    print(f'Agradecemos a preferência, tenha um ótimo fim de semana!')
else:
    print(f'É um dia terrível, você não devia ter saído da cama.')
