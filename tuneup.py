#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

import timeit
import functools
import pstats
import cProfile
__author__ = "timothy la (tla111)"
"Received help from Joseph"


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sortby = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats()
        return result
    return wrapper
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # raise NotImplementedError("Complete this decorator function")


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

# Original Function

# 3 seconds
# @profile
# def find_duplicate_movies(src):
#     """Returns a list of duplicate movies from a src list."""
#     movies = read_movies(src)
#     duplicates = []
#     while movies:
#         movie = movies.pop()
#         if is_duplicate(movie, movies):
#             duplicates.append(movie)
#     return duplicates

# Function Refactored


# .08 seconds
# @profile
def find_duplicate_movies(src):
    # """Returns a list of duplicate movies from a src list."""
    movies = [movie.lower() for movie in read_movies(src)]
    movies.sort()
    # Using zip to find duplicates
    #   [a,b,c,c,e]
    #   [1:] = [b,c,c,e]
    #   [:-1] = [d,c,c,a]
    not_duplicate = [x for x, y in zip(movies[1:], movies[:-1]) if x == y]
    # not_duplicate = [x for x in movies if movies.count(x) > 1]
    return not_duplicate


# What can I do to make the function perform faster?
#   Which lines can I combine to make one line
#   For loop instead of while loop?

# duplicates = [movie = movies.pop() for x in range(movies)]
# duplicates = []
# return list(if movies)


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    # Function we want to time -> find_duplicates_movies
    #   Import function from __main__ to get access
    find_dup_setup = "from __main__ import find_duplicate_movies"
    t = timeit.Timer(
        stmt="find_duplicate_movies('movies.txt')",
        setup=find_dup_setup
    )

    number = 3
    repeat = 2
    result = t.repeat(repeat=repeat, number=number)
    print(result)
    # Divide Min of result by number of repeats
    best_time = min(result) / float(repeat)
    print(
        f"Best time across {repeat} repeats of {number} " +
        f"runs per repeat: {best_time} sec ")


def main():
    """Computes a list of duplicate movie entries."""
    timeit_helper()
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
