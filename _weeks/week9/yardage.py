import time
import functools

# Key: feet of elvish rope
# Value: worth in silver pennies
FEET_TO_PENNIES = {
    2: 1,
    3: 2,
    5: 5,
    6: 7,
    9: 13,
    100: 200,
}


@functools.cache
def optimal_lengths_recursive(n):
    if n <= 0:
        return 0
    best = 0
    for feet, pennies in FEET_TO_PENNIES.items():
        if n >= feet:
            potential_value = pennies + optimal_lengths_recursive(n - feet)
            if potential_value > best:
                best = potential_value
    return best


lengths_to_results = {}


def optimal_lengths_memoized(n):
    if n in lengths_to_results:
        return lengths_to_results[n]
    if n <= 0:
        return 0
    best = 0
    for feet, pennies in FEET_TO_PENNIES.items():
        if n >= feet:
            potential_value = pennies + optimal_lengths_memoized(n - feet)
            if potential_value > best:
                best = potential_value
    lengths_to_results[n] = best
    return best


def optimal_lengths_dynamic_programming(n):
    array_of_length_to_best_value = [0] * (n + 1)
    for subproblem in range(1, len(array_of_length_to_best_value)):
        array_of_length_to_best_value[subproblem] = array_of_length_to_best_value[subproblem - 1]
        best = array_of_length_to_best_value[subproblem - 1]
        for feet, pennies in FEET_TO_PENNIES.items():
            if feet > subproblem:
                continue
            value = array_of_length_to_best_value[subproblem - feet] + pennies
            if value > best:
                best = value
                array_of_length_to_best_value[subproblem] = value
    # print(array_of_length_to_best_value)
    return array_of_length_to_best_value[-1]


def optimal_lengths_dynamic_programming_with_cuts(n):
    array_of_length_to_best_value_and_lengths = [(0, [])] * (n + 1)
    for subproblem in range(1, len(array_of_length_to_best_value_and_lengths)):
        array_of_length_to_best_value_and_lengths[
            subproblem] = array_of_length_to_best_value_and_lengths[subproblem - 1]
        best, _ = array_of_length_to_best_value_and_lengths[subproblem]
        for feet, pennies in FEET_TO_PENNIES.items():
            if feet > subproblem:
                continue
            value, lengths = array_of_length_to_best_value_and_lengths[subproblem - feet]
            value += pennies
            if value > best:
                best = value
                array_of_length_to_best_value_and_lengths[subproblem] = value, lengths + [
                    feet]
    # print(array_of_length_to_best_value_and_lengths)
    return array_of_length_to_best_value_and_lengths[-1]


if __name__ == "__main__":
    rope_length = 35
    while True:
        print(f"Rope length = {rope_length}")
        start_time = time.perf_counter_ns()
        result = optimal_lengths_dynamic_programming_with_cuts(rope_length)
        end_time = time.perf_counter_ns()

        print(f"Result = {result}")
        duration = (end_time - start_time) / 1_000_000_000
        print(f"Duration (sec) = {duration}")
        print()
        rope_length *= 2
        break
