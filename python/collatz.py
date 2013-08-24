"""Calculating the sequences for integers per the 
Collatz conjecture (http://en.wikipedia.org/wiki/Collatz_conjecture).

Currently calculates the sequence for each number as a list.
A graph is probably a more compact representation.
"""

FIRST_TWENTY_SEQUENCES = {1: [1],
                          2: [2, 1],
                          3: [3, 10, 5, 16, 8, 4, 2, 1],
                          4: [4, 2, 1],
                          5: [5, 16, 8, 4, 2, 1],
                          6: [6, 3, 10, 5, 16, 8, 4, 2, 1],
                          7: [7, 22, 11, 34, 17, 52, 26, 
                              13, 40, 20, 10, 5, 16, 8, 
                              4, 2, 1],
                          8: [8, 4, 2, 1],
                          9: [9, 28, 14, 7, 22, 11, 34, 17,
                              52, 26, 13, 40, 20, 10, 5, 16,
                              8, 4, 2, 1],
                          10: [10, 5, 16, 8, 4, 2, 1],
                          11: [11, 34, 17, 52, 26, 13, 40, 20,
                               10, 5, 16, 8, 4, 2, 1],
                          12: [12, 6, 3, 10, 5, 16, 8, 4, 2, 1],
                          13: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
                          14: [14, 7, 22, 11, 34, 17, 52, 26, 13,
                               40, 20, 10, 5, 16, 8, 4, 2, 1],
                          15: [15, 46, 23, 70, 35, 106, 53, 160,
                               80, 40, 20, 10, 5, 16, 8, 4, 2, 1],
                          16: [16, 8, 4, 2, 1],
                          17: [17, 52, 26, 13, 40, 20, 10, 5, 16,
                               8, 4, 2, 1],
                          18: [18, 9, 28, 14, 7, 22, 11, 34, 17,
                               52, 26, 13, 40, 20, 10, 5, 16, 8,
                               4, 2, 1],
                          19: [19, 58, 29, 88, 44, 22, 11, 34, 17,
                               52, 26, 13, 40, 20, 10, 5, 16, 8,
                               4, 2, 1],
                          20, [20, 10, 5, 16, 8, 4, 2, 1]}


def collatz_sequence_tail_recurse_memo(num,
                                       sequence,
                                       memo={1: [1],
                                             2: [2, 1],
                                             4: [4, 2, 1]}):
    if num in memo:
        if sequence != []:
            sequence += memo[num]
            for o_index in xrange(len(sequence)):
                o_num = sequence[o_index]
                if o_num not in memo:
                    memo[o_num] = sequence[o_index:]
            return sequence
        return memo[num]
    else:
        sequence.append(num)
        if num % 2 == 0:
            return collatz_sequence_tail_recurse_memo(
                (num / 2), sequence)
        else:
            return collatz_sequence_tail_recurse_memo(
                (3 * num + 1), sequence)


def collatz_sequence_specify_memo(num, memo):
    return collatz_sequence_tail_recurse_memo(num, [], memo)


def collatz_sequence(num):
    return collatz_sequence_tail_recurse_memo(num, [])
