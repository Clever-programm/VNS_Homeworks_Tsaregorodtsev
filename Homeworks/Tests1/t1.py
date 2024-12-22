import pytest

from Homeworks.Lesson1.hw1 import pull


@pytest.mark.parametrize(
    "input_n,expected",
    [
        (0, (0, 0)),
        (10, (1, 0)),
        (20, (2, 0)),
        (29, (2, 0)),
        (30, (3, 0)),
        (31, (3, 0)),
        (39, (3, 0)),
        (80, (8, 0)),
        (89, (8, 0)),
        (90, (8, 1)),
        (91, (9, 1)),
        (100, (9, 1)),
        (101, (10, 1)),
        (180, (17, 2)),
        (181, (18, 2)),
        (1080, (107, 12)),
        (1081, (108, 12)),
        (2150, (214, 23)),
        (2151, (215, 23)),
        (2152, (215, 23)),
        (2158, (215, 23)),
        (2160, (215, 24)),
        (2161, (216, 24)),
    ],
)
def test_pull(input_n, expected):
    assert pull(input_n) == expected