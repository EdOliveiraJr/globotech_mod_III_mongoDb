import pymongo as mg

# Exercício 1 - Conexão com o MongoDB
# Conecte-se ao servidor local MongoDB e imprima todos os bancos de dados disponíveis.
conexao = mg.MongoClient("mongodb://localhost:27017/")

print("Bancos de dados disponíveis:")
lista_dbs = conexao.list_database_names()
for db in lista_dbs:
    print("-", db)
print()

# Exercício 2 - Criação de banco e coleção
# Crie um banco chamado 'loja_virtual' e uma coleção chamada 'clientes'.
db = conexao["loja_virtual"]

collection_clientes = db["clientes"]

# Exercício 3 - Inserção de um cliente
# Insira o seguinte cliente na coleção 'clientes':
# {"nome": "Amanda Souza", "idade": 28, "email": "amanda@gmail.com", "compras": 3}
cliente_1 = {
    "nome": "Amanda Souza",
    "idade": 28,
    "email": "amanda@gmail.com",
    "compras": 3,
}

collection_clientes.insert_one(cliente_1)

# Exercício 4 - Inserção múltipla
# Insira os seguintes clientes:
# {"nome": "Carlos Lima", "idade": 35, "email": "carlos@gmail.com", "compras": 5}
# {"nome": "Fernanda Dias", "idade": 22, "email": "fernanda@gmail.com", "compras": 1}
clientes_1 = [
    {"nome": "Carlos Lima", "idade": 35, "email": "carlos@gmail.com", "compras": 5},
    {"nome": "Fernanda Dias", "idade": 22, "email": "fernanda@gmail.com", "compras": 1},
]

collection_clientes.insert_many(clientes_1)

# Exercício 5 - Listar bancos e coleções
# Liste todos os bancos de dados e todas as coleções dentro de 'loja_virtual'.
bancos = conexao.list_database_names()

print("Bancos de dados disponíveis:")
for banco in bancos:
    print("-", banco)
print()

lista_colecoes = db.list_collection_names()

print(f"Coleções no banco '{db.name}':")
for colecao in lista_colecoes:
    print("-", colecao)
print()

# Exercício 6 - Buscar todos os clientes
# Exiba todos os documentos da coleção 'clientes'.
todos_clientes = collection_clientes.find()
print(f"Todos os clientes da coleção:")
for cliente in todos_clientes:
    print("-", cliente)
print()

# Exercício 7 - Filtros simples
# Recupere todos os clientes com mais de 2 compras.
todos_cliente_mais_duas_compras = collection_clientes.find({"compras": {"$gte": 2}})
print(f"Todos os clientes com mais de 2 compras")
for cliente in todos_cliente_mais_duas_compras:
    print("-", cliente)
print()

# Exercício 8 - Atualização
# Atualize o número de compras do cliente 'Fernanda Dias' para 3.
collection_clientes.update_one({"nome": "Fernanda Dias"}, {"$set": {"compras": 3}})

print("Cliente Fernanda Dias atualizada")
print(collection_clientes.find_one({"nome": "Fernanda Dias"}))
print()

# Exercício 9 - Remoção
# Remova o cliente com o nome 'Carlos Lima'.
collection_clientes.delete_one({"nome": "Carlos Lima"})
print("Cliente Carlos Lima removido")
print(collection_clientes.find_one({"nome": "Carlos Lima"}))
print()


# Exercício 10 - Desafio bônus
# Crie uma nova coleção chamada 'produtos', insira 3 documentos com os campos: nome, categoria, preco,estoque.
# Depois, exiba todos os produtos da categoria 'eletrônicos' cujo preço seja maior que R$ 100.
collection_produtos = db["produtos"]

lista_produtos = [
    {"nome": "notebook", "categoria": "eletrônicos", "preco": 3299.90, "estoque": 10},
    {"nome": "mp4", "categoria": "eletrônicos", "preco": 99.90, "estoque": 100},
    {"nome": "caderno", "categoria": "papelaria", "preco": 21.50, "estoque": 150},
    {
        "nome": "geladeira",
        "categoria": "eletrodomésticos",
        "preco": 2599.90,
        "estoque": 5,
    },
]

collection_produtos.insert_many(lista_produtos)

eletronicos_mais_que_100 = collection_produtos.find(
    {"categoria": "eletrônicos", "preco": {"$gt": 100.00}}
)

print("Produtos eletrônicos com preço maior que R$ 100.00")
for eletronico in eletronicos_mais_que_100:
    print(eletronico)
print()

db.drop_collection("clientes")
db.drop_collection("produtos")
conexao.close()

