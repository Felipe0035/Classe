class produto:
    def __init__(self, codproduto, nome, descrição, tamanho,preco):
        self.codproduto = codproduto
        self.nome = nome
        self.descrição = descrição
        self.tamanho = tamanho
        self.preco = preco

    def desconto(self, pagamento):
        valor = pagamento - (0.10 * pagamento)
        print(f"Preço S/desconto: {self.preco} \nPreço C/desconto: {valor}")


produto1 = produto("6354547373882", "Pizza de Mussarela", "Caprichada na mussarela com alho frito","Familia",70.00)
produto2 = produto("6354547578668", "Pizza de Camarão", "Caprichada no camarão"," Familia",130.00)
produto3 = produto("0354548676688", "Pizza de Calabresa", "Caprichada na calabresa"," Familia", 85.00)




print("Código:",produto1.codproduto,"\nNome:",produto1.nome,"\nDescrição:",produto1.descrição,"\nTamanho:",produto1.tamanho,"\nPreço",produto1.preco)

produto1.desconto(produto1.preco)

print("Código:",produto2.codproduto,"\nNome:",produto1.nome,"\nDescrição:",produto2.descrição,"\nTamanho:",produto2.tamanho,"\nPreço",produto2.preco)

produto2.desconto(produto2.preco)

print("Código:",produto3.codproduto,"\nNome:",produto1.nome,"\nDescrição:",produto3.descrição,"\nTamanho:",produto3.tamanho,"\nPreço",produto3.preco)

produto3.desconto(produto3.preco)

