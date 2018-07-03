import random
import json
import re
import copy
from time import time
import os
import heapq



if __name__ == "__main__":

    tiempo_inicial = time()
    problem = json.loads(open('datosVrpFinal/an32k5/an32k5.json').read())
    vehicles=problem["vehicles"]
    clientes=problem["customers"]
    dict_idclientes=clientes.keys()
    distances= problem["distance_matrix"]
    cantidadvehiculo=problem["max_vehicle_number"]
    capacidadvehiculo=problem["vehicle_capacity"] 
    print(cantidadvehiculo,capacidadvehiculo)

    print("ingrese cliente 1:")
    cliente1= int(input()) 
    print("ingrese cliente 2:")      
    cliente2= int(input()) 
    distance=distances[clientes[str(cliente1)]["position"]][clientes[str(cliente2)]["position"]]
    print(distance)

    



   

#an32k5Route=[ 21 ,31, 19, 17, 13, 7, 26,12, 1, 16, 30, 27, 24, 29, 18, 8, 9, 22, 15, 10, 25, 5, 20, 14, 28, 11, 4, 23, 3, 2, 6]

        