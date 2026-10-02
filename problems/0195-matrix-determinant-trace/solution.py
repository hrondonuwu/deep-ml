import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	matrix = np.array(matrix, dtype=np.float32)
	n = matrix.shape[0]
	trace = 0
	for i in range (n):
		trace += matrix[i, i]

	A = matrix.copy()
	det = 1

	for i in range (n):
		pivot = A[i, i]
		if pivot == 0:
			for j in range (i + 1, n):
				if A[j, i] != 0:
					A[[i, j]] = A[[j, i]]
					det *= -1
					break
			else:
				return (0.0, trace)
			pivot = A[i, i]

		det *= pivot
		for j in range (i + 1, n):
			A[j] = A[j] - (A[j, i] / pivot) * A[i]

	return (det, trace)