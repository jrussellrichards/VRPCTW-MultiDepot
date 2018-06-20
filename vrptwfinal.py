import random
import json
import re
import copy
from time import time
import os
import heapq




clear = lambda: os.system('cls')
igen=0


def heapSearch( bigArray, k ):
    heap = []
    # Note: below is for illustration. It can be replaced by 
    # heapq.nlargest( bigArray, k )
    for item in bigArray:
        # If we have not yet found k items, or the current item is larger than
        # the smallest item on the heap,
        if len(heap) < k or item > heap[0]:
            # If the heap is full, remove the smallest element on the heap.
            if len(heap) == k: heapq.heappop( heap )
            # add the current element as the new smallest.
            heapq.heappush( heap, item )
    return heap

class Problem_Genetic:#clase que modela el problema: Recibe los clientes, la capacidad del vehículo y la cantidad de vehículos.
              #Cada ruta es un cromosoma y son modelados como listas.
               #Cada individuo corresponde al total de clientes en una ruta, los cuales son guardados en una lista simple


    def __init__(self, clientes,idclientes,capacidadvehiculo,cantidadvehiculo,idvehicles,vehicles ):

        self.capacidadvehiculo=capacidadvehiculo
        self.cantidadvehiculo=cantidadvehiculo
        self.clientes=clientes
        self.idclientes=idclientes
        self.idvehicles=idvehicles
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
        vehicles=copy.copy(Problem_Genetic.idvehicles)
        

        
            
        
        
        for subRoute in route:
            # print(subRoute)
            # print(Problem_Genetic.vehicles)
            # print(vehicles)
            bestvehicle=min(vehicles,key=lambda x:distances[Problem_Genetic.vehicles[str(x)]["position"]][clientes[str(subRoute[0])]["position"]])  
            # subRouteDistance=distances[Problem_Genetic.vehicles[str(bestvehicle)]["position"]][clientes[str(subRoute[0])]["position"]]
            # print(bestvehicle)
            # for i in vehicles:
            #     print(distances[Problem_Genetic.vehicles[str(i)]["position"]][clientes[str(subRoute[0])]["position"]])
            vehicles.pop(bestvehicle)   

              
            # print("--------")         
            vehicle_use+=1
            lastCustomerID = 0
            subRouteDistance = 0
            #print("subruta",subRoute)
            for customerID in subRoute:
                distance=distances[clientes[str(customerID)]["position"]][clientes[str(lastCustomerID)]["position"]]
                #print("customerID,lastCustomerID,distancia",customerID,lastCustomerID,distances[customerID][lastCustomerID])          
                subRouteDistance=subRouteDistance+distance
                lastCustomerID=customerID

            #print("last cutomer id, 0",lastCustomerID,distances[lastCustomerID][0])    
            routDistance+=subRouteDistance + distances[lastCustomerID][0]
            
    #
        #fitness=routDistance*vehicle_use*vehicle_use
        fitness=routDistance
        if(vehicle_use>Problem_Genetic.cantidadvehiculo ):
            fitness=fitness*1000000000000000
            
                    
        return fitness,vehicle_use

def generateRoute(individue,Problem_Genetic): #Genero sub rutas las cuales representan a un vehículo, cada una es una lista y están contenidas en una lista ruta
        route=[]
        subRoute = []
        capacidadvehiculo=Problem_Genetic.capacidadvehiculo
        vehicleLoad=0
        lastCustomerID=0
        elapsedTime=0
        retorno_debido=10000

        for customerID in individue:
            retorno_customer=clientes[str(customerID)]["hora_vuelo"] 
            hora_max_recogida=clientes[str(customerID)]["hora_max_recogida"]
            hora_min_recogida=clientes[str(customerID)]["hora_min_recogida"]
             #se debe setear la hora de vuelo del origen como infinita
            if(retorno_customer<retorno_debido):#La hora en que debe llegar el vehículo es la cota mínima de las restricciones de horarios de vuelo
                retorno_debido=retorno_customer                     

            demanda=Problem_Genetic.clientes[str(customerID)]["demand"]
            distance=distances[customerID][lastCustomerID]#
            service_time=clientes[str(customerID)]["service_time"]#Tiempo que demora el vehiculo desde que llega donde el cliente hasta que continua el viaje
            returnTime = distances[customerID][0]

            vehicleLoadActualizada=demanda+vehicleLoad            
            updatedElapsedTime = elapsedTime+distance+service_time+returnTime #tiempo transcurrido hasta el momento mas el tiempo que demora en llegar al cliente actual(distancia=tiempo)
            hora_retiro=updatedElapsedTime - returnTime
            
            if (vehicleLoadActualizada <= capacidadvehiculo ) and (updatedElapsedTime <= retorno_debido) and (hora_retiro<= hora_max_recogida ) and ( hora_retiro >= hora_min_recogida ):
                subRoute.append(customerID)
                vehicleLoad=vehicleLoadActualizada
                elapsedTime = updatedElapsedTime - returnTime
            else:
                elapsedTime = distances[0][customerID] + service_time #cambiar por distancia desde vehiculo hasta customer id
                route.append(subRoute)
                subRoute=[customerID]
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
    for i,r in enumerate(finalRoute):
        print("Ruta ",i,":",r)

    print("fitness=",fitness(bestChromosome,Problem_Genetic))


    return (bestChromosome,fitness(bestChromosome,Problem_Genetic))




if __name__ == "__main__":

    tiempo_inicial = time()
    problem = json.loads(open('datosTw/an32k5/an32k5.json').read())
    vehicles=problem["vehicles"]
    clientes=problem["customers"]
    dict_idclientes=clientes.keys()
    distances= problem["distance_matrix"]
    cantidadvehiculo=problem["max_vehicle_number"]
    capacidadvehiculo=problem["vehicle_capacity"] 
    print(cantidadvehiculo,capacidadvehiculo)
    

    idclientes=[]
    for i in dict_idclientes:
        idclientes.append(int(i))
    idclientes.pop(0) 

    idvehicles=[]    
    for i in vehicles.keys():
       idvehicles.append(int(i))  
    #tiempo_inicial= time() 
    #Para optimizar el tiempo de computo, modificamos la matriz con distancia 0 a cada uno de los vehiculos
   # for i in idvehicles:
   #     distances[demands_position[str(i)]["position"]][0]=0
    #distances = {0:w0,1:w1,2:w2,3:w3,4:w4,5:w5,6:w6,7:w7,8:w8}

    instance=Problem_Genetic(clientes,idclientes,capacidadvehiculo,cantidadvehiculo,idvehicles,vehicles)
    #def genetic_algorithm(Problem_Genetic,k,opt,ngen,size,ratio_cross,prob_mutate):#k participantes en el torneo
    genetic_algorithm(instance,2,min,2500,50,0.85,0.05)

    tiempo_final = time() 
    print("tiempo de ejecución",tiempo_final-tiempo_inicial)

   

#an32k5Route=[ 21 ,31, 19, 17, 13, 7, 26,12, 1, 16, 30, 27, 24, 29, 18, 8, 9, 22, 15, 10, 25, 5, 20, 14, 28, 11, 4, 23, 3, 2, 6]

        