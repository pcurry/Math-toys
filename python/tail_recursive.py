#!/usr/bin/env python

collatz_orbits = {1: [1], 2: [2, 1]}

def collatz_orbit_list(num):
    return collatz_orbit_tail_recursive_memo(num, [], collatz_orbits)

def collatz_orbit_tail_recursive_memo(num, orbit, memo={1: [1], 2: [2, 1], 4: [4, 2, 1]}):
    if num in memo:
        result = memo[num]
        if orbit != []:
            # Patch the results into the memo
            for n in orbit:
                memo[n] = orbit[orbit.index(n):] + result
            result = orbit + result
        return result
    else:
        orbit.append(num)
        if num % 2 == 0:
            recurse_num = num / 2
        else:
            recurse_num = 3 * num + 1
        return collatz_orbit_tail_recursive_memo(recurse_num, orbit, memo)


