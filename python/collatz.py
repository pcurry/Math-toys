"""Calculating the sequences for integers per the 
Collatz conjecture (http://en.wikipedia.org/wiki/Collatz_conjecture).

Currently calculates the sequence for each number as a list.
A graph is probably a more compact representation.
"""


from collections import defaultdict

COLLATZ_SEQUENCE = defaultdict(lambda: "Unknown")
COLLATZ_SEQUENCE[1] = [1]
COLLATZ_SEQUENCE[2] = [2, 1]
COLLATZ_SEQUENCE[4] = [4] + COLLATZ_SEQUENCE[2]

                          # 3: [3, 10, 5, 16, 8, 4, 2, 1],
                          # 4: [4, 2, 1],
                          # 5: [5, 16, 8, 4, 2, 1],
                          # 6: [6, 3, 10, 5, 16, 8, 4, 2, 1],
                          # 7: [7, 22, 11, 34, 17, 52, 26,
                          #     13, 40, 20, 10, 5, 16, 8,
                          #     4, 2, 1],
                          # 8: [8, 4, 2, 1],
                          # 9: [9, 28, 14, 7, 22, 11, 34, 17,
                          #     52, 26, 13, 40, 20, 10, 5, 16,
                          #     8, 4, 2, 1],
                          # 10: [10, 5, 16, 8, 4, 2, 1],
                          # 11: [11, 34, 17, 52, 26, 13, 40, 20,
                          #      10, 5, 16, 8, 4, 2, 1],
                          # 12: [12, 6, 3, 10, 5, 16, 8, 4, 2, 1],
                          # 13: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
                          # 14: [14, 7, 22, 11, 34, 17, 52, 26, 13,
                          #      40, 20, 10, 5, 16, 8, 4, 2, 1],
                          # 15: [15, 46, 23, 70, 35, 106, 53, 160,
                          #      80, 40, 20, 10, 5, 16, 8, 4, 2, 1],
                          # 16: [16, 8, 4, 2, 1],
                          # 17: [17, 52, 26, 13, 40, 20, 10, 5, 16,
                          #      8, 4, 2, 1],
                          # 18: [18, 9, 28, 14, 7, 22, 11, 34, 17,
                          #      52, 26, 13, 40, 20, 10, 5, 16, 8,
                          #      4, 2, 1],
                          # 19: [19, 58, 29, 88, 44, 22, 11, 34, 17,
                          #      52, 26, 13, 40, 20, 10, 5, 16, 8,
                          #      4, 2, 1],
                          # 20, [20, 10, 5, 16, 8, 4, 2, 1]}


def find_collatz_sequence(num: int, verbose: bool = False) -> list:
    missing_sequence = "Unknown"
    num_sequence = COLLATZ_SEQUENCE[num]
    if num_sequence != missing_sequence:
        return num_sequence
    stack = [num]
    next_int = collatz_next(num)
    latest_sequence = COLLATZ_SEQUENCE[next_int]
    def print_status():
        if verbose:
            print(f"stack: {stack}, next_int: {next_int}, latest_sequence: {latest_sequence}")
    print_status()
    while latest_sequence == missing_sequence:
        stack.append(next_int)
        next_int = collatz_next(next_int)
        latest_sequence = COLLATZ_SEQUENCE[next_int]
        print_status()
    while stack:
        next_int = stack.pop()
        latest_sequence = [next_int] + latest_sequence
        COLLATZ_SEQUENCE[next_int] = latest_sequence
        print_status()
    return latest_sequence


def collatz_next(num: int) -> int:
    return (num * 3) + 1 if num % 2 else num // 2
