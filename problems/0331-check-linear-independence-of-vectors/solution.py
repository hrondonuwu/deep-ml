import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    A = A.astype(float).copy()

    if A.size == 0: return 0
    rows = A.shape[0]
    cols = A.shape[1]

    
    row_pivot = 0
    for c in range (cols):
        if row_pivot >= rows:
            break
        pivot_row = None

        for r in range(row_pivot, rows):
            if abs(A[r, c]) > tol:
                pivot_row = r
                break

        if pivot_row is None:
            continue

        A[[row_pivot, pivot_row]] = A[[pivot_row, row_pivot]]

        pivot = A[row_pivot, c]

        for r in range (row_pivot + 1, rows):
            A[r] -= A[row_pivot] * (A[r, c] / pivot)

        row_pivot += 1

    return row_pivot

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Your code here
    return matrix_rank(np.array(vectors)) == len(vectors)