def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    # Import function from __main__ to get access
    find_dup_setup = "from __main__ import find_duplicate_movies"
    time_it_helper = timeit.timeit(
        stmt="find_duplicate_movies('movies.txt')",
        setup=find_dup_setup
    )
