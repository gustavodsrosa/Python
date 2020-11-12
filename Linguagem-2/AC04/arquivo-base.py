from abc import ABC, abstractmethod


class Medico:
    def __init__(self, crm, cpf_medico, rg_medico, nome_medico, telefone_medico, salario):
        self.crm = crm
        self.cpf_medico = cpf_medico
        self.rg_medico = rg_medico
        self.nome_medico = nome_medico
        self.telefone_medico = telefone_medico
        self.salario = salario


class Paciente(Medico):
    def __init__(self, nome_medico, salario, nome, crm, rg, cpf, rg_medico, cpf_medico, endereco, telefone_medico, telefone, data_nasc):
        super().__init__(crm, cpf_medico, rg_medico, nome_medico, telefone_medico, salario)
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.data_nasc = data_nasc


class Especialidade(Medico):
    def __init__(self, crm, cpf_medico, rg_medico, nome_medico, telefone_medico, salario, especialidade):
        super().__init__(crm, cpf_medico, rg_medico, nome_medico, telefone_medico, salario)
        self.especialidade = especialidade


class Quarto(Paciente):
    def __init__(self, nome, rg, cpf, endereco, telefone, data_nasc, numero, andar, rg_medico, cpf_medico, telefone_medico):
        super().__init__(nome, rg, cpf, endereco, telefone, data_nasc, rg_medico, cpf_medico, telefone_medico, data_nasc)
        self.numero = numero
        self.andar = andar


class Observacoes(ABC):
    @abstractmethod
    def observacao_paciente(self): 
        pass


class Historico(Medico):
    def __init__(self, crm, cpf_medico, rg_medico, nome_medico, telefone_medico, salario, data, horario):
        super().__init__(nome_medico, crm, cpf_medico, rg_medico, telefone_medico, salario)
        self.data = data
        self.horario = horario
    
    def observacao_paciente(self):
        self.observacao_paciente = ''


medico = Medico(123321, 999999999, 111222333, 'Jairo Monteiro', '(11)999888', 2000)
paciente = Paciente('Josias', 3000, 'Luís Otávio', 1222, 101414, 12321232, 1454785, 23333, 'Rua Olavo', '(11)99887766', '(11)14789632', '20/12/1900')
especialidade = Especialidade(1221213, 88778877, 123, 'Fernando', '(11)88787', 2000, 'Terapeuta')
quarto = Quarto('Jonas', 2000, 'Gustavo', 789, 87456923, 1478523, 412547858, 7896541, 'Av. Dois', '(11)745874587', '(11)123456789')
historico = Historico(145451, 745896587, 145478547, 'Jailson', '(11)14754787', 3500, '20/10/2036', '23:00')
historico.observacao_paciente('Paciente em alta')