import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    
    a = np.array(a)
    a_t = a.flatten(order='F').reshape(a.shape[1], a.shape[0])

    return a_t