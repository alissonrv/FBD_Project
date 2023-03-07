class Cliente(object):
    def __init__(self, nome, endereco, telefone, id=None):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - Nome: {self.nome} - Endereco{self.endereco} - Telefone{self.telefone}'

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone,
        }

    def get_sql_insert(self):
        return
