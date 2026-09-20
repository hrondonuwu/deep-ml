import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) != len(b):
		return -1

	return (np.array(a) + np.array(b)).tolist()