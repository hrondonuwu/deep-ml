def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	expected_value = (n + 1) / 2.0
	variance = (n * n - 1.0) / (12)
	return expected_value, variance