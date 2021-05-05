#!/usr/bin/env python

from math import ceil, sqrt
from collections import namedtuple

Point = namedtuple("Point", "x y")


def get_square(j):
    return ceil(sqrt(j) / 2)


def get_anchor(j):
    square = get_square(j)
    return ((square - 1) * 2) ** 2 + 1


def get_side_length(j):
    square = get_square(j)
    return square * 2 - 1


def get_normalised_j(j):
    anchor = get_anchor(j)
    return j - anchor


def get_side(j):
    return get_normalised_j(j) // get_side_length(j)


def get_position_on_side(j):
    return get_normalised_j(j) % get_side_length(j)


def get_square_anchor_point(j):
    square = get_square(j)
    return Point((square - 1), -(square - 1))


def get_side_anchor_point(j):
    side_anchor = get_square_anchor_point(j)
    side = get_side(j)
    side_length = get_side_length(j)

    if side == 0:
        return side_anchor
    if side == 1:
        return Point(side_anchor.x - side_length + 1, side_anchor.y + 1)
    if side == 2:
        return Point(side_anchor.x - side_length + 2, side_anchor.y + side_length)
    # side == 3
    return Point(side_anchor.x + 1, side_anchor.y + side_length - 1)


def calc(i):
    point_translations = [
        lambda dist: Point(-1 * dist, 0),
        lambda dist: Point(0, 1 * dist),
        lambda dist: Point(1 * dist, 0),
        lambda dist: Point(0, -1 * dist),
    ]

    side_anchor_point = get_side_anchor_point(i)
    position = get_position_on_side(i)
    translation = point_translations[get_side(i)](position)
    return (side_anchor_point.x + translation.x, side_anchor_point.y + translation.y)
