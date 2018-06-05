import numpy as np
import json
import sys
import re

def distance(customer1, customer2):
        return ((customer1[0] - customer2[0])**2 + (customer1[1] - customer2[1])**2)**0.5

if __name__ == "__main__":
    number_vechile=5
    vehicle_capacity=100

    matrix = np.loadtxt('test/an32k5.vrp', usecols=(1,2))
    f = open("customProblem.json","w") 
    f.write("{ \n"+'"max_vehicle_number":'+str(number_vechile)+", \n")
    f.write('"vehicle_capacity":'+str(vehicle_capacity)+","+"\n")
    f.write('"distance_matrix":[')


    #Convertir distancias
    distances=[]


    for i,c1 in enumerate(matrix):

        distances.append([])


        for c2 in matrix:
            d=round(distance(c1,c2),2)
            distances[i].append(d)
            
        f.write(str(distances[i])+","+"\n")    

    f.write("],"+"\n")

    #End convertir distancias


    fclientes=np.loadtxt('test/an32k5clientes.vrp', usecols=())
    
    for i,c in enumerate(fclientes):
        f.write('"'+str(i+1)+'":'+'{"demand":'+str(c[1])+"},\n")
  
    f.write("}")


