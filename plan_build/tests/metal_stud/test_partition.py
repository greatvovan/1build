import pytest
from ...metal_stud.partition import plan, MaterialsList


def test_validation():
    with pytest.raises(ValueError):
        plan(-1.0)

    with pytest.raises(ValueError):
        plan(0)

    with pytest.raises(ValueError):
        plan(0.1)


def test_positive():
    assert plan(1.0) == MaterialsList(0.2, 2, 0.5, 2, 2, 14, 36)
    assert plan(2.0) == MaterialsList(0.4, 2, 1.0, 3, 3, 14, 36)
    assert plan(3.0) == MaterialsList(0.6, 3, 1.5, 3, 3, 14, 54)
    assert plan(4.0) == MaterialsList(0.8, 3, 2.0, 4, 4, 14, 54)
    assert plan(5.1) == MaterialsList(1.02, 4, 2.55, 5, 5, 14, 90)
