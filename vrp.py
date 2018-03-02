
import random

class problem:#clase que modela el problema: Recibe los clientes, la capacidad del vehículo y la cantidad de vehículos.
			  #Cada ruta es un cromosoma y son modelados como listas.
			   #Cada individuo corresponde al total de clientes en una ruta, los cuales son guardados en una lista simple


	def __init__(self, demandas,chromosome,capacidadvehiculo,cantidadvehiculo ):

		self.capacidadvehiculo=capacidadvehiculo
		self.cantidadvehiculo=cantidadvehiculo
		self.demandas=demandas
		self.chromosome=chromosome

	def cromtorut(instance,chromosome):
		route=[]
		subRoute = []
		capacidadvehiculo=instance.capacidadvehiculo
		vehicleLoad=0
		lastCustomerID=0
		for customerID in chromosome:
			demanda=instance.clientes[customerID]
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
		print (route)
		return route

	

	def mutation(self,chromosome):    
	
		start, stop = sorted(random.sample(range(len(chromosome)), 2))
		cromo = chromosome[:start] + chromosome[stop:start-1:-1] + chromosome[stop+1:]
		return cromo 

def fitness(route): #sobre la ruta total
		costo=0
		subRouteDistance=0
		routCost=0
		weightCost=0
		for subRoute in route:
			lastCustomerID = 0
			subRouteDistance = 0
			for customerID in subRoute:
				distance=distances[customerID][lastCustomerID]          
				subRouteDistance=subRouteDistance+distance
				lastCustomerID=customerID
			routCost+=subRouteDistance
			totalCost=routCost+weightCost
		fitness=1/totalCost 
		return fitness   

	
def crossover(ind1, ind2):
	print("individuo 1",ind1)
	print("individuo 2",ind2)
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

	print("se transforma en",ind1)
	print("se transforma en",ind2)
	return ind1, ind2
	




def genetic_algorithm(Problem_Genetic,k,opt,ngen,size,ratio_cross,prob_mutate):#k participantes en el torneo
	
   
	def initial_population(Problem_Genetic,size): #se crean los cromosomas aleatoriamente, luego se rea una poblacion inicial de cromosomas de acuerdo al tamaño elegido( size)
		def generateRoute():

			individual=Problem_Genetic.chromosome
			route = []
			subRoute = []
			capacidadvehiculo = Problem_Genetic.capacidadvehiculo
			vehicleLoad = 0
			lastCustomerID = 0
			random.shuffle(individual)
	



			for customerID in individual:
				demanda=Problem_Genetic.demandas[customerID] #demanda debe ser una tupla
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

		
		return [generateRoute() for _ in range(size)]   
				
			
			

			
						
			
			
			
	def new_generation_t(Problem_Genetic,k,opt,population,n_parents,n_directs,prob_mutate):
		
		def tournament_selection(Problem_Genetic,population,n,k,opt):#devuelve los n ganadores ganadores del torneo
			winners=[]
			for _ in range(n):
				elements = random.sample(population,k) #se escogen los k participantes del torneo
				padre1=elements[0]
				padre2=elements[1]
				fitness1=fitness(padre1)
				fitness2=fitness(padre2)    

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
	

	bestChromosome = opt(population, key = fitness)
	print(bestChromosome)


	return (bestChromosome,fitness(bestChromosome))





if __name__ == "__main__":

	clientes = {0:2,1:4,2:7,3:5,4:2,5:8,6:1,7:2,8:3}
	chromosome=[0,1,2,3,4,5,6,7,8]
	w0 = [0,454,317,165,528,222,223,410,323]
	w1 = [453,0,253,291,210,325,234,121,323]
	w2 = [317,252,0,202,226,108,158,140,323]
	w3 = [165,292,201,0,344,94,124,248,323]
	w4 = [508,210,235,346,0,336,303,94,323]
	w5 = [222,325,116,93,340,0,182,247,222]
	w6 = [223,235,158,125,302,185,0,206,222]
	w7 = [410,121,141,248,93,242,199,0,111]
	w8 = [410,121,141,248,93,242,199,999,0]
	distances = {0:w0,1:w1,2:w2,3:w3,4:w4,5:w5,6:w6,7:w7,8:w8}

	instance=problem(clientes,chromosome,8,4)
	
	genetic_algorithm(instance,2,min,200,100,0.8,0.05)


 


	
	# Constant that is an instance object 
	
   


		