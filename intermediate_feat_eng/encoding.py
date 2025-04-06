def one_hot_encode(categories):
    """Convert a list of categorical values to one-hot encoding."""
    if not categories:
        return []
    unique = sorted(set(categories))
    encoding = {val: [1 if i == idx else 0 for i in range(len(unique))] for idx, val in enumerate(unique)}
    return [encoding[cat] for cat in categories]