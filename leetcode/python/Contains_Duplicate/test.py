from solution import contains_duplicate


def test_empty_array():
    assert contains_duplicate([]) is False


def test_single_element():
    assert contains_duplicate([5]) is False


def test_example1():
    assert contains_duplicate([1, 2, 3, 3]) is True


def test_example2():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_duplicate_at_beginning():
    assert contains_duplicate([1, 1, 2, 3]) is True


def test_duplicate_in_middle():
    assert contains_duplicate([1, 2, 2, 3]) is True


def test_all_duplicates():
    assert contains_duplicate([7, 7, 7, 7]) is True


def test_negative_numbers():
    assert contains_duplicate([-1, -2, -3, -1]) is True


def test_mixed_numbers():
    assert contains_duplicate([-1, 2, 3, -1]) is True


def test_boundary_values():
    assert contains_duplicate([1000000000, -1000000000]) is False


def test_boundary_duplicate():
    assert contains_duplicate([1000000000, -1000000000, 1000000000]) is True