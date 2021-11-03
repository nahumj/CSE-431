#!/usr/bin/env python3

import time
import copy


def bin_packing_nonoptimal(threshold, values):
    return len(values)


def bin_packing_brute_force(threshold, values, included=None, excluded=None, undecided=None):
    if included is None:
        included = []
        excluded = []
        undecided = list(values)
    if not undecided:
        total = sum(included)
        if total > threshold:
            return 0
        return total

    included = copy.copy(included)
    excluded = copy.copy(excluded)
    undecided = copy.copy(undecided)

    next_value = undecided.pop()

    included.append(next_value)
    total_with_value = bin_packing_brute_force(
        threshold, values, included, excluded, undecided)

    del included[-1]
    excluded.append(next_value)
    total_without_value = bin_packing_brute_force(
        threshold, values, included, excluded, undecided)

    best_total = max(total_with_value, total_without_value)
    return best_total


def bin_packing_backtracking(threshold, values, included=None, excluded=None, undecided=None, included_total=0):
    if included is None:
        included = []
        excluded = []
        undecided = list(values)
    if included_total > threshold:
        return 0
    if not undecided:
        return included_total

    included = copy.copy(included)
    excluded = copy.copy(excluded)
    undecided = copy.copy(undecided)

    next_value = undecided.pop()

    included.append(next_value)
    total_with_value = bin_packing_backtracking(
        threshold, values, included, excluded, undecided, included_total + next_value)

    del included[-1]
    excluded.append(next_value)
    total_without_value = bin_packing_backtracking(
        threshold, values, included, excluded, undecided, included_total)

    best_total = max(total_with_value, total_without_value)
    return best_total


BEST_TOTAL_SO_FAR = 0


def bin_packing_bounding(threshold, values, included=None, excluded=None, undecided=None, included_total=0, undecided_total=None):
    global BEST_TOTAL_SO_FAR
    if included is None:
        included = []
        excluded = []
        undecided = list(values)
        undecided_total = sum(undecided)
        BEST_TOTAL_SO_FAR = 0
    if included_total > threshold:
        return 0
    if (included_total + undecided_total) < BEST_TOTAL_SO_FAR:
        return 0
    if not undecided:
        if included_total > BEST_TOTAL_SO_FAR:
            BEST_TOTAL_SO_FAR = included_total
        return included_total

    included = copy.copy(included)
    excluded = copy.copy(excluded)
    undecided = copy.copy(undecided)

    next_value = undecided.pop()
    undecided_total -= next_value

    included.append(next_value)
    total_with_value = bin_packing_bounding(
        threshold, values, included, excluded, undecided, included_total + next_value, undecided_total)

    del included[-1]
    excluded.append(next_value)
    total_without_value = bin_packing_bounding(
        threshold, values, included, excluded, undecided, included_total, undecided_total)

    best_total = max(total_with_value, total_without_value)
    return best_total


def bin_packing_sorting(threshold, values, included=None, excluded=None, undecided=None, included_total=0, undecided_total=None):
    global BEST_TOTAL_SO_FAR
    if included is None:
        included = []
        excluded = []
        undecided = list(values)
        undecided.sort()
        undecided_total = sum(undecided)
        BEST_TOTAL_SO_FAR = 0
    if included_total > threshold:
        return 0
    if (included_total + undecided_total) < BEST_TOTAL_SO_FAR:
        return 0
    if not undecided:
        if included_total > BEST_TOTAL_SO_FAR:
            BEST_TOTAL_SO_FAR = included_total
        return included_total

    included = copy.copy(included)
    excluded = copy.copy(excluded)
    undecided = copy.copy(undecided)

    next_value = undecided.pop()
    undecided_total -= next_value

    included.append(next_value)
    total_with_value = bin_packing_sorting(
        threshold, values, included, excluded, undecided, included_total + next_value, undecided_total)

    del included[-1]
    excluded.append(next_value)
    total_without_value = bin_packing_sorting(
        threshold, values, included, excluded, undecided, included_total, undecided_total)

    best_total = max(total_with_value, total_without_value)
    return best_total


if __name__ == "__main__":
    number_of_values, threshold = input().split()
    number_of_values = int(number_of_values)
    threshold = float(threshold)
    values = [float(input()) for _ in range(number_of_values)]

    print(f"Number of Values = {number_of_values}")
    print(f"Threshold = {threshold}")
    print(f"Values = {values}")

    start_time = time.perf_counter_ns()
    solution = bin_packing_sorting(threshold, values)
    end_time = time.perf_counter_ns()
    duration = (end_time - start_time) / 1_000_000_000
    print(f"Solution = {solution}")
    print(f"Duration = {duration} (sec)")
