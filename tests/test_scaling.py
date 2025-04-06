import pytest
from intermediate_feat_eng.scaling import min_max_scale, standard_scale

def test_min_max_scale():
    assert min_max_scale([1, 2, 3]) == [0.0, 0.5, 1.0]
    assert min_max_scale([]) == []
    assert min_max_scale([5, 5, 5]) == [0, 0, 0]

def test_standard_scale():
    result = standard_scale([1, 2, 3])
    assert abs(sum(result)) < 1e-10  # Mean ≈ 0
    assert abs(sum(x ** 2 for x in result) / len(result) - 1) < 1e-10  # Std ≈ 1
    assert standard_scale([]) == []