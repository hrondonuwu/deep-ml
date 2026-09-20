def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	sum = []
	if len(a) != len(b):
		return -1
	
	for i in range (len(a)):
		sum.append(a[i] + b[i])
	
	return sum