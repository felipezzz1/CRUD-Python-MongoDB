# esta classe é responsável pela comunicação com o Mongo
# e realizar as operações de banco de dados
import os
from pymongo import MongoClient
from pymongo.results import InsertOneResult
from pymongo.server_api import ServerApi
from pymongo.synchronous.cursor import Cursor
from dotenv import load_dotenv

from model.produto import Produto


class MongoHandler:
    load_dotenv()
    def __init__(self):
        self.uri = f"mongodb+srv://{os.getenv('API_USER')}:{os.getenv('API_KEY')}@crud.jzxod.mongodb.net/?retryWrites=true&w=majority&appName=CRUD"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client["crud"]
        self.collection = self.db["produtos"]

    def insert_produto(self, produto: Produto) -> InsertOneResult:
        return self.collection.insert_one(produto.__dict__)

    def get_produtos(self) -> Cursor:
        return self.collection.find({})

    def update_produto(self, filtro, novos_valores):
        resultado = self.collection.update_one(filtro, {"$set": novos_valores})
        return resultado.modified_count

    def delete_produto(self, filtro):
        resultado = self.collection.delete_one(filtro)
        return resultado.deleted_count