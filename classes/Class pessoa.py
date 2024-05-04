class Pessoa:
    def __init__(self ,nome, data_nascimento, sexo ):
            self.nome = nome
            self.data_nascimento = data_nascimento
            self.sexo = sexo

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

class aluno(Pessoa):
     def __init__(self, nome, data_nascimento, sexo, matricula):
          super().__init__(nome, data_nascimento, sexo)
          self.matricula = matricula


pessoa1 = Pessoa("José", "20/10/1995", "Masculino")
pessoa2 = Pessoa("Maria", "15/01/2001", "Feminino")

aluno1 = aluno("José boi", "20/10/1995", "Masculino", "28376465")
aluno2 = aluno("Maria Corna","15/01/2001", "Feminino","836454743")
    
print("Nome:",pessoa1.nome,"Data de nascimento:",pessoa1.data_nascimento,"Sexo:",pessoa1.sexo)
print("Nome:",pessoa2.nome,"Data de nascimento:",pessoa2.data_nascimento,"Sexo:",pessoa2.sexo)


pessoa1.falar("Eu sou um...")
pessoa2.falar("Desgraçado") 












