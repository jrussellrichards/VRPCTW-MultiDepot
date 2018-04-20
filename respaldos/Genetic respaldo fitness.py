
import random
import json
import re
import copy
from time import time

class Problem_Genetic:#clase que modela el problema: Recibe los clientes, la capacidad del vehículo y la cantidad de vehículos.
			  #Cada ruta es un cromosoma y son modelados como listas.
			   #Cada individuo corresponde al total de clientes en una ruta, los cuales son guardados en una lista simple


	def __init__(self, clientes,chromosome,capacidadvehiculo,cantidadvehiculo ):

		self.capacidadvehiculo=capacidadvehiculo
		self.cantidadvehiculo=cantidadvehiculo
		self.clientes=clientes
		self.chromosome=chromosome

	

	def mutation(self,chromosome):    
	
		start, stop = sorted(random.sample(range(len(chromosome)), 2))
		cromo = chromosome[:start] + chromosome[stop:start-1:-1] + chromosome[stop+1:]
		return cromo 




def fitness(individue,Problem_Genetic): #sobre la ruta total

		route=generateRoute(individue,Problem_Genetic)
		#print("individuo",individue)
		costo=0
		subRouteDistance=0
		routDistance=0
		capacity=0
		spaceUsed=0
		vehicleUse=0
		global distanceMax
		global distanceMin
		global vehicleMax
		global vehicleMin
		global count
		
		
		for subRoute in route:
			vehicleUse+=1
			lastCustomerID = 0 # para tener la penalización desde el origen. Si tengo [4,5,6] calcula la distancia entre el origen y 4, entre 4 y 5 y entre 5 y 6
			subRouteDistance = 0
			for customerID in subRoute:
				distance=distances[customerID][lastCustomerID]          
				subRouteDistance=subRouteDistance+distance
				lastCustomerID=customerID
			routDistance+=subRouteDistance
	#	print("distancia ruta",routDistance,"distancia maxima",distanceMax,"distancia minima",distanceMin)
		if(routDistance<distanceMin):
		#	print("como distancia de ruta es menor a la minima ruta minima igual a distancia de ruta")
			distanceMin=routDistance
		#	print("distancia ruta",routDistance,"distancia maxima",distanceMax,"distancia minima",distanceMin)
		elif(routDistance>distanceMax):
		#	print("como la ruta era mayor a la maxima pero no menor a la minima, distancia maxima igual a distancia ruta")
			distanceMax=routDistance
		#	print("distancia ruta",routDistance,"distancia maxima",distanceMax,"distancia minima",distanceMin)
		if(vehicleUse>vehicleMax):
			vehicleMax=vehicleUse

		elif(vehicleUse<vehicleMin):
			vehicleMin=vehicleUse
		#print("distancia ruta",routDistance)
			
		Fdistance=(distanceMax-routDistance)/(distanceMax-distanceMin)
		if(vehicleMax==vehicleMin):
			Fvehicle=0
		else:
			Fvehicle=(vehicleMax-vehicleUse)/(vehicleMax-vehicleMin)
		fitness= (Fdistance+Fvehicle)/2		
					
		return fitness 

def generateRoute(individue,Problem_Genetic):
		route=[]
		subRoute = []
		capacidadvehiculo=Problem_Genetic.capacidadvehiculo
		vehicleLoad=0
		lastCustomerID=0

		

		for customerID in individue:			

			demanda=Problem_Genetic.clientes[str(customerID)]["demand"]

			vehicleLoadActualizada=demanda+vehicleLoad
			
			if (vehicleLoadActualizada <= capacidadvehiculo):
				subRoute.append(customerID)
				vehicleLoad=vehicleLoadActualizada
			else:

				route.append(subRoute)
				subRoute= [customerID]
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
	




def genetic_algorithm(Problem_Genetic,k,opt,ngen,size,ratio_cross,prob_mutate):#k participantes en el torneo
	
   
	def initial_population(Problem_Genetic,size): #se crean los cromosomas aleatoriamente, luego se rea una poblacion inicial de cromosomas de acuerdo al tamaño elegido( size)
		population=[]
		individue=Problem_Genetic.chromosome

		for i in range(size):
			
			random.shuffle(individue)
			aux=copy.deepcopy(individue)			
			population.append(aux)
				

		return population
		 
				
			
				

	
			
			
	def new_generation_t(Problem_Genetic,k,opt,population,n_parents,n_directs,prob_mutate):
		
		def tournament_selection(Problem_Genetic,population,n,k,opt):#devuelve los n ganadores ganadores del torneo
			winners=[]
			for _ in range(n):
				elements = random.sample(population,k) #se escogen los k participantes del torneo
				padre1=elements[0]
				padre2=elements[1]
				
				fitness1=fitness(padre1,Problem_Genetic)
				fitness2=fitness(padre2,Problem_Genetic)    

				if(fitness1>fitness2):
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
						
		directs        =   tournament_selection(Problem_Genetic, population, n_directs, k, opt)
		crosses        =   cross_parents(Problem_Genetic,tournament_selection(Problem_Genetic, population, n_parents, k, opt))#la cruza se escoge con otros ganadores del torneo para mantener la diversidad
		mutations      =   mutate(Problem_Genetic, crosses, prob_mutate)
		new_generation =   directs + mutations
		
		return new_generation
	
	population = initial_population(Problem_Genetic, size)  
	n_parents = round(size*ratio_cross)#se redondea la cantidad de la población que se obtendrá mediante cruzas
	n_parents = (n_parents if n_parents%2==0 else n_parents-1)#debe ser un número par de padres para que se logren cruzar todos
	n_directs = size - n_parents #los hijos deben ser el total menos la cantidad de padres ya que los padres seguirán en la generación quizás mutados
		
	for _ in range(ngen):
		population = new_generation_t(Problem_Genetic, k, opt, population, n_parents, n_directs, prob_mutate)
	

	#bestChromosome = opt(population, key = fitness(population,Problem_Genetic))

	def theBest():
		maxi=population[0]
		
		for i in population:

			if(fitness(i,Problem_Genetic)> fitness(maxi,Problem_Genetic)):
				maxi=i
		return maxi

	bestChromosome=theBest()



	#for i in population:
	#	print("cromosoma y funcion",i,fitness(i,Problem_Genetic))
	#print(bestChromosome)

	finalRoute=generateRoute(bestChromosome,Problem_Genetic)
	print(finalRoute)



	return (bestChromosome,fitness(bestChromosome,Problem_Genetic))


distanceMin=9999
distanceMax=0	
vehicleMax=0
vehicleMin=25
count=0




if __name__ == "__main__":

	clientes = json.loads(open('customers.json').read())
	problem = json.loads(open('problem.json').read())
	distances= problem["distance_matrix"]
	cantidadvehiculo=problem["max_vehicle_number"]
	capacidadvehiculo=problem["vehicle_capacity"]	
	chromosome=[]
		

	for i in clientes.keys():
		chromosome.append(int(i))

	tiempo_inicial= time() 


	
	#distances = {0:w0,1:w1,2:w2,3:w3,4:w4,5:w5,6:w6,7:w7,8:w8}

	instance=Problem_Genetic(clientes,chromosome,capacidadvehiculo,cantidadvehiculo)
	
	genetic_algorithm(instance,2,min,1000,100,0.8,0.05)

	tiempo_final = time() 
	print("tiempo de ejecución",tiempo_final-tiempo_inicial)
 



   


		