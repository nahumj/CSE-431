import time
import functools

FEET_TO_PENNIES = {
    4: 1,
    3: 2,
    5: 5,
    6: 7,
    9: 13,
    100: 105,
}



def optimal_lengths_recursive(n):
    """
    Return the optimal value possible for a given rope length (n)
    """
    if n <= 0:
        return 0
    best = 0
    for feet, pennies in FEET_TO_PENNIES.items():
        if n >= feet:
            potential_value = pennies + optimal_lengths_recursive(n - feet)
            if potential_value > best:
                best = potential_value
    return best

optimal_lengths_saved = {}

def optimal_lengths_memoized(n):
    if n in optimal_lengths_saved:
        return optimal_lengths_saved[n]

    if n <= 0:
        optimal_lengths_saved[n] = 0
        return 0
    best = 0
    for feet, pennies in FEET_TO_PENNIES.items():
        if n >= feet:
            potential_value = pennies + optimal_lengths_memoized(n - feet)
            if potential_value > best:
                best = potential_value
    optimal_lengths_saved[n] = best
    return best

@functools.cache
def optimal_lengths_cache(n):
    """
    Return the optimal value possible for a given rope length (n)
    """
    if n <= 0:
        return 0
    best = 0
    for feet, pennies in FEET_TO_PENNIES.items():
        if n >= feet:
            potential_value = pennies + optimal_lengths_cache(n - feet)
            if potential_value > best:
                best = potential_value
    return best


def optimal_lengths_dynamic_programming(n):
    array_of_length_to_best_value = [0] * (n + 1)
    for subproblem in range(1, len(array_of_length_to_best_value)):
        best = array_of_length_to_best_value[subproblem - 1]
        array_of_length_to_best_value[subproblem] = best
        for feet, pennies in FEET_TO_PENNIES.items():
            if feet > subproblem:
                continue
            potential_value = pennies + array_of_length_to_best_value[subproblem - feet]
            if potential_value > best:
                best = potential_value
                array_of_length_to_best_value[subproblem] = potential_value
    return array_of_length_to_best_value[-1]


def optimal_lengths_dynamic_programming_with_cuts(n):
    array_of_length_to_best_value_and_cuts = [(0, [])] * (n + 1)
    for subproblem in range(1, len(array_of_length_to_best_value_and_cuts)):
        array_of_length_to_best_value_and_cuts[subproblem] = array_of_length_to_best_value_and_cuts[subproblem - 1]
        #print(array_of_length_to_best_value_and_cuts)
        best_value, _ =  array_of_length_to_best_value_and_cuts[subproblem] 

        for feet, pennies in FEET_TO_PENNIES.items():
            if feet > subproblem:
                continue
            potential_value, cuts = array_of_length_to_best_value_and_cuts[subproblem - feet]
            potential_value +=  pennies
            if potential_value > best_value:
                best_value = potential_value
                array_of_length_to_best_value_and_cuts[subproblem] = (potential_value, cuts + [feet])
    # return the optimal value, and a list of the needed cuts
    return array_of_length_to_best_value_and_cuts[-1]
    


if __name__ == "__main__":
    rope_length = 35
    while True:
        start_time = time.perf_counter_ns()
        result = optimal_lengths_dynamic_programming_with_cuts(rope_length)
        end_time = time.perf_counter_ns()
        duration = (end_time - start_time) / 1_000_000_000
        print(f"rope_length = {rope_length}; result = {result}; duration = {duration}")

        rope_length *= 2
       