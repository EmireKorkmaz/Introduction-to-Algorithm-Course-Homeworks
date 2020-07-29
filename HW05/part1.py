
def question1(weight, time):
	array = [None] * len(weight)
	ratio = 0
	indices = [None] * len(weight)

	for i in range(len(weight)):
		ratio = weight[i] / time[i]
		array[i] = ratio

	dict = {}
	for i in range (len(array)):
		dict[str(i)] = [weight[i], time[i],array[i]]

	array.sort(reverse=True)
	newWeight = [None] * len(weight)
	newTime = [None] * len(time)
	size= len(weight)
	i=0
	j=0
	for i in range (len(array)):
		for j in range(len(newWeight)):
			if(array[i] == dict[str(j)][2]):
				newWeight[i] = dict[str(j)][0]
				newTime[i] = dict[str(j)][1]

	print("Weight : "+str(newWeight))
	print("Time : "+ str(newTime))
	time=0
	total = 0
	i=0
	for i in range(len(newWeight)):
		time = time + newTime[i]
		total = total + (time*newWeight[i])
	print("Ratio : "+ str(array))
	print('Weighted sum is '+str(total))


weight = [100,19,27,25,15,12,35,26]
time = [2,1,2,1,3,4,5,7]

question1(weight, time)