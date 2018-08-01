import sys
import copy
import os
import json

matrices = json.loads(open('matrixZarpes.json').read())
matrixComuna= matrices["adjacency"]
matrix=matrices["distances"]
numberVehicles=matrices["numberVehicles"]


auto=80
deposito={0:copy.copy(auto)}

archivo_log = open("log.txt", "w")
archivo_log.write("La matriz de distancia es:"+'\n')
for fila in matrix:
  archivo_log.write("%s\n" % fila)
archivo_log.write("Por otro lado la matriz de adyacencia es:"+'\n')
for fila in matrixComuna:
  archivo_log.write("%s\n" % fila)




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
	print("vehicle",vehicle)
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
			global auto
			aux=0	

			print("vehicles",vehicles)
			for i,v in enumerate(vehicles):# Para cada vehículo agrega el cliente y calcula el tsp para ese vehículo. El vehículo que da la distancia mínima, es al que se agrega el cliente.
				
				v.append(idd)
				ruta=tsp(tuple(v))
				distance=ruta[1]
				archivo_log.write("probando con el  vehiculo "+str(deposito[i])+" obtenemos que la mejor ruta es: "+str(ruta[0])+" y aquella ruta tiene una distancia de: "+str(distance)+'\n')

				if(i==0):
					
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
			#print("aux=",aux)
			archivo_log.write("se agrego el cliente al vehiculo "+str(deposito[aux])+" ya que es la distancia más corta"+'\n')
			rutaAux=tsp(tuple(vehicles[aux]))[0]
			g = {}
			p = [] 

			ultimo=rutaAux[-1]
			penultimo=rutaAux[-2]


			if(matrixComuna[clientes[penultimo]-1][clientes[ultimo]-1]!=1 and len(vehicles)<numberVehicles ):

				vehicles.append([])
				auto+=1
				indicador=copy.copy(auto)
				deposito[len(vehicles)-1]=indicador				
				vehicles[-1].append(idd)
				vehicles[aux].remove(idd)

				print("se agrego el cliente",idd,"al vehiculo",len(vehicles))
				archivo_log.write("como la mejor ruta no es compatible con la matriz de adyacencia debemos asignar otro automovil "+str(deposito[len(vehicles)-1])+"por lo que los moviles quedan:"+str(vehicles)+'\n')




			else:				
				print("se agrego el cliente",idd,"al vehículo",aux+1)

			

			if(len(vehicles[aux])==8):
				print("el vehiculo",aux+1,"se llenó")
				vehicles.pop(aux)
				archivo_log.write("el vehiculo "+str(deposito[aux])+" se llenó"+'\n')

				if(len(deposito)==1):
					deposito[0]+=1
					archivo_log.write("debe partir el último vehículo así que se asignará otro "+str(deposito)+'\n')	

				else:

					for x in range(0,len(deposito),1):
						if x < len(deposito)-1:
							deposito[x]= deposito.pop(x+1)

			
						


					
			if(vehicles==[]):
				vehicles.append([])



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
		archivo_log.write("\n"+"Nuevo cliente, su id es: "+str(idd)+" y el destino:"+str(destino)+'\n')
		
		

		for pos,i in enumerate(vehicles):
			

			if(i==[]):
				# tsp(tuple(i))
				i.append(idd)
				# tsp(tuple(i))
				archivo_log.write("se agrego el cliente al vehiculo"+str(deposito[0])+'\n')
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
		print("vehicles",vehicles)

		if(v!=[]):
			print("v",v)
			ruta=tsp(tuple(v))
			g = {}
			p = [] 
			vehicles[i] =ruta[0]

			vehicles[i].remove(1)



	print("la ruta óptima para tus vehículos es",vehicles)	
	archivo_log.write("los vehiculos que quedan son: "+str(deposito)+" compuestos de la siguiente manera: "+str(vehicles))
	
	
	
