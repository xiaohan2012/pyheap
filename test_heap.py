import pytest
from heap import build_heap, heap
from copy import copy


@pytest.fixture
def hp():
    keys = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    return build_heap(keys)


def _test_e2i(hp):
    for i in range(hp.size):
        assert hp.e2i[hp.es[i]] == i


def _test_heap_property(hp):
    for i in range(1, hp.size):
        assert hp.keys[hp.parent(i)] > hp.keys[i]
        # assert hp.es[hp.parent(i)] > hp.es[i]


def _test_basic(hp):
    _test_e2i(hp)
    _test_heap_property(hp)

    
def test_build_heap(hp):
    _test_basic(hp)


def test_pop_max(hp):
    i = 0
    keys = list(sorted(copy(hp.keys), reverse=True))
    while hp.size > 0:
        k, e = hp.pop_max()
        assert keys[i] == k
        assert keys[i] == e
        i += 1

    assert e not in hp.e2i
    _test_basic(hp)


def test_insert(hp):
    keys = copy(hp.keys)
    new_hp = heap([], [])
    for k in keys:
        new_hp.insert(k, k)

    assert new_hp.keys == hp.keys

    _test_basic(hp)


def test_increase_key(hp):
    hp.increase_key(1, 20)
    assert hp.peep_max() == (20, 1)
    assert hp.e2i[1] == 0

    _test_basic(hp)
    

def test_decrease_key(hp):
    hp.decrease_key(16, 0)
    assert hp.peep_max() == (14, 14)

    _test_basic(hp)


def test_update_key(hp):
    hp.update_key(16, 0)
    assert hp.peep_max() == (14, 14)

    hp.increase_key(1, 20)
    assert hp.peep_max() == (20, 1)

    _test_basic(hp)
