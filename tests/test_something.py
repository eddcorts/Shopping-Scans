import pytest


@pytest.fixture
def example_data() -> int:
    return 3


def test_example(example_data: int) -> None:
    data = 3
    assert data == example_data
