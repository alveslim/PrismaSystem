class OrdemProducao:
    def __init__(self, data_in, data_out, cliente, firma, op, referencia, ft, desenhista, status):
        self.data_entrada = data_in
        self.data_entrega = data_out
        self.cliente = cliente
        self.firma = firma
        self.op = op
        self.referencia = referencia
        self.ft = ft
        self.desenhista = desenhista
        self.status = status
        
    def for_list_csv(self):
        """Unify the data in format of list for csv"""
        return[self.firma, self.op, self.referencia, self.ft, self.desenhista, self.status]
    
    def for_dict(self):
        """Unify the data in dictionary for generator of text/pdf"""
        return {
            "data_entrada": self.data_entrada,
            "data_entrega": self.data_entrega,
            "cliente": self.cliente,
            "firma": self.firma,
            "op": self.op,
            "referencia": self.referencia,
            "ft": self.ft,
            "desenehista": self.desenhista,
            "status": self.status
        }