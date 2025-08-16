#!/usr/bin/env python3
"""
este modulo contiene una funcion en python que sirbe
para listar todos los documentos de una coleccion
"""
import pymongo
from pymongo import MongoClient
import os


def list_all(mongo_collection):
    """
    Lista todos los documentos en una colección de MongoDB.

    args:
        mongo_collection: El objeto de colección de PyMongo.

    returns:
        list: Una lista de todos los documentos en la colección.
              Devuelve una lista vacía si la colección está vacía.
    """
    try:
        documents = list(mongo_collection.find())
        return documents
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error de conexión: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []
