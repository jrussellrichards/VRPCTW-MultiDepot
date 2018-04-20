import sys
import copy
import os



matrix = [
	[0, 2, 9, 10],
	[0, 0, 6, 4],
	[0, 7, 0, 8],
	[0, 3, 12, 0]
]

matrixComuna = [
	[1, 1, 0, 0],
	[1, 1, 1, 1],
	[1, 0, 1, 0],
	[1, 1, 0, 1]
]





g = {} # guarda la distancia mínima entre rutas ej: (1,(2,3,4)):3 , el valor mínimo desde ir de 1 y pasar por 2 3 y 4
p = []#guarda las rutas óptimas
#datos para ruteo
vehicles=[[]]

class vehicle:

	def __init__(self,code):
		self.code=code
		capacity=8
		clients=[]
		avaible=True

	def llenar(client):

		if(capacity<8):

			clients.append(client)
			capacity-=1

def tsp(vehicle): #el algoritmo tsp recibe una ruta en forma de tupla
#   print("calculando para el vehiculo",vehicle)
	
	finalSolution=[] #para guardar la solucion final
	for x in vehicle: 

			   
		g[x , ()] = matrix[clientes[x]-1][0]

	VehicleClients=tuple(vehicle)    

		 
	distance=get_minimum(1, VehicleClients)


	solution = p.pop()
	
	
	finalSolution.append(1)

	finalSolution.append(solution[1][0])

	for x in range(len(vehicle) - 1):
		for new_solution in 	p:
			if tuple(solution[1]) == new_solution[0]:
				solution = new_solution
				#print(solution[1][0], end=', ')
				finalSolution.append(solution[1][0])
				break

	
	return finalSolution,distance


def get_minimum(k, a): #calcula camino mínimo entre el nodo k y el set de nodos a
	


	if (k, a) in g:


		# Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
		return g[k, a]


	values=[]
	all_min=[]


	for j in a: #j es el valor de cada cliente y a es el valor de cada sub ruta
		
		
		comunaJ=clientes[j]
		comunaK=clientes[k]

		set_a = copy.deepcopy(list(a))  
				 
		set_a.remove(j)

		all_min.append([j, tuple(set_a)])

		result = get_minimum(j, tuple(set_a))

		values.append(matrix[comunaK-1][comunaJ-1] + result)#costo de ir desde k a j + la distancia más corta en ir a j y pasar por el anterior set_a

	g[k, a] = min(values)
	p.append(((k, a), all_min[values.index(g[k, a])]))


	return g[k, a]


def llenar(idd):#agrega el cliente al vehículo que de la menor distancia

			global g
			global p
			global vehicles	
			not_min=True		

			print("vehicles",vehicles)
			for i,v in enumerate(vehicles):# Para cada vehículo agrega el cliente y calcula el tsp para ese vehículo. El vehículo que da la distancia mínima, es al que se agrega el cliente.
				
				print("valor i,,id,v",i,idd,v)
				if(len(v)==3):
					print("el vehiculo ",i,"se ha completado, un nuevo vehículo ocupará su lugar")
					print("el recorrido es ",v)
					vehicles.remove(v)


				else: 	

					v.append(idd)
					ruta=tsp(tuple(v))
					distance=ruta[1]

					if(not_min):
						distanceMin=distance
						aux=i
						
					elif(distance<distanceMin):
						vehicles[aux].remove(idd)
						aux=i		

					elif(distance>=distanceMin):
						v.remove(idd)


					g = {}
					p = [] 

#desde acá verifico que cumplan la condición de la matriz, si no lo hace entonces se crea un nuevo vehículo mientras este sea menor a 5 y lo asigno ahí"""
			
			rutaAux=tsp(tuple(vehicles[aux]))[0]
			g = {}
			p = [] 

			ultimo=rutaAux[-1]
			penultimo=rutaAux[-2]


			if(matrixComuna[clientes[penultimo]-1][clientes[ultimo]-1]!=1 and len(vehicles)<5 ):

				vehicles.append([])
				vehicles[-1].append(idd)
				vehicles[aux].remove(idd)

				print("se agrego el cliente",idd,"al vehiculo",len(vehicles))




			else:
				

				print("se agrego el cliente",idd,"al vehículo",aux+1)





if __name__ == '__main__':

	# clientes=(2,3,4)
	
	clientes={1:1}
	continuar=1
	
	isFull=0
	distanceMin=0
	aux=0
	print("agregue cliente")
	while(continuar==1):
		
		
		idd = int(input())
		destino= int(input())
		clientes[idd]=destino
		
		

		for pos,i in enumerate(vehicles):

			if(i==[]):
				i.append(idd)
				print("agregado el cliente",idd, "al vehículo",pos+1)
				#print(vehicles)
				isFull=0
				break
			else:
				isFull=1    

		if(isFull==1): 
			llenar(idd)

		print("agregar otro?")
		continuar=int(input())



	for i,v in enumerate(vehicles):


		if(v!=[]):

			ruta=tsp(tuple(v))
			g = {}
			p = [] 
			vehicles[i] =ruta[0]

			vehicles[i].remove(1)



	print("la ruta óptima para tus vehículos es",vehicles)	
	
	
	
	
