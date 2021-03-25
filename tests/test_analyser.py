import pytest


def get_size(num):
    return num


def test_get_size():
    assert get_size(2096) is not None
