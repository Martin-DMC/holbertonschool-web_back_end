#!/usr/bin/env python3
"""
Este modulo contiene una funcion que retorna una lista
que tienen un tema especifico en su lista de 'topics'.
"""
import pymongo
from pymongo import MongoClient
import os


def schools_by_topic(mongo_collection, topic):
    """
    Devuelve la lista de escuelas que tienen un tema específico.

    args:
        mongo_collection: El objeto de colección de PyMongo.
        topic (string): el topic a buscar.

    returns:
        list: una lista de documentos que hicieron match.
    """
    try:
        filter_query = {"topics": topic}

        cursor = mongo_collection.find(filter_query)

        return list(cursor)

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error de conexión: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []
