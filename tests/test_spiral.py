#!/usr/bin/env python

from spiral import calc


def test_one():
    assert calc(1) == (0, 0)


def test_two():
    assert calc(2) == (0, 1)


def test_three():
    assert calc(3) == (1, 1)


def test_four():
    assert calc(4) == (1, 0)


def test_five():
    assert calc(5) == (1, -1)


def test_rest():
    results = [
        (6, (0, -1)),
        (7, (-1, -1)),
        (8, (-1, 0)),
        (9, (-1, 1)),
        (10, (-1, 2)),
        (11, (0, 2)),
        (12, (1, 2)),
        (13, (2, 2)),
        (14, (2, 1)),
        (15, (2, 0)),
        (16, (2, -1)),
        (17, (2, -2)),
        (18, (1, -2)),
        (19, (0, -2)),
        (20, (-1, -2)),
        (21, (-2, -2)),
        (22, (-2, -1)),
        (23, (-2, 0)),
        (24, (-2, 1)),
        (25, (-2, 2)),
        (26, (-2, 3)),
        (27, (-1, 3)),
    ]

    r = [calc(i) == cord for i, cord in results]
    assert all(r)
