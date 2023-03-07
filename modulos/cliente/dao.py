from flask import Response

from dataBase.connect import ConnectDataBase
from modulos.cliente.modelo import Cliente
from modulos.cliente.sql import SQLCliente


class DaoCliente():

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_clintes(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_BUSCA_NOME.format(SQLCliente._NOME_TABELA,
                                              busca) if busca else SQLCliente._SELECT_ALL

        cursor.execute(sql)
        clientes = []
        columns_name = [desc[0] for desc in cursor.description]
        for cliente in cursor.fetchall():
            data = dict(zip(columns_name, cliente))
            clientes.append(Cliente(**data).get_json())
        return clientes

    def salvar(self, cliente):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SCRIPT_INSERT,
                       (cliente.nome, cliente.endereco, cliente.telefone))
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id

    def get_por_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SELECT_ID, (str(id)))
        cliente = cursor.fetchone()
        if not cliente:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, cliente))
        return Cliente(**data)

    def atualizar(self, cliente):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._UPDATE_BY_ID, (cliente.nome, cliente.endereco, cliente.telefone, cliente.id))
        self.connect.commit()
        return True