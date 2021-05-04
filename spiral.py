#!/usr/bin/env python

from math import ceil, sqrt

coord_transforms = [
    lambda dist: (-1 * dist, 0),
    lambda dist: (0, 1 * dist),
    lambda dist: (1 * dist, 0),
    lambda dist: (0, -1 * dist),
]


def which_square(j):
    return ceil(sqrt(j) / 2)


def which_anchor(j):
    square = which_square(j)
    return ((square - 1) * 2) ** 2 + 1


def get_anchor_coord(square):
    return ((square - 1), -(square - 1))


def which_side(j):
    square = which_square(j)
    anchor = which_anchor(j)
    normalised_j = j - anchor
    side_length = square * 2 - 1
    return normalised_j // side_length


def which_slot(j):
    square = which_square(j)
    anchor = which_anchor(j)
    side_length = square * 2 - 1
    normalised_j = j - anchor
    return normalised_j % side_length


def get_side_anchor(square, side):
    end_to_next_anchor = [(0, 1), (1, 0), (0, -1)]
    side_length = square * 2 - 2  # explain the -2
    side_anchor = [(0, 0), (0, 0), (0, 0), (0, 0)]
    side_anchor[0] = get_anchor_coord(square)

    side_end = (
        side_anchor[0][0] + coord_transforms[0](side_length)[0],
        side_anchor[0][1] + coord_transforms[0](side_length)[1],
    )

    side_anchor[1] = (
        side_end[0] + end_to_next_anchor[0][0],
        side_end[1] + end_to_next_anchor[0][1],
    )

    side_end = (
        side_anchor[1][0] + coord_transforms[1](side_length)[0],
        side_anchor[1][1] + coord_transforms[1](side_length)[1],
    )
    side_anchor[2] = (
        side_end[0] + end_to_next_anchor[1][0],
        side_end[1] + end_to_next_anchor[1][1],
    )
    side_end = (
        side_anchor[2][0] + coord_transforms[2](side_length)[0],
        side_anchor[2][1] + coord_transforms[2](side_length)[1],
    )
    side_anchor[3] = (
        side_end[0] + end_to_next_anchor[2][0],
        side_end[1] + end_to_next_anchor[2][1],
    )

    return side_anchor[side]


def calc(i):
    coord = get_side_anchor(which_square(i), which_side(i))
    offset = which_slot(i)
    side_length = which_square(i) * 2 - 2  # explain the -2
    travel = coord_transforms[which_side(i)](offset)
    our_coord = (coord[0] + travel[0], coord[1] + travel[1])
    return our_coord


# if __name__ == "__main__":
#    calc(5)
