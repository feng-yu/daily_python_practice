"""
You leave in a city with perfect grid.
At each intersection, you random choose to go to north, south, east or west

"""


import random


def random_walk(n):
    """return the coordinate after nth random walk"""
    current_position = [0, 0]
    walk_choices = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for _ in range(10):
        choice = random.choice(walk_choices)
        current_position[0] = current_position[0] + choice[0]
        current_position[1] = current_position[1] + choice[1]

    return current_position


def random_walk2(n):
    x, y = 0, 0
    for _ in range(n):
        dx, dy = random.choice(((-1, 0), (1, 0), (0, -1), (0, 1)))
        x += dx
        y += dy
    return x, y


def test_random_walk():
    for _ in range(20):
        position = random_walk(10)
        distance = abs(position[0]) + abs(position[1])
        print(f'After 10 random walks, the position is {position} and distance is {distance}')


def test_random_walk2():
    for _ in range(20):
        x, y = random_walk2(10)
        print(f'After 10 random walks, the position is [{x}, {y}] and distance is {abs(x)+abs(y)}')


def find_percentage_lessen_than_4_blocks(stop_count, walk_count=10000):
    """
    find the percentage that after N stop, it's less than 4 blocks away from the start point
    :param walk_count:
    :param stop_count:
    :return:
    """

    for stop in range(5, stop_count):
        walk_lessen_4_block_count = 0
        for _ in range (walk_count):
            x, y = random_walk2(stop)
            if abs(x)+abs(y) < 5:
                walk_lessen_4_block_count += 1
        percentage_for_lessen_4_blocks = walk_lessen_4_block_count / walk_count
        print(f'After {walk_count} try, for {stop} stops, there are {percentage_for_lessen_4_blocks * 100}%, it is less than 5 blocks away')

find_percentage_lessen_than_4_blocks(30)



