def question2(NY, SF, M, n):
	optNY = [0] * len(NY)
	optSF = [0] * len(SF)
	i=1
	for i in range(n):
		optNY[i] = NY[i] + min(optNY[i-1], M+optSF[i-1])
		optSF[i] = SF[i] + min(optSF[i-1], M+optNY[i-1])

	print("Cost is "+str(min(optNY[n-1], optSF[n-1])))

NY = [1,3,20,30]
SF=[50,20,2,4]

M=10
n=4

question2(NY, SF, M, n)