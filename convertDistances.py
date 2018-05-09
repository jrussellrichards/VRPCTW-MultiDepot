from scipy.spatial import distance
import json
import sys


if __name__ == "__main__":


	a = (1,2,3)
	b = (4,5,6)
	dst = distance.euclidean(a,b)
	