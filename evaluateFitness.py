import random
import json
import re
import copy
from time import time
import os



#ruta an32k5=[[21, 31, 19, 17, 13, 7, 26],[12, 1, 16, 30],[27, 24],[29, 18, 8, 9, 22, 15, 10, 25, 5, 20],[14, 28, 11, 4, 23, 3, 2, 6]]
#rutaan80k10 [[1, 7 ,21, 40],[10 ,63 ,11 ,24 ,6, 23 ],[13 ,74 ,60, 39 ,3 ,77 ,51 ],[17 ,31 ,27 ,59 ,5 ,44 ,12, 62 ],[29 ,20 ,75 ,57 ,19 ,26 ,35 ,65 ,69 ,56 ,47 ,15 ,33 ,64 ],[30 ,78 ,61 ,16 ,43 ,68 ,8 ,37 ,2 ,34 ],[38 ,72 ,54 ,9 ,55 ,41 ,25 ,46],[42 ,53 ,66 ,67 ,36 ,73 ,49 ],[52 ,28 ,79 ,18 ,48 ,14 ,71],[58 ,32 ,4 ,22 ,45 ,50 ,76, 70 ]] 


ruta= [[21, 31, 19, 17, 13, 7, 26],[12, 1, 16, 30],[27, 24],[29, 18, 8, 9, 22, 15, 10, 25, 5, 20],[14, 28, 11, 4, 23, 3, 2, 6]]
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
            lastCustomerID = 0
            subRouteDistance = 0
            #print("subruta",subRoute)
            for customerID in subRoute:
                distance=distances[customerID][lastCustomerID]
                #print("customerID,lastCustomerID,distancia",customerID,lastCustomerID,distances[customerID][lastCustomerID])          
                subRouteDistance=subRouteDistance+distance
                lastCustomerID=customerID

            #print("last cutomer id, 0",lastCustomerID,distances[lastCustomerID][0])    
            routDistance+=subRouteDistance + distances[lastCustomerID][0]
            
    #
        #fitness=routDistance*vehicle_use*vehicle_use
        fitness=routDistance
     
            
                    
        return fitness,vehicle_use

def selection(Problem_Genetic,population,n):

            heap = []
            # Note: below is for illustration. It can be replaced by 
            # heapq.nlargest( bigArray, k )
            for item in population:
                # If we have not yet found k items, or the current item is larger than
                # the smallest item on the heap,
                if len(heap) < n or fitness(item,Problem_Genetic) < heap[0]:
                    # If the heap is full, remove the smallest element on the heap.
                    if len(heap) == k: heapq.heappop( heap )
                    # add the current element as the new smallest.
                    heapq.heappush( heap, item )
            return heap


if __name__ == "__main__":

   
    
    
    cantidadvehiculo=problem["max_vehicle_number"]
    capacidadvehiculo=problem["vehicle_capacity"]   
    print(cantidadvehiculo,capacidadvehiculo)

    print(fitness())