    
import sys
import copy
"""
matrix = [
            [0,          0.268188,   1.0861600,  0.284266,  2.1870300, 2.90507,  1.06443,    0.641625,   0.191624, 3.44142],
            [0.1609330,      0,      0.6911510,  0.464564,  1.4049800, 1.96431,  0.168696,   0.654258,   1.41509,  2.98196],
            [0.3580770,  0.379707,       0,      1.249930,  0.0821726, 0.408356, 1.74232,    2.37079,    2.95341,  3.90037],
            [0.0818823,  0.223001,   1.0921200,     0,      2.1872100, 2.89526,  0.942284,   0.56915,    0.872503, 2.75427],
            [0.3714430,  0.397651,   0.0423335,  1.289620,      0,     0.315516, 1.82914,    2.46966,    3.06793,  3.87276],
            [0.4166200,  0.46945,    0.1776410,  1.441470,  0.2664210,      0,   2.15881,    2.82956,    3.44337,  3.90929],
            [0.1427810,  0.0377101,  0.7089300,  0.438806,  1.4446600, 2.01924,     0,       0.526249,   1.24782,  3.13342],
            [0.0799607,  0.135875,   0.8962080,  0.246239,  1.8121500, 2.45884,  0.488912,       0,      0.76215,  3.14592],
            [0.0228630,  0.281361,   1.0688800,  0.361399,  2.1552200, 2.86474,  1.10989,    0.729676,       0,    3.6366 ],
            [0.4020280,  0.580519,   1.3821200,  1.117020,  2.6638000, 3.18444,  2.72886,    2.94897,    3.56066,        0],
]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


    
matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
data = [1, 2, 3, 4]

n = len(data)
all_sets = []
g = {}
p = []
finalSolution=[]
    


def get_minimum(k, a):
    print("----------------------------------------------------------------------")
    print("valor de g",g)
    if (k, a) in g:
        print(k,a,"estan en g=",g)
        print("retornar g[k, a]=",g[k, a])
        
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]


    values = []
    all_min = []
    for j in a:
        print("entrando con k",k," y j",j)
        print("para ",j,"en ",a)
        set_a = copy.deepcopy(list(a))  
        print("set a =",set_a)      
        set_a.remove(j)
        print("remuevo ",j,"de set_a")
        all_min.append([j, tuple(set_a)])
        print("agrego a all_min el valor", j, "y el set a como tupla")
        print("por lo tanto el valor all_min queda como",all_min)
        print("hacemos recursión en la función y la igualamos al resultado ",j,tuple(set_a))
        result = get_minimum(j, tuple(set_a))
        print("para ver cuando se llega acá",result)
        values.append(matrix[k-1][j-1] + result)
        print(" hasta acá k y j valen",k,j,"y all_min",all_min)
        print("se agrega a values la matriz [k-1][j-1] + result cuyo valores son matriz:",matrix[k-1][j-1] ,result)
        print("por lo tanto values queda con",values)

    # get minimun value from set as optimal solution for
    print("g=",g,"a=",a)
    print("salimos del for e igualamos  g[k, a]  al valor minimo de values que es",min(values))
    g[k, a] = min(values)

    print("agregamos a p ((k, a), all_min[values.index(g[k, a])])")
    p.append(((k, a), all_min[values.index(g[k, a])]))
    print("p es igual",p)

    return g[k, a]


if __name__ == '__main__':
    
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]     
        

    get_minimum(1, (2,3,4))

    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    finalSolution.append(solution[1][0])
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                finalSolution.append(solution[1][0])
                break
    print('1}')

    print (finalSolution)

