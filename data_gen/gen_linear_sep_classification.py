import numpy as np
from random import randint
import matplotlib.pyplot as plt
import csv

# TODO: Currently the softness parameter does nothing - implement softness
def gen(data_size, m, c, scale_x=1000, scale_y=1000, margin = 1, softness=0):
	data = []
	print randint(0, 10)
	i = 0
	while i < data_size:
		y = ((np.random.normal() * scale_y) + c)/2
		x = ((np.random.normal() * scale_x) - (c/m))/2
		dist = (m*x + c - y) / np.sqrt(1+ (m*m))
		# print x, y, dist
		if (dist < margin) and (dist > -1*margin):
			print "in margin:", -1*margin, "<", dist, "<", margin
			continue
		elif dist >= margin:
			data.append((x, y, 1))
		elif dist <= -1 * margin:
			data.append((x, y, -1))
		else:
			print "ERROR: It is impossible to reach here"
		i += 1

	return data

def show(data):
	X1 = []
	X2 = []
	Y1 = []
	Y2 = []
	for indep, dep, category in data:
		if category == 1:
			X1.append(indep)
			Y1.append(dep)
		elif category == -1:
			X2.append(indep)
			Y2.append(dep)
	plt.plot(X1, Y1, 'ro')
	plt.plot(X2, Y2, 'b.')
	plt.show()

def genCSV(data, filename = ''):
    if filename == '':
        filename = "data_" + len(data) + ".csv"
    else:
        filename = filename+".csv"
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for indep, dep, category in data:
            writer.writerow([dep, indep, category])

def main():
	print "started"
	m = -3.5
	c = 7000
	margin = 20
	data_size = 1000
	softness = 2
	variance_measure = 200
	data = gen(data_size, m,c, variance_measure, variance_measure, margin, softness = softness)
	print len(data)
	show(data)
        
	# Naming convention: "classification_data_<Num of Points>_<m>_<c>_<data_size>_<margin>_<variance>"
	filename = "classification_data_"+str(len(data))+"_"+str(m)+"_"+str(c)+"_"+str(data_size)+"_"+str(margin)+"_"+str(variance_measure)
	genCSV(data, filename)


main()
