from nose.tools import assert_list_equal
import random
from bubble_sort import sort


def test_bubble():
    sorted_list = [i for i in range(2500)]

    unsorted = sorted_list.copy()
    random.shuffle(unsorted)
    sort(unsorted)

    assert_list_equal(sorted_list, unsorted)

    # wew, takes about a second
