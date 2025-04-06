import pytest
from intermediate_feat_eng.encoding import one_hot_encode

def test_one_hot_encode():
    assert one_hot_encode(["cat", "dog", "cat"]) == [[1, 0], [0, 1], [1, 0]]
    assert one_hot_encode([]) == []
    assert one_hot_encode(["a", "a"]) == [[1], [1]]