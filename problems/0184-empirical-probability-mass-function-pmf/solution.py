def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    counts = {}
    total = len(samples)

    for sample in samples:
        counts[sample] = counts.get(sample, 0) + 1

    pmf = []
    for key, value in counts.items():
        pmf.append((key, value / total))

    return pmf