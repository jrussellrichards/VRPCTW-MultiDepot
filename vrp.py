
import random

class problema:

	def __init__(self, clientes,capacidadvehiculo,cantidadvehiculo ):

		self.capacidadvehiculo=capacidadvehiculo
		self.cantidadvehiculo=cantidadvehiculo
		self.clientes=clientes

     

         

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


		
		



def fitness(route):
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


def mutation(chromosome):
    
    print("el cromosoma es",chromosome)
    start, stop = sorted(random.sample(range(len(chromosome)), 2))
    cromo = chromosome[:start] + chromosome[stop:start-1:-1] + chromosome[stop+1:]
    print("pero se transforma en: ", cromo)
    return cromo




	







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

	instancia=problema(clientes,8,4)
	ruta=cromtorut(instancia,chromosome)
	fitness(ruta)
	mutation(chromosome)


 


	
    # Constant that is an instance object 
    
   


        