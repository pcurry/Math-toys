"""A collection of functions to generate series functions with memoized
collected values.
"""


def series_n_maker(seed0, seed1):
    seed = [seed0, seed1]

    def series_n_memo(nth, memo=seed):
        if nth < len(memo):
            return memo[nth]
        else:
            seed.append(series_n_memo(nth - 1) + series_n_memo(nth - 2))
            return seed[-1]
    series_n_memo(10)
    return series_n_memo
