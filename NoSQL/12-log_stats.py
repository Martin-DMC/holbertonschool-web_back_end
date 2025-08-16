#!/usr/bin/env python3
"""
Este script se conecta a una base de datos de MongoDB
para obtener estadísticas sobre los logs de Nginx.
"""
import pymongo


def run_stats():
    """
    Proporciona estadísticas sobre los logs de Nginx en MongoDB.
    """
    try:
        client = pymongo.MongoClient()

        db = client.logs
        nginx_collection = db.nginx

        total_logs = nginx_collection.count_documents({})
        print(f"{total_logs} logs")

        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            count = nginx_collection.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")

        status_check_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"})
        print(f"{status_check_count} status check")

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error de conexión a MongoDB: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
