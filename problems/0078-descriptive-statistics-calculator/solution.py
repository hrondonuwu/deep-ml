import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    mean = np.mean(data)
    median = np.median(data)

    values, counts = np.unique(data, return_counts = True)
    mode = values[np.argmax(counts)]
    
    variance = np.mean(((data - mean) *( data - mean)))
    standard_deviation = np.sqrt(variance)

    quartiles = np.quantile(data, [0.25, 0.50, 0.75])
    interquartile_range = quartiles[2] - quartiles[0]

    return {
        "mean": mean,
        "median": median,
        "mode": mode,

        "variance": variance,
        "standard_deviation": standard_deviation,

        "25th_percentile": quartiles[0],
        "50th_percentile": quartiles[1],
        "75th_percentile": quartiles[2],
        "interquartile_range": interquartile_range
    }