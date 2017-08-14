import urllib2
import numpy as np
import matplotlib.pyplot as pl

class LossData:

	# entry of GetContainerHost is SVM.scala
	containerhostpath = "/home/hadoop0master/workspace/Git/Benchmark/ForkedSparkBench/spark-bench/SVM/LogAnalysis/SVMCH"
	containerId = ""
	hostname = ""
	
	pageport = ":8042"
	pagehead = "http://"
	pagemiddle = "/node/containerlogs/"
	pagerear = "/hadoop0master/stdout/?start=0"
	pagestring = ""
	page = ""

	Xdata = []
	Ydata = []

	goal = 124261.05126729673
	Ygoal = []

	def __init__(self):
		self.loadpage()
		self.loaddata()

	def loadpage(self):
		try:
			containerhostfile = open(self.containerhostpath)
			firstline = containerhostfile.readline()
			self.containerId = firstline.split(" ")[0]
			self.hostname = firstline.split(" ")[1]
			self.pagestring = self.pagehead + self.hostname + self.pageport + self.pagemiddle + self.containerId + self.pagerear
			print self.pagestring
			self.page = urllib2.urlopen(self.pagestring, timeout=10)
			containerhostfile.close()
		except IOError as error:
			print ("file open error: " + str(error))
			return 0

	def loaddata(self):
		lines = self.page.read().splitlines()
		for line in lines:
			splitedline = line.split("=")
			if len(splitedline) == 2:
				if splitedline[0].strip() == "TotalLoss":
					self.Ydata.append(float(splitedline[1].strip()))
					self.Ygoal.append(self.goal)
				if splitedline[0].strip() == "Iteration Time":
					self.Xdata.append(float(splitedline[1].strip()))

	def draw(self):
		pl.figure()
		#pl.plot(self.Xdata, self.Ygoal, '-r')
		pl.plot(self.Xdata, self.Ydata, '-o')
		pl.show()

if __name__ == "__main__":
	lossdata = LossData()
	lossdata.draw()
