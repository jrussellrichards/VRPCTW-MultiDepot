import sys
import copy
import os
import json

matrices = json.loads(open('matrixZarpes.json').read())
matrixComuna = matrices["adjacency"]
matrix = matrices["distances"]


# guarda la distancia mínima entre rutas ej: (1,(2,3,4)):3 , el valor
# mínimo desde ir de 1 y pasar por 2 3 y 4
g = {}
p = []  # guarda las rutas óptimas
# datos para ruteo


class client:

	def __init__(self, code, destino):
		self.code = code
		self.destino = destino


class vehicle:

	def __init__(self, code):
		self.code = code
		self.capacity = 8
		self.avaible = True
		self.route = []
		self.distance_route = 0

	def cost_add(self,client):#Revisar esto

		route_aux = copy.copy(self.route)
		route_aux_2 = copy.copy(self.route)
		route_aux_2.append(client)
		distance_route_aux = tsp(route_aux)[1]
		distance_route_aux_2 = tsp(route_aux_2)[1]
		cost = distance_route_aux_2 - distance_route_aux
		return cost

	def add_client(self,client):
		self.route.append(client)
		self.capacity = self.capacity - 1
		self.distance_route = tsp(self.route)[1]
		self.route = tsp(self.route)[0]

	def remove_client(self,client):
		if(client not in self.route):
			print("el cliente no esta en este vehiculo")
		else:
			clients.remove(self.route)
			distance_route = tsp(self.route)[1]


class deposito():

	def __init__(self, capacity):
		self.capacity = capacity
		self.lugares = []

	def view_depot(self):
		for v in self.lugares:
			print("Vehículo ", v.code, ":")
			for c in v.route:
				print(c)

	def add_vehicle(self,v):
		if(len(self.lugares) == 5):
			print("no hay espacio disponible")
		else:
			print("se agregó el vehículo",v)
			self.lugares.append(v)

	def remove_vehicle(self,v):
		if(v not in lugares):
			print("el vehiculo no esta en el deposito")
		else:
			lugares.remove(v)

	def add_cliente(self,id_cliente):
		if(self.lugares[0].route==[]):
			self.lugares[0].add_client(id_cliente)
		else:
			best_vehicle = min(self.lugares, key=lambda x: x.cost_add(id_cliente))
			best_vehicle.add_client(id_cliente)


def tsp(vehicle):  # el algoritmo tsp recibe una ruta en forma de tupla
	#   print("calculando para el vehiculo",vehicle)

	finalSolution = []  # para guardar la solucion final
	for x in vehicle:
		g[x, ()] = matrix[x.destino - 1][0]

	VehicleClients = tuple(vehicle)

	distance = get_minimum(1, VehicleClients)

	solution = p.pop()

	finalSolution.append(1)

	finalSolution.append(solution[1][0])

	for x in range(len(vehicle) - 1):
		for new_solution in p:
			if tuple(solution[1]) == new_solution[0]:
				solution = new_solution
				# print(solution[1][0], end=', ')
				finalSolution.append(solution[1][0])
				break

	return finalSolution, distance


def get_minimum(k, a):  # calcula camino mínimo entre el nodo k y el set de nodos a

	if (k, a) in g:

		# Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
		return g[k, a]

	values = []
	all_min = []

	for j in a:  # j es el valor de cada cliente y a es el valor de cada sub ruta
		print("j,a",j,a)
		comunaJ = j.destino
		comunaK = a.destino

		set_a = copy.deepcopy(list(a))

		set_a.remove(j)

		all_min.append([j, tuple(set_a)])

		result = get_minimum(j, tuple(set_a))

		# costo de ir desde k a j + la distancia más corta en ir a j y pasar
		# por el anterior set_a
		values.append(matrix[comunaK - 1][comunaJ - 1] + result)

	g[k, a] = min(values)
	p.append(((k, a), all_min[values.index(g[k, a])]))

	return g[k, a]


if __name__ == '__main__':

	continuar = 1
	depot = deposito(5)
	while(continuar != 0):

		print("¿Que desea hacer?")
		print("1: Ingresar cliente")
		print("2: Ingresar vehiculo")
		print("3: Quitar vehiculo")
		print("4: Quitar cliente")
		print("5: Ver depósito")
		print("0: Salir")
		opcion = int(input())

		if(opcion == 1):
			print("Ingrese codigo cliente")
			idd = input()
			print("Ingrese comuna destino")
			destino = int(input())
			cliente=client(idd,destino)
			depot.add_cliente(cliente)


		if(opcion == 2):
			print("Ingrese id vehículo")
			idd = input()
			v=copy.copy(vehicle(idd))
			depot.add_vehicle(v)

		if(opcion == 3):
			print("Ingrese id vehículo")
			idd = int(input())
			depot.remove_vehicle(idd)

		if(opcion == 4):
			print("¿En que vehículo está el cliente?")
			v = int(input())
			print("¿Cuál es el id del cliente?")
			idd = int(input())
			v.remove_client(idd)
		if(opcion==5):
			depot.view_depot()




		if(opcion == str(0)):
			break
		
