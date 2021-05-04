#!/usr/bin/env python

from spiral import (
    get_square,
    get_anchor,
    get_side,
    get_position_on_side,
    get_side_anchor_point,
    get_square_anchor_point,
)


def test_get_square():
    assert get_square(1) == 1
    assert get_square(2) == 1
    assert get_square(3) == 1
    assert get_square(4) == 1
    assert get_square(5) == 2
    assert get_square(13) == 2
    assert get_square(16) == 2
    assert get_square(17) == 3
    assert get_square(35) == 3
    assert get_square(36) == 3
    assert get_square(37) == 4


def test_get_anchor():
    assert get_anchor(1) == 1
    assert get_anchor(4) == 1
    assert get_anchor(5) == 5
    assert get_anchor(13) == 5
    assert get_anchor(16) == 5
    assert get_anchor(17) == 17
    assert get_anchor(36) == 17
    assert get_anchor(37) == 37


def test_get_side():
    assert get_side(1) == 0
    assert get_side(2) == 1
    assert get_side(3) == 2
    assert get_side(4) == 3
    assert get_side(5) == 0
    assert get_side(6) == 0
    assert get_side(7) == 0
    assert get_side(8) == 1
    assert get_side(9) == 1
    assert get_side(10) == 1
    assert get_side(11) == 2
    assert get_side(14) == 3
    assert get_side(16) == 3

    assert get_side(17) == 0
    assert get_side(21) == 0
    assert get_side(22) == 1
    assert get_side(28) == 2
    assert get_side(32) == 3
    assert get_side(36) == 3


def test_get_position_on_side():
    assert get_position_on_side(1) == 0
    assert get_position_on_side(2) == 0
    assert get_position_on_side(3) == 0
    assert get_position_on_side(4) == 0
    assert get_position_on_side(5) == 0
    assert get_position_on_side(6) == 1
    assert get_position_on_side(7) == 2
    assert get_position_on_side(8) == 0


def test_get_side_anchor_point():
    assert get_side_anchor_point(1) == (0, 0)
    assert get_side_anchor_point(2) == (0, 1)
    assert get_side_anchor_point(3) == (1, 1)
    assert get_side_anchor_point(4) == (1, 0)

    assert get_side_anchor_point(5) == (1, -1)
    assert get_side_anchor_point(8) == (-1, 0)
    assert get_side_anchor_point(11) == (0, 2)
    assert get_side_anchor_point(14) == (2, 1)

    assert get_side_anchor_point(17) == (2, -2)
    assert get_side_anchor_point(22) == (-2, -1)
    assert get_side_anchor_point(27) == (-1, 3)
    assert get_side_anchor_point(32) == (3, 2)


def test_get_square_anchor_point():
    assert get_square_anchor_point(1) == (0, 0)
    assert get_square_anchor_point(5) == (1, -1)
    assert get_square_anchor_point(17) == (2, -2)
    assert get_square_anchor_point(37) == (3, -3)
