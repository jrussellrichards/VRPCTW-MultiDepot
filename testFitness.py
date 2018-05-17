import random
import json
import re
import copy
from time import time
import os


if __name__ == "__main__":

	demandas = json.loads(open('customCustomers.json').read())
	problem = json.loads(open('customProblem.json').read())
	distances= problem["distance_matrix"]
	cantidadvehiculo=problem["max_vehicle_number"]
	capacidadvehiculo=problem["vehicle_capacity"]   

	distancia_ruta_1=distances[0][43]+distances[43][44]+distances[44][28]+distances[28][33]+distances[33][29]+distances[30][27]+distances[27][6]+distances[7][5]+distances[5][7]+distances[7][35]+distances[35][3]+distances[3][4]+distances[4][14]+distances[14][13]+distances[13][12]+distances[11][18]+distances[18][17]+distances[17][10]
	distancia_ruta_2=distances[0][42]+distances[42][30]+distances[30][41]+distances[41][32]+distances[32][31]+distances[31][34]+distances[34][40]+distances[40][39]+distances[39][36]+distances[36][38]+distances[38][37]
	distancia_ruta_3=distances[0][24]+distances[24][9]+distances[9][15]+distances[15][1]+distances[1][2]+distances[2][16]
	distancia_ruta_4=distances[0][20]+distances[20][21]+distances[21][25]+distances[25][26]+distances[26][23]+distances[23][22]+distances[22][19]+distances[19][8]
	print("distancia ruta 1=",distancia_ruta_1+distancia_ruta_2+distancia_ruta_3+distancia_ruta_4)