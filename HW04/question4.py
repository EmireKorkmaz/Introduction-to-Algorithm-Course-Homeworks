def func(people, pairs):
	know = 0
	doesntknow = 0
	invited = ["" for i in range(len(people))]
	i = 0
	for p in people:
		for a,b in pairs:
			if(a==p):
				know = know +1
			elif(a!=p):
				doesntknow = doesntknow + 1
		if(doesntknow >= 5 and know >=5 and i<len(people)):
			print(i)
			invited[i] = p
			i = i+1
	print(invited)
	
liste = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
pairs= (("a","b"), ("a", "f"), ("a", "g"), ("b", "a"), ("b", "h"), ("b", "i"), ("b", "c"), ("b", "k"), ("b", "l"), ("b","m"))

func(liste, pairs)