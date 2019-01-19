from nose.tools import assert_list_equal
import random
from bubble_sort import sort as bubble_sort
from merge_sort import merge_sort
from selection_sort import sort as selection_sort


def test_bubble():
    sorted_list = [i for i in range(2500)]

    unsorted = sorted_list.copy()
    random.shuffle(unsorted)
    bubble_sort(unsorted)

    assert_list_equal(sorted_list, unsorted)

    # wew, takes about a second


def test_merge():
    sorted_list = [i for i in range(19000)]

    unsorted = sorted_list.copy()
    random.shuffle(unsorted)

    assert_list_equal(sorted_list, merge_sort(unsorted))

    # still takes about a second but... is a bit faster, should probably use C...


def test_selection():
    sorted_list = [i for i in range(5000)]

    unsorted = sorted_list.copy()
    random.shuffle(unsorted)

    selection_sort(unsorted)

    assert_list_equal(sorted_list, unsorted)


def test_inbuilt():
    sorted_list = [i for i in range(850000)]

    unsorted = sorted_list.copy()
    random.shuffle(unsorted)

    unsorted.sort()
    assert_list_equal(sorted_list, unsorted)

    # i'm just going to leave sorting to the inbuilt bois
