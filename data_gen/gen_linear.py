import numpy as np
from random import randint
import matplotlib.pyplot as plt
import csv

def gen(m, c, domain, density, var):
	data = []
	for x in xrange(0, domain):
		rep = randint(0,density)
		for j in xrange(0, rep):
			scale = randint(0, var)
			y = (m * x) + c + (scale * np.random.normal())
			data.append((x, y))
        return data

def show(data):
	X = []
	Y = []
	for dep, indep in data:
		X.append(dep)
		Y.append(indep)
	plt.plot(X, Y, 'ro')
	plt.show()

def genCSV(data, filename = ''):
    if filename == '':
        filename = "data_" + len(data) + ".csv"
    else:
        filename = filename+".csv"
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for dep, indep in data:
            writer.writerow([dep, indep])

def main():
	m = -3.5
	c = 7000
        domain = 1000
        density = 2
        variance_measure = 250
	data = gen(m, c, domain, density, variance_measure)
        print len(data)
	show(data)
        
        # Naming convention: "data_<Num of Points>_<m>_<c>_<x-range>_<density>_<variance>"
        filename = "data_"+str(len(data))+"_"+str(m)+"_"+str(c)+"_"+str(domain)+"_"+str(density)+"_"+str(variance_measure)
        genCSV(data, filename)


main()
