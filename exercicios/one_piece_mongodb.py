import json
import pymongo as mg

conexao = mg.MongoClient("mongodb://localhost:27017/")

db = conexao['one_piece']

collection_episodios = db['episodios']

with open("One_Piece.json", "r") as arquivo :
  dados = json.load(arquivo) 

collection_episodios.insert_many(dados)

print(collection_episodios.count_documents({}))

db.drop_collection("episodios")
conexao.close()


# anos = [doc["start"] for doc in colecao.find()]
# contagem = Contador (anos)
# for ano, qtd in sorted(contagem.items()):
#     print (f"{ano}: {qtd}")