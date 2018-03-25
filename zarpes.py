import json

if __name__ == "__main__":

	clientes = json.loads(open('customers.json').read())
	problem = json.loads(open('problem.json').read())
	distances= problem["distance_matrix"]
	cantidadvehiculo=problem["max_vehicle_number"]
	capacidadvehiculo=problem["vehicle_capacity"]
	vehicle1=[]
	vehicle2=[]
	vehicle3=[]
	vehicle4=[]
	vehicle5=[]
	customer = {}
	distances=[0,0,0,0,0]
	
	Comunas = {0:'Quilicura',1:'Renca',2:'Maipu',3:'Conchali',4:'Las Condes',5:'San Bernardo',6:'Ñuñoa',7:'Cerro Navia',8:'La Cisterna'}

#Distance between each pair of cities

w0 = [0,1,2,1,2,4,2,3,1]
w1 = [0,0,2,1,2,3,2,3,3]
w2 = [0,1,0,1,2,1,2,3,1]
w3 = [0,1,2,0,2,2,2,3,2]
w4 = [0,5,2,1,0,4,2,3,4]
w5 = [0,1,3,1,2,0,2,3,5]
w6 = [2,3,2,1,2,2,0,3,1]
w7 = [0,1,2,1,2,1,2,0,1]
w8 = [2,2,2,1,2,1,2,3,0]
	

	print("Agregar cliente y destino")
	idd = input()
	destino= input()
	customer["idd"]=[destino]
	vehicle1.append(idd)
	continuar=input()

	while (continuar=="si"):		

		print("Ingrese el cliente y destino")
		idd = input()
		destino= input()
		customer["idd"]=[destino]


		vehicle1.append(idd)
		print("¿Desea agregar otro?")
		continuar=input()

	print("Buen viaje")



	
	


	





	


		



	

