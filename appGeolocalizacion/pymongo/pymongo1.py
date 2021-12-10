# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:50:29 2021

@author: lenovo
"""

from pymongo import MongoClient
from pprint import pprint
#"mongodb://username:password@host:port/database"
#conexión a servidor mongo


mongo = MongoClient("localhost",27017)
#Lista de bases de datos
#print(mongo.list_database_names())

dbejemplo = mongo["colegio"]
#lista las colecciones de la base de datos
#print(dbejemplo.list_collection_names())

#Creación de colección productos en base de datos testg51
#dbejemplo.create_collection("producto")
#print(dbejemplo.list_collection_names())

"""
coleccionProductos = dbejemplo["productos"]

listaproductos = coleccionProductos.find({})
for doc in listaproductos:
    pprint(doc)
  """  

dbaccion = mongo["accion"]
colfamilia = dbaccion["familia"]
print(colfamilia.count_documents({}))
#Falta el .sort en el filtro    
listafamilia = colfamilia.find({},{"_id":0}).limit(10)
for doc in listafamilia:
    pprint(doc)


mongo.close()


#FLASK .app WEB con formulario para registrar datos, direccion-> latitud y longitud geopy,verlo en mapa . Visual studio code


