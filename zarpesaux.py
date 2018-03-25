


def solve_tsp_dynamic(points):
    #calc all lengths
    all_distances = [[length(x,y) for y in points] for x in points]
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]


if __name__ == '__main__':


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

    solve_tsp_dynamic(matrix)