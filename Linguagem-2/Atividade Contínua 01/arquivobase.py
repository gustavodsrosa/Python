def analista(novosalario):
    if salariobase >= 2000:
        novosalario = salariobase * 0.75
    else:
        novosalario = salariobase * 0.85
    return novosalario

def desenvolvedor(novosalario):
    if salariobase >= 3000:
        novosalario = salariobase * 0.8
    else:
        novosalario = salariobase * 0.9
    return novosalario

def gerente(novosalario):
    if salariobase >= 5000:
        novosalario = salariobase * 0.7
    else:
        novosalario = salariobase * 0.8
    return novosalario

lista = []

# nome, e-mail, salário base, cargo
nome = input('Nome: ')
lista.append(nome)
email = input('E-mail: ')
lista.append(email)
salariobase = float(input('Salário-base: '))
lista.append(salariobase)
cargo = str(input('Cargo: '))
lista.append(cargo)

# cargo.analista(salariobase)

def escolha():
    if lista[3] == 'DESENVOLVEDOR':
        desenvolvedor(salariobase)
    elif lista[3] == 'ANALISTA':
        analista(salariobase)
    elif lista[3] == 'GERENTE':
        gerente(salariobase)





