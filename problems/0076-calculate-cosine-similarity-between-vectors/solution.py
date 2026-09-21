import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	
	dot_product = np.sum(v1 * v2)
	mag_v1 = np.sqrt(np.sum(v1 * v1))
	mag_v2 = np.sqrt(np.sum(v2 * v2))
	return dot_product / (mag_v1 * mag_v2)