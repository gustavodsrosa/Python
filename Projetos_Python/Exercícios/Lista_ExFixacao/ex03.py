'''
3 - Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o
preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o
desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
- Se quantidade <= 5 o desconto será de 2%
- Se quantidade >; 5 e quantidade <=10 o desconto será de 3%
- Se quantidade > 10 o desconto será de 5%
Dica: utilize if / else if / else
'''

descricao = str(input("Descrição do produto: "))
qtd = int(input("Quantidade adquirida: "))
pr_unitario = float(input("Prço unitário: "))
total = 0
desconto = 0
total_a_pagar = 0


if qtd <= 5:
    desconto = 0.02
    total = qtd * pr_unitario
    total_a_pagar = total - desconto
    print("Total a pagar: ", total_a_pagar)
elif qtd > 5 and qtd <= 10:
    desconto = 0.03
    total = qtd * pr_unitario
    total_a_pagar = total - desconto
    print("Total a pagar: ", total_a_pagar)
else:
    desconto = 0.05
    total = qtd * pr_unitario
    total_a_pagar = total - desconto
    print("Total a pagar: ", total_a_pagar)

    

