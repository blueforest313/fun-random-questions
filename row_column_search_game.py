import random
import timeit

import matplotlib.pyplot as plt
import numpy as np


def winning_player(n:int, m:int, k:int, balls=None) -> str:
    if not balls:
        balls = [[random.randint(1, n), random.randint(1, m)] for k in range(0, k)]
    start_a = [1,1]
    start_b = [1,1]
    while True:
        if start_a in balls and start_b in balls:
            return 'E'
        elif start_a in balls:
            return 'A'
        elif start_b in balls:
            return 'B'

        if start_a[1] == m:
            start_a[1] = 1
            start_a[0] += 1
        else:
            start_a[1] += 1

        if start_b[0] == n:
            start_b[0] = 1
            start_b[1] += 1
        else:
            start_b[0] += 1


def winning_player_improve(n:int, m:int, k:int, balls=None) -> str:
    # if balls:
    #     balls_0 = [balls[i][0] for i in range(0,k)]
    #     balls_1 = [balls[i][1] for i in range(0,k)]
    # else:
    rng = np.random.default_rng()
    balls_0 = rng.integers(1, n+1, k)
    balls_1 = rng.integers(1, m+1, k)
    # print(balls_0)
    # print(balls_1)
    # minimum_row = min(balls_0)
    # minimum_column = min(balls_1)
    # minimum_row_to_column = m
    # minimum_column_to_row = n
    # for i in range(0,k):
    #     if balls_0[i] == minimum_row:
    #         if balls_1[i] < minimum_row_to_column:
    #             minimum_row_to_column = balls_1[i]
    #     if balls_1[i] == minimum_column:
    #         if balls_0[i] < minimum_column_to_row:
    #             minimum_column_to_row = balls_0[i]
    # print(minimum_row, minimum_row_to_column, minimum_column, minimum_column_to_row)
    minimum_row = balls_0.min()
    minimum_column = balls_1.min()
    minimum_row_index = np.where(balls_0 == minimum_row)
    minimum_col_index = np.where(balls_1 == minimum_column)
    minimum_a = (minimum_row-1)*m + min(balls_1[minimum_row_index])
    minimum_b = (minimum_column-1)*n + min(balls_0[minimum_col_index])
    if minimum_a < minimum_b:
        return 'A'
    elif minimum_b < minimum_a:
        return 'B'
    else:
        return 'E'


def winning_probability(n:int, m:int, k:int, run_times:int) -> float:
    a_wins = b_wins = equals = 0

    for i in range(0,run_times):
        result = winning_player(n,m,k)
        if result == 'A':
            a_wins += 1
        elif result == 'B':
            b_wins += 1
        else:
            equals += 1
    return (a_wins + (1/2)*equals)/run_times


def winning_probability_improve(n:int, m:int, k:int, run_times:int) -> float:
    a_wins = b_wins = equals = 0

    for i in range(0,run_times):
        result = winning_player_improve(n,m,k)
        if result == 'A':
            a_wins += 1
        elif result == 'B':
            b_wins += 1
        else:
            equals += 1
    return (a_wins + 0.5*equals)/run_times


# print(winning_probability(2,1024,2,10000))

# plt.style.use('_mpl-gallery')

# new_func = np.vectorize(winning_probability_improve)
# X, Y = np.meshgrid(np.linspace(1,10,10), np.linspace(1,10,10))
# n = 2
# Z = new_func(X,Y,2,10000)
# print(Z)
# fig, ax = plt.subplots()
# ax.imshow(Z)
# plt.show()

# Z = np.zeros((20,20))
# for i in range(1,21):
#     for j in range(1,21):
#         Z[i-1][j-1] = winning_probability_improve(i,j,2,10000)
Z = np.fromfunction(lambda i,j: winning_probability_improve(i+1, j+1, 2, 10000), (20, 20), dtype=float)
print(Z)
# fig, ax = plt.subplots()
# ax.imshow(Z)
# plt.show()


# print(winning_probability_improve(3,1,2,10000))
# print(winning_player_improve(3,1,8))

# print(winning_probability(2,1024,2,10000))
#
# a = np.array([1,2,3])
# print(a[0])

# for i in range(0,1):
#     balls_set = [[random.randint(1, 20), random.randint(1, 20)] for k in range(0, 2)]
#     print(winning_player(20,20,2, balls=balls_set), winning_player_improve(20,20,2, balls=balls_set))

# balls_set = [[10,10], [10,9]]
# print(winning_player_improve(20,20,2,balls=balls_set))

# for i in range(0,100):
#     balls_set = [[random.randint(1, 100), random.randint(1, 100)] for k in range(0, 2)]
#     if winning_probability(100,100,2,100, balls=balls_set) == winning_probability_improve(100,100,2,100, balls=balls_set):
#         print("It's the same!")


# t1 = timeit.timeit('winning_player_improve(1000,1000,2)', 'from __main__ import winning_player_improve', number=100)
# t2 = timeit.timeit('winning_player(1000,1000,2)', 'from __main__ import winning_player', number=100)
# print(t1, t2)
