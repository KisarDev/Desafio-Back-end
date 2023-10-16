import datetime


class OrdemProducao:
    def __init__(self, produto, quantidade, data_entrega):
        self.produto = produto
        self.quantidade = quantidade
        self.data_entrega = data_entrega
        self.status = "Em andamento"
        self.data_conclusao = None

    def concluir(self):
        self.status = "Concluída"
        self.data_conclusao = datetime.now()
