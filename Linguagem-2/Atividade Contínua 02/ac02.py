def salario(lista):

    salario_base = lista[2]
    cargo = lista[3]
    try:
        if cargo == "DESENVOLVEDOR":
            if salario_base >= 3000:
                sal_liq = salario_base - (salario_base*0.2)
                return sal_liq
            else:
                sal_liq = salario_base - (salario_base*0.10)
                return sal_liq
        elif cargo == "ANALISTA":
            if salario_base >= 2000:
                sal_liq = salario_base - (salario_base * 0.25)
                return sal_liq
            else:
                sal_liq = salario_base - (salario_base*0.15)
                return sal_liq
        elif cargo == "GERENTE":
            if salario_base >= 5000:
                sal_liq = salario_base - (salario_base*0.30)
                return sal_liq
            else:
                sal_liq = (salario_base) - (salario_base*0.20)
                return sal_liq
        elif cargo != 'DESENVOLVEDOR' and 'cargo' != 'ANALISTA' and cargo != 'GERENTE':
            raise UnboundLocalError
    except UnboundLocalError:
        return 'Cargo não existe!!'
    except Exception:
        return 'Algo deu Errado.'