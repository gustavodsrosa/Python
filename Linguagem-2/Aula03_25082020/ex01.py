'''
Preencha um dicionário com informações de 5 produtos.
Utilize o nome do produto como chave e o preço 
como valor.
Percorra o dicionário e exiba o nome dos produtos 
com preço superior a R$ 50.00
'''

# Preço tabelado
produtos = {
    'Café': 5.00,
    'Requeijão': 8.90,
    'Cesta Básica': 58.99,
    'Panela de pressão': 108.00,
    'Liquidificador': 60.00
}

lista = []
for i in produtos:
    if produtos[i] > 50:
        lista.append(i)
print(lista)



        
