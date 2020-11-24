'''
1 - Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem
que diga se ela poderá ou não votar este ano (não é necessário considerar o
mês em que a pessoa nasceu).'''

ano_atual = 2020

ano_nasc = int(input("Em que ano você nasceu? "))

dif_ano = ano_atual - ano_nasc

if dif_ano > 17 and dif_ano < 70:
    print(f"Você tem {dif_ano} anos. Seu voto é obrigatório")
else:
    print(f"Você tem {dif_ano} anos. Seu voto é facultativo")

