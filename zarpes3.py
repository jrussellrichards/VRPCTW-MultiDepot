__author__ = 'Plinio H. Vargas'
__date__ = '2015  18, 2:42 PM'

import sys
import copy


matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
data = [1, 2, 3, 4]
#datos para tsp
n = len(data)
all_sets = []
g = {}
p = []
#datos para ruteo
minDistance=999

def tsp(vehicle):
    
    for x in vehicle:
                  
        g[x , ()] = matrix[clientes[x]-1][0]

    VehicleClients=tuple(vehicle)    
    #claves=tuple(clientes.keys()) 
         
    get_minimum(1, VehicleClients)

    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()

    print(solution[1][0], end=', ')

    for x in range(len(vehicle) - 1):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                break
    print('1}')
    return


def get_minimum(k, a):
     
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
   
    for j in a:
        comuna=clientes[j]

        set_a = copy.deepcopy(list(a))  
    
        set_a.remove(j)

        all_min.append([j, tuple(set_a)])

        result = get_minimum(j, tuple(set_a))

        values.append(matrix[k-1][j-1] + result)


    # get minimun value from set as optimal solution for
    print("k,a",k,a)
    print("g vale",g)
    
    g[k, a] = min(values)
   
    p.append(((k, a), all_min[values.index(g[k, a])]))
 

    return g[k, a]


if __name__ == '__main__':

  # clientes=(2,3,4)
    clientes={}
    continuar=1
    vehicles=[[2,3,4],[],[],[],[]]
    
    print("agregue cliente")
    while(continuar==1):

        idd = int(input())
        destino= int(input())
        clientes[idd]=destino
        idd = int(input())
        destino= int(input())
        clientes[idd]=destino
        idd = int(input())
        destino= int(input())
        clientes[idd]=destino

            
        i=vehicles[0]    
        distance1=tsp(tuple(i))
            #print("distancia",distance1)
        print("agregar otro?")
        continuar=int(input())
    
    
    
    
    