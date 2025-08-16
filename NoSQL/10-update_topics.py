#!/usr/bin/env python3
"""
este modulo contiene una funcion que sirbe para actualizar documentos
dentro de una coleccion por un nombre especifico
"""
import pymongo
from pymongo import MongoClient
import os


def update_topics(mongo_collection, name, topics):
    """
    Cambia los tópics de un documento basado en el nombre.

    args:
        mongo_collection: El objeto de colección de PyMongo.
        name (str): El nombre del documento a actualizar.
        topics (list): La lista de tópics nuevos.

    returns:
        int: El número de documentos modificados (1 si tiene éxito, 0 si no).
             Retorna -1 en caso de error.
    """
    try:
        filter_query = {"name": name}
        
        update_operation = {"$set": {"topics": topics}}
        
        result = mongo_collection.update_many(filter_query, update_operation)
        
        return result.modified_count
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error de conexión: {e}")
        return -1
    except Exception as e:
        print(f"Error inesperado: {e}")
        return -1
