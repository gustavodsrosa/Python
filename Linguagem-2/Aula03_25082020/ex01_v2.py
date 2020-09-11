'''
Preencha um dicionário com informações de 5 produtos.
Utilize o nome do produto como chave e o preço 
como valor.
Percorra o dicionário e exiba o nome dos produtos 
com preço superior a R$ 50.00
'''

# Cliente insere o preço
cliente = {}

for x in range(5):
    nome = input('Qual produto: ')
    valor = float(input('Qual o preço do produto: '))
    cliente[nome] = valor

armazenaDados = []
for k in cliente:
    if cliente[k] > 50:
        armazenaDados.append(k)
print(armazenaDados)