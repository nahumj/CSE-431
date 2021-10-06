import random
import collections
import itertools


def shuffle_pop(input):
    result = []
    while input:
        index = random.randint(0, len(input) - 1)
        result.append(input.pop(index))
    return result


def shuffle_sentinel(input):
    result = []
    while any(input):
        index = random.randint(0, len(input) - 1)
        if input[index]:
            result.append(input[index])
            input[index] = 0
    return result


def shuffle_sentinel_better(input):
    iterations = 0
    result = []
    while len(result) < len(input):
        iterations += 1
        index = random.randint(0, len(input) - 1)
        if input[index]:
            result.append(input[index])
            input[index] = 0
    print(f"Iterations = {iterations}")
    return result


def shuffle_inplace(input):
    result = list(input)
    for index in range(len(input)):
        other_index = random.randint(0, len(result) - 1)
        # Swap
        result[index], result[other_index] = result[other_index], result[index]
    return result


def shuffle_inplace_2(input):
    result = list(input)
    for index in range(len(input) - 1):
        later_index = random.randint(index, len(result) - 1)
        # Swap
        result[index], result[later_index] = result[later_index], result[index]
    return result


def test_shuffle(shuffle_function):
    permute_counter = collections.Counter()
    data = list("ABC")
    for _ in range(1000000):
        shuffled = shuffle_function(data)
        permute_counter[tuple(shuffled)] += 1
    for permutation in itertools.permutations(data):
        print(f"{permutation}: {permute_counter[permutation]}")


def main():
    data = list("ABC")
    shuffled = shuffle_inplace(data)
    print(shuffled)


if __name__ == "__main__":
    test_shuffle(shuffle_inplace)
