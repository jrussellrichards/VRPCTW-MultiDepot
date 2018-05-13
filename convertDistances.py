import numpy as np
import json
import sys

def distance(customer1, customer2):
        return ((customer1[0] - customer2[0])**2 + (customer1[1] - customer2[1])**2)**0.5

if __name__ == "__main__":

    matrix = np.loadtxt('test/fn45k4.vrp', usecols=(1,2))
    f = open("distanciasCalculadas.json","w") 
    f.write('"distance_matrix:"')


 
    distances=[]


    for i,c1 in enumerate(matrix):

        distances.append([])

        for c2 in matrix:
            d=round(distance(c1,c2),2)
            distances[i].append(d)
            


            
    f.write(str(distances))


