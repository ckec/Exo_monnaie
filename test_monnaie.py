import pytest

from monnaie import MAX, change


def test_raise_exception_when_inf_2():
    with pytest.raises(Exception):
        change(1)
    with pytest.raises(Exception):
        change(0)


def test_raise_exception_when_sup():
    with pytest.raises(Exception):
        change(MAX + 1)


def test_change_10():
    result = change(10)
    expected_result = {"two": 0, "five": 0, "ten": 1}
    assert expected_result == result


def test_change_5():
    result = change(5)
    expected_result = {"two": 0, "five": 1, "ten": 0}
    assert expected_result == result


def test_change_2():
    result = change(2)
    expected_result = {"two": 1, "five": 0, "ten": 0}
    assert expected_result == result


def test_change_3():
    result = change(3)
    expected_result = None
    assert expected_result == result


def test_change_4():
    result = change(4)
    expected_result = {"two": 2, "five": 0, "ten": 0}
    assert expected_result == result


def test_change_6():
    result = change(6)
    expected_result = {"two": 3, "five": 0, "ten": 0}
    assert expected_result == result


def test_change_7():
    result = change(7)
    expected_result = {"two": 1, "five": 1, "ten": 0}
    assert expected_result == result


def test_change_8():
    result = change(8)
    expected_result = {"two": 4, "five": 0, "ten": 0}
    assert expected_result == result


def test_change_9():
    result = change(9)
    expected_result = None
    assert expected_result == result


def test_change_11():
    result = change(11)
    expected_result = None
    assert expected_result == result


def test_change_12():
    result = change(12)
    expected_result = {"two": 1, "five": 0, "ten": 1}
    assert expected_result == result


def test_change_13():
    result = change(13)
    expected_result = None
    assert expected_result == result


def test_change_14():
    result = change(14)
    expected_result = {"two": 2, "five": 0, "ten": 1}
    assert expected_result == result


def test_change_15():
    result = change(15)
    expected_result = {"two": 0, "five": 1, "ten": 1}
    assert expected_result == result


def test_change_16():
    result = change(16)
    expected_result = {"two": 3, "five": 0, "ten": 1}
    assert expected_result == result


def test_change_17():
    result = change(17)
    expected_result = {"two": 1, "five": 1, "ten": 1}
    assert expected_result == result


def test_change_42():
    result = change(42)
    expected_result = {"two": 1, "five": 0, "ten": 4}
    assert expected_result == result


def test_change_96():
    result = change(96)
    expected_result = {"two": 3, "five": 0, "ten": 9}
    assert expected_result == result


def test_change_100():
    result = change(100)
    expected_result = {"two": 0, "five": 0, "ten": 10}
    assert expected_result == result


def test_change_max():
    result = change(MAX)
    expected_result = {"two": 1, "five": 1, "ten": 922337203685477580}
    assert expected_result == result
