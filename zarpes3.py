import sys
import copy
import os



matrix = [
	[0, 2, 9, 10],
	[0, 0, 6, 4],
	[0, 7, 0, 8],
	[0, 3, 12, 0]
]

#datos para tsp



g = {} # guarda la distancia mínima entre rutas ej: (1,(2,3,4)):3 , el valor mínimo desde ir de 1 y pasar por 2 3 y 4
p = []#guarda las rutas óptimas
#datos para ruteo


def tsp(vehicle): #el algoritmo tsp recibe una ruta en forma de tupla
#   print("calculando para el vehiculo",vehicle)
	
	finalSolution=[] #para guardar la solucion final
	for x in vehicle: #

			   
		g[x , ()] = matrix[clientes[x]-1][0]

	VehicleClients=tuple(vehicle)    
	#claves=tuple(clientes.keys()) 
		 
	distance=get_minimum(1, VehicleClients)

	
		
	#print('\n\nSolution to TSP: {1, ', end='')
	solution = p.pop()
	
	
	finalSolution.append(1)
	#print(solution[1][0], end=', ')
	finalSolution.append(solution[1][0])

	for x in range(len(vehicle) - 1):
		for new_solution in 	p:
			if tuple(solution[1]) == new_solution[0]:
				solution = new_solution
				#print(solution[1][0], end=', ')
				finalSolution.append(solution[1][0])
				break
	#finalSolution.append(1)
		   
	#print('1}')
	
	return finalSolution,distance


def get_minimum(k, a): #calcula camino mínimo entre el nodo k y el set de nodos a
	#print("---------------------------------------------------------------------------------------------------------------------------------------------------")


	if (k, a) in g:
		#print("k,a se encuentran en g",k,a)

		# Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
		return g[k, a]

	#else:

	#   print("como no se encontro hacemos el procedimiento para",k,a)
	values=[]
	all_min=[]


	for j in a: #j es el valor de cada cliente y a es el valor de cada sub ruta
		
		
		comunaJ=clientes[j]
		comunaK=clientes[k]
#       print("entrando con k",k," y j",j)
#       print("para ",j,"en ",a)
		set_a = copy.deepcopy(list(a))  
				 
		set_a.remove(j)
#       print("set a =",set_a) 
		all_min.append([j, tuple(set_a)])
#       print("all_min=j,set_a",all_min)
#       print("result= get_min",j,tuple(set_a))
		result = get_minimum(j, tuple(set_a))
#       print("result=",result)
		
#       print("values",values)
#       print("k vale",k)
		values.append(matrix[comunaK-1][comunaJ-1] + result)#costo de ir desde k a j + la distancia más corta en ir a j y pasar por el anterior set_a
		
#       print("matrix",matrix[comunaK-1][comunaJ-1])
#       print("values.append matrix[",comunaK,"-1][",comunaJ,"-1]",)
#       print("values",values)

	# get minimun value from set as optimal solution for

	#print("k,a",k,a)
	#print("g vale",g)  
	g[k, a] = min(values)
#	print(p)
	p.append(((k, a), all_min[values.index(g[k, a])]))
	#print("pppppppppppppppppppppppppppppppppppppp",p)
#	print(p)

	return g[k, a]



		



if __name__ == '__main__':

	# clientes=(2,3,4)
	
	clientes={1:1}
	continuar=1
	vehicles=[[],[],[]]
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
			for i,v in enumerate(vehicles):
			#	print("entrando con i y v",i,v)
				v.append(idd)
			#	print("añado",idd)
				ruta=tsp(tuple(v))
				distance=ruta[1]
			#	print("la ruta es",ruta[0])
			#	print("distancia y distancia minima",distance,distanceMin)
				if(i==0):
			#		print("como es la primera distancia")
					distanceMin=distance
					aux=i

					
				elif(distance<distanceMin):
			#		print("distance menor distance min",distance,distanceMin)
			#		print("elimino de",vehicles[aux],"el valor",idd)
					vehicles[aux].remove(idd)
			#		print("vehicle[aux queda",vehicle[aux] )
					aux=i		

				elif(distance>=distanceMin):
			#		print("como distancia min es mayor que distancia elimino de ",v,idd)
					v.remove(idd)	
			#		print("quedando",v)
			#		print("vehicle i",vehicles[i])


				g = {}
				p = [] 

			print("se agrego el cliente",idd,"al vehículo",aux+1)	
			
		#i=vehicles[0]    
		#distance1=tsp(tuple(i))
			#print("distancia",distance1)
	#	print(vehicles)	

		print("agregar otro?")
		continuar=int(input())


	#print(vehicles)

	for i,v in enumerate(vehicles):

	#	print("haciendo tsp a",v)

		ruta=tsp(tuple(v))
		vehicles[i] =ruta[0]
		vehicles[i].remove(1)
	#	print("la ruta queda",vehicles[i])



	print("la ruta óptima para tus vehículos es",vehicles)	
	
	
	
	
	