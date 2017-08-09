import urllib2
import numpy as np
import matplotlib.pyplot as pl

page = urllib2.urlopen('http://hadoop1slave2:8042/node/containerlogs/container_1502248731564_0002_01_000001/hadoop0master/stdout/?start=0', timeout=10)
lines = page.read().splitlines()

Xdata = []
Ydata = []

for line in lines:
	splitedline = line.split("=")
	if len(splitedline) == 2:
		if splitedline[0].strip() == "TotalLoss":
			Ydata.append(float(splitedline[1].strip()))
		if splitedline[0].strip() == "Iteration Time":
			Xdata.append(float(splitedline[1].strip()))

pl.plot(Xdata, Ydata, '-o')
pl.show()
