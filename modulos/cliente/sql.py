class SQLCliente:
    _NOME_TABELA = 'cliente'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}(' \
                           f'id serial primary key,' \
                           f'nome varchar(100),' \
                           f'endereco varchar(100),' \
                           f'telefone varchar(50))'

    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(nome, endereco, telefone) ' \
                    f'values(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'
    _SELECT_BUSCA_NOME = "SELECT * FROM {} where nome ILIKE '%{}%'"

    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET nome=%s, endereco=%s, telefone=%s ' \
                    f'WHERE id=%s'