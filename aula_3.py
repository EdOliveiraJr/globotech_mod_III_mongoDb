from pymongo import MongoClient

# Conexão com o MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Criando ou acessando um banco de dados
db = client["meu_banco"]

# Criando ou acessando uma coleção
colecao = db["minha_colecao"]

# Limpando a coleção para testes
colecao.delete_many({})

# ===== INSERÇÕES =====
print("\n--- Inserindo documentos ---")

# Inserção única
documento = {"nome": "João", "idade": 30, "email": "joao@example.com"}
res1 = colecao.insert_one(documento)
print("1 documento inserido:", res1.inserted_id)

# Inserção múltipla
documentos = [
    {"nome": "Maria", "idade": 25, "email": "maria@example.com"},
    {"nome": "Carlos", "idade": 35, "email": "carlos@example.com"},
    {"nome": "Ana", "idade": 40},
    {"nome": "Beatriz", "idade": 25}
]
res2 = colecao.insert_many(documentos)
print("Documentos inseridos:", res2.inserted_ids)

# ===== CONSULTAS =====
print("\n--- Todos os documentos ---")
for doc in colecao.find():
    print(doc)

print("\n--- find_one (Maria) ---")
print(colecao.find_one({"nome": "Maria"}))

print("\n--- idade > 30 ---")
for doc in colecao.find({"idade": {"$gt": 30}}):
    print(doc)

print("\n--- Apenas nomes (projeção) ---")
for doc in colecao.find({}, {"_id": 0, "nome": 1}):
    print(doc)

# ===== CONTAGEM E VALORES ÚNICOS =====
print("\n--- Contagem de pessoas com idade > 30 ---")
print(colecao.count_documents({"idade": {"$gt": 30}}))

print("\n--- Idades únicas ---")
print(colecao.distinct("idade"))

# ===== ATUALIZAÇÕES =====
print("\n--- Atualizando o email de João ---")
colecao.update_one({"nome": "João"}, {"$set": {"email": "joao_novo@email.com"}})

print("\n--- Incrementando idade de quem tem > 30 ---")
colecao.update_many({"idade": {"$gt": 30}}, {"$inc": {"idade": 1}})

# ===== CONSULTA PÓS-ATUALIZAÇÃO =====
print("\n--- Documentos após atualizações ---")
for doc in colecao.find():
    print(doc)

# ===== REMOÇÕES =====
print("\n--- Deletando Carlos ---")
colecao.delete_one({"nome": "Carlos"})

print("\n--- Deletando quem tem idade < 30 ---")
colecao.delete_many({"idade": {"$lt": 30}})

# ===== CONSULTA FINAL =====
print("\n--- Documentos restantes ---")
for doc in colecao.find():
    print(doc)

# ===== INFO DE BANCO E COLEÇÕES =====
print("\n--- Bancos disponíveis ---")
print(client.list_database_names())

print("\n--- Coleções em 'meu_banco' ---")
print(db.list_collection_names())

# ===== OPERADORES LÓGICOS =====
print("\n--- nome = Ana OU idade = 25 ---")
query = {"$or": [{"nome": "Ana"}, {"idade": 25}]}
for doc in colecao.find(query):
    print(doc)


with open("One Piece Json.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

colecao.insert_many(dados)

# 1. Mostrar os primeiros 5 documentos
print("\n=== Amostragem (5 primeiros documentos) ===")
for doc in collection.find().limit(5):
    print(doc)


# 2. Contar quantos documentos existem
total = collection.count_documents({})
print(f"\n=== Total de documentos: {total} ===")

# 3. Listar todos os nomes de campos encontrados
campos = set()
for doc in collection.find().limit(100):
    campos.update(doc.keys())
print("\n=== Campos únicos encontrados ===")
print(campos)

# 4. Frequência dos valores no campo "start"
anos = [doc.get("start") for doc in collection.find()]
contagem = Counter(anos)
print("\n=== Distribuição por ano (start) ===")
for ano, qtd in contagem.items():
    print(f"{ano}: {qtd}")

#ordenar as informações
collection.find().sort("average_rating", -1).limit(10)
