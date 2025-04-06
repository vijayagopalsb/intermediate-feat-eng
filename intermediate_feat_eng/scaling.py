def min_max_scale(data):
    """Scale a list of numbers to [0, 1]."""
    if not data:
        return []
    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        return [0] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def standard_scale(data):
    """Standardize data to mean=0, std=1."""
    if not data:
        return []
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std = variance ** 0.5 if variance > 0 else 1
    return [(x - mean) / std for x in data]