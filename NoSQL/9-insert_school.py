#!/usr/bin/env python3
"""
este modulo contiene una funcion que inserta nuevos documentos a
una coleccion
"""
import pymongo
from pymongo import MongoClient
import os


def insert_school(mongo_collection, **kwargs):
    """
    Inserta un nuevo documento en una colección de MongoDB.

    args:
        mongo_collection: El objeto de colección de PyMongo.
        **kwargs: Los campos y valores del nuevo documento a insertar.

    returns:
        ObjectId: El _id del documento recién insertado.
                  Retorna None en caso de error.
    """
    try:
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error de conexión: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
