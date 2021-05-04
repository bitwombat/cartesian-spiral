#!/usr/bin/env python

from spiral import which_square, which_anchor, which_side, which_slot, get_side_anchor, get_anchor_coord


def test_which_square():
    assert which_square(1) == 1
    assert which_square(2) == 1
    assert which_square(3) == 1
    assert which_square(4) == 1
    assert which_square(5) == 2
    assert which_square(13) == 2
    assert which_square(16) == 2
    assert which_square(17) == 3
    assert which_square(35) == 3
    assert which_square(36) == 3
    assert which_square(37) == 4


def test_get_anchor():
    assert which_anchor(1) == 1
    assert which_anchor(4) == 1
    assert which_anchor(5) == 5
    assert which_anchor(13) == 5
    assert which_anchor(16) == 5
    assert which_anchor(17) == 17
    assert which_anchor(36) == 17
    assert which_anchor(37) == 37


def test_which_side():
    assert which_side(1) == 0
    assert which_side(2) == 1
    assert which_side(3) == 2
    assert which_side(4) == 3
    assert which_side(5) == 0
    assert which_side(6) == 0
    assert which_side(7) == 0
    assert which_side(8) == 1
    assert which_side(9) == 1
    assert which_side(10) == 1
    assert which_side(11) == 2
    assert which_side(14) == 3
    assert which_side(16) == 3

    assert which_side(17) == 0
    assert which_side(21) == 0
    assert which_side(22) == 1
    assert which_side(28) == 2
    assert which_side(32) == 3
    assert which_side(36) == 3


def test_which_slot():
    assert which_slot(1) == 0
    assert which_slot(2) == 0
    assert which_slot(3) == 0
    assert which_slot(4) == 0
    assert which_slot(5) == 0
    assert which_slot(6) == 1
    assert which_slot(7) == 2
    assert which_slot(8) == 0


def test_get_side_anchor():
    assert get_side_anchor(1, 0) == (0, 0)
    assert get_side_anchor(1, 1) == (0, 1)
    assert get_side_anchor(1, 2) == (1, 1)
    assert get_side_anchor(1, 3) == (1, 0)

    assert get_side_anchor(2, 0) == (1, -1)
    assert get_side_anchor(2, 1) == (-1, 0)
    assert get_side_anchor(2, 2) == (0, 2)
    assert get_side_anchor(2, 3) == (2, 1)

    assert get_side_anchor(3, 0) == (2, -2)
    assert get_side_anchor(3, 1) == (-2, -1)
    assert get_side_anchor(3, 2) == (-1, 3)
    assert get_side_anchor(3, 3) == (3, 2)


def test_get_anchor_coord():
    assert get_anchor_coord(1) == (0, 0)
    assert get_anchor_coord(2) == (1, -1)
    assert get_anchor_coord(3) == (2, -2)
    assert get_anchor_coord(4) == (3, -3)
