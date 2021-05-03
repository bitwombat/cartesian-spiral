#!/usr/bin/env python

coord_transforms = [
    lambda coord: (coord[0], coord[1] + 1),
    lambda coord: (coord[0] + 1, coord[1]),
    lambda coord: (coord[0], coord[1] - 1),
    lambda coord: (coord[0] - 1, coord[1]),
]


def calc(i):
    coord = (0, 0)

    break_increment_state = True
    break_increment = 1
    next_break_value = 2

    coord_transform_index = 0

    for j in range(2, i + 1):

        coord = coord_transforms[coord_transform_index](coord)

        if j == next_break_value:
            next_break_value += break_increment

            if break_increment_state:
                break_increment += 1

            break_increment_state = not break_increment_state

            coord_transform_index = (coord_transform_index + 1) % 4

    return coord
