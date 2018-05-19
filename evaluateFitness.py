import random
import json
import re
import copy
from time import time
import os



#ruta=[[21, 31, 19, 17, 13, 7, 26],[12, 1, 16, 30],[27, 24],[29, 18, 8, 9, 22, 15, 10, 25, 5, 20],[14, 28, 11, 4, 23, 3, 2, 6]]


ruta=[[100, 20, 27, 24, 6, 13, 26, 30], [101, 28, 18, 8, 22, 29, 10, 15, 25, 5], [102, 9, 11, 4, 23, 2, 3, 14], [103, 16, 7, 17, 31, 21, 19], [104, 1, 12]]
clients_vehicles = json.loads(open('customCustomers.json').read())
clientes = clients_vehicles["clients_vehicles"]
problem = json.loads(open('customProblem.json').read())
distances= problem["distance_matrix"]
cantidadvehiculo=problem["max_vehicle_number"]
capacidadvehiculo=problem["vehicle_capacity"]  
def fitness(): #Se calcula la evaluación fitness para cada ruta

        route=ruta
        subRouteDistance=0
        routDistance=0
        capacity=0
        vehicle_use=0

            
    
        print(ruta)
       
        for subRoute in route:
            vehicle_use+=1
            positionLastCustomerID = 0
            subRouteDistance = 0
            #print("subruta",subRoute)
            for customerID in subRoute:
                #distance1=distances[customerID][lastCustomerID]
                positionCustomerId=clientes[str(customerID)]["position"]

                distance=distances[positionCustomerId][positionLastCustomerID]
                #print("distancia entre customerID y lastCustomerID",distance, positionCustomerId,positionLastCustomerID)
                #print("customerID,lastCustomerID,distancia",customerID,lastCustomerID,distances[customerID][lastCustomerID])          
                subRouteDistance=subRouteDistance+distance
                positionLastCustomerID=positionCustomerId

            #print("last cutomer id, 0",lastCustomerID,distances[lastCustomerID][0])    
            routDistance+=subRouteDistance + distances[positionLastCustomerID][0]
            
    #
        #fitness=routDistance*vehicle_use*vehicle_use
        fitness=routDistance
     
            
                    
        return fitness,vehicle_use


if __name__ == "__main__":

   
    
    
    cantidadvehiculo=problem["max_vehicle_number"]
    capacidadvehiculo=problem["vehicle_capacity"]   
    print(cantidadvehiculo,capacidadvehiculo)
    print(fitness())