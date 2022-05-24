"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])



@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))



def test_daily_max():
    """" Test that max function works on a 2D array and returns 1D array
    """
    from inflammation.models import daily_max

    test_input = np.array([[1, 2],
                           [5, 7],
                           [3, 4]])
    test_result = np.array([5, 7])

    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min():
    """" Test that min function works on a 2D array and returns 1D array
    """
    from inflammation.models import daily_min

    test_input = np.array([[1, 2],
                           [5, 7],
                           [3, 4]])
    test_result = np.array([1, 2])

    npt.assert_array_equal(daily_min(test_input), test_result)