import pytest
from common.system_analyser.memomry_byte_scaling import get_size


def test_get_size():
    assert get_size(2096) is not None
