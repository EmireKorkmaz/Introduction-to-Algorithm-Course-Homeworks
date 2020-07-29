def question1(hotels):
	bestpath = [0 for i in range(len(hotels))]
	stop = [0 for i in range(len(hotels))]

	for i in range (len(hotels)):
		bestpath[i] = (200 - hotels[i])**2
		stop[i] = 0
		for j in range(i):
			if (bestpath[j] + pow(200 - (hotels[i] - hotels[j]),2) < bestpath[i]):
				bestpath[i] = pow(200 - (hotels[i] - hotels[j]),2) +bestpath[j]
				stop[i] = j + 1

	print("Penalty is "+str(bestpath[len(hotels) - 1]))

	path = ""
	index = len(stop)-1
	while(index>=0):
		path = str((index+1))+ "   " +str(path)
		index = stop[index]-1

	print(stop)
	print("Stops are "+path)

A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]

question1(A)