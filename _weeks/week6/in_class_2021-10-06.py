import itertools
import random
import collections

def shuffle_simple(input):
    """
    It should take a list (array) in python and permute it.
    The permutation should be a random selection of all possible permutations.
    """
    all_permutations = list(itertools.permutations(input))
    special_permutation = random.choice(all_permutations)
    return special_permutation

def shuffle_one_at_a_time(input):
    input_copy = list(input) 
    result = []
    for _ in range(len(input_copy)):
        value = random.choice(input_copy)
        input_copy.remove(value)
        result.append(value)
    return result

def shuffle_index(input):
    input_copy = list(input)
    result = []
    for _ in range(len(input_copy)):
        index = random.randint(0, len(input_copy) - 1)
        value = input_copy.pop(index)
        result.append(value)
    return result

def shuffle_setinel(input):
    input_copy = list(input)
    result = []
    random_gen_calls = 0
    while any(input_copy):
        index = random.randint(0, len(input_copy) - 1)
        random_gen_calls += 1
        value = input_copy[index]
        if value is None:
            continue
        result.append(value)
        input_copy[index] = None
    # print(f"Random calls = {random_gen_calls}")
    return result

def shuffle_inplace(input):
    result = list(input)
    for index in range(len(input)):
        other_index = random.randint(0, len(input) - 1)
        # swap
        result[index], result[other_index] = result[other_index], result[index]
    return result

def test_shuffle(shuffle_function):
    data = list("ABC")
    permutation_counter = collections.Counter()
    for _ in range(1000000):
        result = shuffle_function(data)
        permutation_counter[tuple(result)] +=  1
    for permutation in itertools.permutations(data):
        print(f"{permutation}: {permutation_counter[permutation]}")
    
        


def main():
    print("Studying Shuffles")
    data = list("ABCDEFG")
    result = shuffle_inplace(data)
    print(result)

if __name__ == "__main__":
    test_shuffle(shuffle_inplace)