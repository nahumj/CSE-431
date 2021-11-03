import time
import itertools

# https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def bin_packing_correct(threshold, values):
    best_total = 0
    for subset in powerset(values):
        total = sum(subset)
        if total > best_total and total <= threshold:
            best_total = total
    return best_total
        
def bin_packing_recursive(threshold, values, included=None, excluded=None, undecided=None):
    if included is None:
        included = []
        excluded = []
        undecided = values[:]
    if not undecided:
        total = sum(included)
        if total > threshold:
            return 0.0
        return total
    
    included = included[:]
    excluded = excluded[:]
    undecided = undecided[:]

    value = undecided.pop()

    # Try including it
    included.append(value)
    total_including_value = bin_packing_recursive(
            threshold, values, included, excluded, undecided)

    # Try excluding it
    excluded.append(value)
    included.pop()
    total_excluding_value = bin_packing_recursive(
            threshold, values, included, excluded, undecided)
    
    best_total = max(total_including_value, total_excluding_value)
    return best_total


def bin_packing_backtracking(threshold, values, included=None, excluded=None, undecided=None, included_total=0):
    if included is None:
        included = []
        excluded = []
        undecided = values[:]
        included_total = 0
    if included_total > threshold:
        return 0.0
    if not undecided:
        return included_total
    
    
    included = included[:]
    excluded = excluded[:]
    undecided = undecided[:]

    value = undecided.pop()

    # Try including it
    included.append(value)
    total_including_value = bin_packing_backtracking(
            threshold, values, included, excluded, undecided, included_total + value)

    # Try excluding it
    excluded.append(value)
    included.pop()
    total_excluding_value = bin_packing_backtracking(
            threshold, values, included, excluded, undecided, included_total)
    
    best_total = max(total_including_value, total_excluding_value)
    return best_total


BEST_TOTAL_SO_FAR = 0

def bin_packing_bounding(threshold, values, included=None, excluded=None, 
        undecided=None, included_total=0, undecided_total=None):
    global BEST_TOTAL_SO_FAR
    if included is None:
        included = []
        excluded = []

        undecided = values[:]
        undecided_total = sum(undecided)
        BEST_TOTAL_SO_FAR = 0


    if included_total > threshold:
        return 0.0
    if (included_total + undecided_total) < BEST_TOTAL_SO_FAR:
        return 0.0
    if not undecided:
        return included_total
    
    included = included[:]
    excluded = excluded[:]
    undecided = undecided[:]

    value = undecided.pop()
    undecided_total -= value

    # Try including it
    included.append(value)
    total_including_value = bin_packing_bounding(
            threshold, values, included, excluded, undecided, included_total + value, undecided_total)

    # Try excluding it
    excluded.append(value)
    included.pop()
    total_excluding_value = bin_packing_bounding(
            threshold, values, included, excluded, undecided, included_total, undecided_total)
    
    best_total = max(total_including_value, total_excluding_value)
    if best_total > BEST_TOTAL_SO_FAR:
        BEST_TOTAL_SO_FAR = best_total
    return best_total


def bin_packing_ordered(threshold, values, included=None, excluded=None, 
        undecided=None, included_total=0, undecided_total=None):
    global BEST_TOTAL_SO_FAR
    if included is None:
        included = []
        excluded = []
        undecided = values[:]
        # undecided.sort(reverse=True)
        undecided.sort()
        undecided_total = sum(undecided)
        BEST_TOTAL_SO_FAR = 0


    if included_total > threshold:
        return 0.0
    if (included_total + undecided_total) < BEST_TOTAL_SO_FAR:
        return 0.0
    if not undecided:
        return included_total
    
    
    included = included[:]
    excluded = excluded[:]
    undecided = undecided[:]

    value = undecided.pop()
    undecided_total -= value

    # Try including it
    included.append(value)
    total_including_value = bin_packing_ordered(
            threshold, values, included, excluded, undecided, included_total + value, undecided_total)

    # Try excluding it
    excluded.append(value)
    included.pop()
    total_excluding_value = bin_packing_ordered(
            threshold, values, included, excluded, undecided, included_total, undecided_total)
    
    best_total = max(total_including_value, total_excluding_value)
    if best_total > BEST_TOTAL_SO_FAR:
        BEST_TOTAL_SO_FAR = best_total
    return best_total

if __name__ == "__main__":
    number_of_values, threshold = input().split()
    number_of_values = int(number_of_values)
    threshold = float(threshold)
    values = [float(input()) for _ in range(number_of_values)]

    print(f"number_of_values = {number_of_values}")
    print(f"threshold = {threshold}")
    print(f"values = {values}")

    start_time = time.perf_counter_ns()
    result = bin_packing_ordered(threshold, values)
    end_time = time.perf_counter_ns()
    duration = (end_time - start_time) / 1_000_000_000

    print(f"result = {result}")
    print(f"duration = {duration} (sec)")
