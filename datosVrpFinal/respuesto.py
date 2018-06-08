import random
import json
import re
import copy
from time import time
import os


clear = lambda: os.system('cls')
igen=0
class Problem_Genetic:#clase que modela el problema: Recibe los clientes, la capacidad del vehículo y la cantidad de vehículos.
                      #Cada ruta es un cromosoma y son modelados como listas.
                      #Cada individuo corresponde al total de clientes en una ruta, los cuales son guardados en una lista simple


    def __init__(self, clientes,idclientes,capacidadvehiculo,cantidadvehiculo,vehicles ):

        self.capacidadvehiculo=capacidadvehiculo
        self.cantidadvehiculo=cantidadvehiculo
        self.clientes=clientes
        self.idclientes=idclientes
        self.vehicles=vehicles

    
    def mutation(self,idclientes):    
    
        start, stop = sorted(random.sample(range(len(idclientes)), 2))
        cromo = idclientes[:start] + idclientes[stop:start-1:-1] + idclientes[stop+1:]
        return cromo 




def fitness(individue,Problem_Genetic): #Se calcula la evaluación fitness para cada ruta

        route=generateRoute(individue,Problem_Genetic)
        subRouteDistance=0
        routDistance=0
        capacity=0
        vehicle_use=0
        infactible=0

      #  print(route)
        for subRoute in route:
            vehicle_use+=1
            positionLastCustomerID = 0
            subRouteDistance = 0 - distances[Problem_Genetic.clientes[str(subRoute[0])]["position"]][0]
            #print("subruta",subRoute)
            for customerID in subRoute:
                #distance1=distances[customerID][lastCustomerID]
               # ventana_retiro_min=Problem_Genetic.clientes[str(customerID)]["ventanas"]["retiro"][0]
               # ventana_retiro_max=Problem_Genetic.clientes[str(customerID)]["ventanas"]["retiro"][1]
                #print("customerid,ventana retiro min y max",customerID,ventana_retiro_min,ventana_retiro_max)

                positionCustomerId=Problem_Genetic.clientes[str(customerID)]["position"]
                distance=distances[positionCustomerId][positionLastCustomerID]

               # print("distancia entre customerID y lastCustomerID",distance, positionCustomerId,positionLastCustomerID)

                #print("customerID,lastCustomerID,distancia",customerID,lastCustomerID,distances[customerID][lastCustomerID])          
                subRouteDistance=subRouteDistance+distance
               # if(subRouteDistance>ventana_retiro_max or subRouteDistance<ventana_retiro_min):
                #   infactible=1
                positionLastCustomerID=positionCustomerId

            #print("last cutomer id, 0",lastCustomerID,distances[lastCustomerID][0])    
            routDistance+=subRouteDistance + distances[positionLastCustomerID][0]
            
    #   
        #fitness=routDistance*vehicle_use*vehicle_use
        fitness=routDistance
        if(vehicle_use>Problem_Genetic.cantidadvehiculo or infactible==1 ):
            fitness=fitness*1000000000000000
            
                    
        return fitness,vehicle_use

def generateRoute(individue,Problem_Genetic): #Genero sub rutas las cuales representan a un vehículo, cada una es una lista y están contenidas en una lista ruta
        route=[]
        subRoute = []
        capacidadvehiculo=Problem_Genetic.capacidadvehiculo
        vehicleLoad=0
        lastCustomerID=0
        false_client=900
        vehicles_aux=copy.copy(idvehicles)


        #random.shuffle(vehicles_aux)

        pos_vehicle=vehicles_aux.pop(0)

        distancia=0
        subRoute.append(pos_vehicle)
        lastCustomerID=pos_vehicle

        for customerID in individue:            
            ventana_retiro_min=Problem_Genetic.clientes[str(customerID)]["ventanas"]["retiro"][0]
            ventana_retiro_max=Problem_Genetic.clientes[str(customerID)]["ventanas"]["retiro"][1]
            demanda=Problem_Genetic.clientes[str(customerID)]["demand"]
            vehicleLoadActualizada=demanda+vehicleLoad
            distancia+=distances[Problem_Genetic.clientes[str(customerID)]["position"]][Problem_Genetic.clientes[str(lastCustomerID)]["position"]]

           # print("cliente,min ventana,max ventana, distancia",customerID,ventana_retiro_min,ventana_retiro_max,distancia)
            if ((vehicleLoadActualizada <= capacidadvehiculo) and distancia<ventana_retiro_max and distancia>ventana_retiro_min ):
                subRoute.append(customerID)
                vehicleLoad=vehicleLoadActualizada

            else:
               # print("no se cumple")
                route.append(subRoute)
                pos_vehicle=vehicles_aux.pop(0)
                distancia=distances[Problem_Genetic.clientes[str(customerID)]["position"]][Problem_Genetic.clientes[str(pos_vehicle)]["position"]]
                lastCustomerID=pos_vehicle
                subRoute=[pos_vehicle]
                subRoute.append(customerID)
                vehicleLoad=demanda
            lastCustomerID=customerID

        if subRoute != []:
            route.append(subRoute)
        return route
    
def crossover(ind1, ind2):
    #print("individuo 1",ind1)
    #print("individuo 2",ind2)
    size = min(len(ind1), len(ind2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    temp1 = ind1[cxpoint1:cxpoint2+1] + ind2
    temp2 = ind1[cxpoint1:cxpoint2+1] + ind1
    ind1 = []
    for x in temp1:
        if x not in ind1:           
            ind1.append(x)
    ind2 = []
    for x in temp2:
        if x not in ind2:
            ind2.append(x)

    return ind1, ind2
    




def genetic_algorithm(Problem_Genetic,k,opt,ngen,size,ratio_cross,prob_mutate):#k participantes en el torneo, size= tamaño de poblacion
    
   
    def initial_population(Problem_Genetic,size): #se crean los cromosomas aleatoriamente, luego se crea una poblacion inicial de cromosomas de acuerdo al tamaño elegido( size)
        population=[]
        individue=Problem_Genetic.idclientes

        for i in range(size):
            
            random.shuffle(individue)
            aux=copy.deepcopy(individue)            
            population.append(aux)
                

        return population

            
            
    def new_generation_t(Problem_Genetic,k,opt,population,n_parents,n_directs,prob_mutate):
    
        def selection(Problem_Genetic,population,n):

            
            # Note: below is for illustration. It can be replaced by 
            # heapq.nlargest( bigArray, k )
            heapq.heapify(population)
            heap=heapq.nsmallest(n, population,key= lambda x: fitness(x,Problem_Genetic))

    
            return heap
            
        def tournament_selection(Problem_Genetic,population,n,k,opt):#devuelve los n ganadores ganadores del torneo
            winners=[]
            for _ in range(n):
                elements = random.sample(population,k) #se escogen los k participantes del torneo
                padre1=elements[0]
                padre2=elements[1]
                
                fitness1=fitness(padre1,Problem_Genetic)
                fitness2=fitness(padre2,Problem_Genetic)    

                if(fitness1<fitness2):
                    winners.append(padre1)                  
                else:
                    winners.append(padre2)                  
            return winners
            
        def cross_parents(Problem_Genetic,parents):#Devuelve los cromosomas resultantes por cruza. Se itera de 2 en 2 porque se reproducen de a pares y la función recibe varios padres
            childs=[]
            for i in range(0,len(parents),2):
                childs.extend(crossover(parents[i],parents[i+1]))
            return childs
    
        def mutate(Problem_Genetic,population,prob):
            for i in population:
                if(random.random() < prob):
                    Problem_Genetic.mutation(i)             
                    
            return population
                        
        directs        =   selection(Problem_Genetic, population, n_directs)
        crosses        =   cross_parents(Problem_Genetic,tournament_selection(Problem_Genetic, population, n_parents, k, opt))#la cruza se escoge con otros ganadores del torneo para mantener la diversidad
        mutations      =   mutate(Problem_Genetic, crosses, prob_mutate)
        new_generation =   directs + mutations
        
        return new_generation
    
    population = initial_population(Problem_Genetic, size)  
    n_parents = round(size*ratio_cross)#se redondea la cantidad de la población que se obtendrá mediante cruzas
    n_parents = (n_parents if n_parents%2==0 else n_parents-1)#debe ser un número par de padres para que se logren cruzar todos
    n_directs = size - n_parents #los hijos deben ser el total menos la cantidad de padres ya que los padres seguirán en la generación quizás mutados
        
    for i in range(ngen):
        population = new_generation_t(Problem_Genetic, k, opt, population, n_parents, n_directs, prob_mutate)

    #bestChromosome = opt(population, key = fitness(population,Problem_Genetic))

    def theBest():
        best=population[0]
        
        for i in population:
            if(fitness(i,Problem_Genetic)< fitness(best,Problem_Genetic)):
                
                best=i
        
        return best

    bestChromosome=theBest()
    



    #for i in population:
    #   print("cromosoma y funcion",i,fitness(i,Problem_Genetic))
    #print(bestChromosome)

    finalRoute=generateRoute(bestChromosome,Problem_Genetic)
    print(finalRoute)
    print("fitness=",fitness(bestChromosome,Problem_Genetic))


    return (bestChromosome,fitness(bestChromosome,Problem_Genetic))




if __name__ == "__main__":

    clients_vehicles = json.loads(open('customCustomers.json').read())
    idclientes=clients_vehicles["clients"]
    demands_position=clients_vehicles["clients_vehicles"]
    problem = json.loads(open('customProblem.json').read())
    distances= problem["distance_matrix"]
    cantidadvehiculo=problem["max_vehicle_number"]
    capacidadvehiculo=problem["vehicle_capacity"] 
    vehicles=problem["vehicles"]
    print(cantidadvehiculo,capacidadvehiculo)
    idvehicles=[]

  
    for i in vehicles.keys():
        idvehicles.append(int(i))  
    tiempo_inicial= time() 
    #Para optimizar el tiempo de computo, modificamos la matriz con distancia 0 a cada uno de los vehiculos
   # for i in idvehicles:
   #     distances[demands_position[str(i)]["position"]][0]=0
    #distances = {0:w0,1:w1,2:w2,3:w3,4:w4,5:w5,6:w6,7:w7,8:w8}

    instance=Problem_Genetic(demands_position,idclientes,capacidadvehiculo,cantidadvehiculo,vehicles)
    #def genetic_algorithm(Problem_Genetic,k,opt,ngen,size,ratio_cross,prob_mutate):#k participantes en el torneo
    genetic_algorithm(instance,2,min,1200,800,0.42,0.02)

    tiempo_final = time() 
    print("tiempo de ejecución",tiempo_final-tiempo_inicial)



   

#an32k5Route=[ 21 ,31, 19, 17, 13, 7, 26,12, 1, 16, 30, 27, 24, 29, 18, 8, 9, 22, 15, 10, 25, 5, 20, 14, 28, 11, 4, 23, 3, 2, 6]

        