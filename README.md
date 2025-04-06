# Intermediate Feature Engineering
A Python package for scaling and encoding features.

## Installation
pip install intermediate-feat-eng

## Usage
from intermediatefeateng import min_max_scale, standard_scale, one_hot_encode

# Scaling
print(min_max_scale([1, 2, 3]))  # [0.0, 0.5, 1.0]
print(standard_scale([1, 2, 3]))  # ≈ [-1.0, 0.0, 1.0]

# Encoding
print(one_hot_encode(["cat", "dog", "cat"]))  # [[1, 0], [0, 1], [1, 0]]
