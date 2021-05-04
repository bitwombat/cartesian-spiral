#!/usr/bin/env python

from math import ceil, sqrt
from collections import namedtuple

Point = namedtuple("Point", "x y")

point_transforms = [
    lambda dist: Point(-1 * dist, 0),
    lambda dist: Point(0, 1 * dist),
    lambda dist: Point(1 * dist, 0),
    lambda dist: Point(0, -1 * dist),
]


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


def get_square_anchor_point(square):
    return Point((square - 1), -(square - 1))


def get_side_anchor_point(square, side):
    translation_to_next_anchor = [Point(0, 1), Point(1, 0), Point(0, -1)]
    side_anchor = []
    side_anchor.append(get_square_anchor_point(square))
    side_length = square * 2 - 2  # explain the -2

    for i in range(0, 3):
        side_end = Point(
            side_anchor[i].x + point_transforms[i](side_length).x,
            side_anchor[i].y + point_transforms[i](side_length).y,
        )

        side_anchor.append(
            Point(
                side_end.x + translation_to_next_anchor[i].x,
                side_end.y + translation_to_next_anchor[i].y,
            )
        )

    return side_anchor[side]


def calc(i):
    side_anchor_point = get_side_anchor_point(get_square(i), get_side(i))
    position = get_position_on_side(i)
    translation = point_transforms[get_side(i)](position)
    point = (side_anchor_point.x + translation.x, side_anchor_point.y + translation.y)
    return point
