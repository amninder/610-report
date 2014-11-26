import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.mlab as mlab
import numpy as np
import time
from random import randint
import math
import scipy.stats as norm


def plotPrimeRange():
	r = []
	r.append([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
	r.append([0.002665239, 0.00254972, 0.002649738, 0.002520612, 0.002680297, 0.002727096, 0.002605132, 0.002670949, 0.002741469, 0.002747976])
	r.append([0.497518499, 0.495699847, 0.495101886, 0.507682351, 0.494035418, 0.49020414, 0.501864704, 0.492039917, 0.499069543, 0.500872781])
	print r
	plt.plot(r[0], r[1], marker="o")
	plt.plot(r[0], r[2], linestyle='--', marker="x")
	plt.legend(["Websocket", "Ajax"])
	# plt.xticks(np.arange(min(r[0], max(r[0]), 1.0)))
	plt.ylabel('Milliseconds')
	plt.xlabel('Sets of requests')
	pp = PdfPages('ajax_websocket.pdf')
	plt.savefig(pp, format='pdf')
	pp.close()
	# plt.show()


def normal_dist_test():
	mean = 0
	variance = 1
	sigma = math.sqrt(variance)
	x = np.linspace(-3, 3, 100)
	plt.plot(x, mlab.normpdf(x, mean, sigma))
	plt.show()

def normal_dist():
	# h = [0.002665239, 0.00254972, 0.002649738, 0.002520612, 0.002680297, 0.002727096, 0.002605132, 0.002670949, 0.002741469, 0.002747976]
	h = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
	file_names = ["lp/data_10.txt", "lp/data_20.txt", "lp/data_30.txt", "lp/data_40.txt", "lp/data_50.txt", "lp/data_60.txt", "lp/data_70.txt", "lp/data_80.txt", "lp/data_90.txt", "lp/data_100.txt"]
	websocket_file_names = ["lp/websocket/data_10.txt", "lp/websocket/data_20.txt", "lp/websocket/data_30.txt", "lp/websocket/data_40.txt", "lp/websocket/data_50.txt", "lp/websocket/data_60.txt", "lp/websocket/data_70.txt", "lp/websocket/data_80.txt", "lp/websocket/data_90.txt", "lp/websocket/data_100.txt"]
	data = []
	for file_name in websocket_file_names:
		with open(file_name, "r") as f:
			for line in f:
				data.append(float(line[:-1]))
	h = data
	print "{}".format(len(h))
	h.sort()
	hmean = np.mean(h)
	hstd = np.std(h)
	pdf = norm.norm.pdf(h, hmean, hstd)
	print min(pdf)
	plt.plot(h, pdf)
	# plt.plot((0.49, 0.49), (0, 1.4), linestyle="--")
	plt.plot((0.0026, 0.0026), (0, 255), linestyle="--")
	# plt.axis([0, 1, 0, 5])
	# ajax axis
	# plt.xlim(0, 1)
	# plt.ylim(0.3, 1.4)
	plt.xlim(0, 0.0053)
	plt.ylim(64, 250)
	# plt.show()
	# plt.hist(h, normed=True)
	pp = PdfPages('websocket_normal.pdf')
	plt.savefig(pp, format='pdf')
	pp.close()

def find_mean():
	file_names = ["lp/data_10.txt", "lp/data_20.txt", "lp/data_30.txt", "lp/data_40.txt", "lp/data_50.txt", "lp/data_60.txt", "lp/data_70.txt", "lp/data_80.txt", "lp/data_90.txt", "lp/data_100.txt"]
	websocket_file_names = ["lp/websocket/data_10.txt", "lp/websocket/data_20.txt", "lp/websocket/data_30.txt", "lp/websocket/data_40.txt", "lp/websocket/data_50.txt", "lp/websocket/data_60.txt", "lp/websocket/data_70.txt", "lp/websocket/data_80.txt", "lp/websocket/data_90.txt", "lp/websocket/data_100.txt"]
	data = []
	for file_name in file_names:
		with open(file_name, "r") as f:
			for line in f:
				data.append(float(line[:-1]))

	mean = np.mean(data)
	std = np.std(data)
	print "Mean: {}".format(mean)
	print "Standard Deviation: {}".format(std)
	print "value range: {}".format(mean + math.sqrt((mean-std)**2))

find_mean()

