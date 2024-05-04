class Funcionario:
    def __init__(self,matricula, nome, telefone, email, cpf,rg):
        self.matricula = matricula
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.rg = rg

class Medico(Funcionario):
    def __init__(self,matricula, nome, telefone, email, cpf,rg,crm):
        super().__init__(matricula, nome, telefone, email , cpf,rg )
        self.crm = crm

    def especialidade(self,mensagem):
        print(f"{self.nome} especialidade:{mensagem}")



class Enfermeiro( Funcionario):
    def __init__(self,matricula, nome, telefone ,email , cpf , rg , coren):
        super().__init__(matricula, nome, telefone,email , cpf , rg )
        self.coren=coren

    

medico1 = Medico("1","DR lucas","99999999","medicos@gmail.com","1234567898","00000000","1111")
medico2 = Medico("2","DRa Luana","8888888","medicos@gmail.com","1234567898","00000000","2223")
enfemeiro1 = Enfermeiro("1","\nEnfermeira Veronica","33333333","enfermeira@gmail.com","123456789","55555555","123")
enfemeiro1 = Enfermeiro("2","\nEnfermeiro Euclefaciolistopode","44444444","enfermeira@gmail.com","123456789","6666666","456")
medico1.especialidade("\nNutricionista horario  \nAtendimento segunda e quinta das 14 as 18hs. ")
medico2.especialidade("\npsicologa horario \nAtendimento terça,sexta de 9 as 13hs.")