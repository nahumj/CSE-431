import pprint
import math
"""
Mind Breaking Game

You are on a space exploration team that discovers an alien artifact.
It has a helmet that members of your crew can put on, and a knob with
many different power levels. 
A previous expedition found that it is possible that 
if the level is too high, it melts the wearer's brain. 
But lower levels may reveal glimpses in to the secrets of the universe, 
with more detail as the levels increase. 
You are concerned that using the machine too many times might
damage it.

Your mission is to find the maximum level a human can endure, as quickly
as possible (meaning as few trials of the machine). You are willing to
expend the lives of your crewmates in this important mission.

Known Facts
* If a crewmate survives a level, all crewmates can survive that level
  and all lower levels.
* If a crewmate gets melted, all other crewmates will get melted on that
  level and all higher levels.
* Any level may possibly melt brains
* Possibly no levels may melt brains

Report the maximum number of trials needed to determine the max safe
level of the machine given:
* the number of crewmates you can expend (n)
* number of power levels on the knob (p).
"""

def max_trials_needed(num_crewmates, num_power_levels):
    if num_crewmates == 1:
        return num_power_levels
    if num_power_levels == 1:
        return 1
    if num_power_levels == 0:
        return 0
    
    minimum_trials = None
    for power_levels_to_try in range(1, num_power_levels + 1):
        # consider if crewmate melts
        melt = max_trials_needed(num_crewmates - 1, power_levels_to_try - 1)
        # consider if crewmate doesn't melt
        no_melt = max_trials_needed(num_crewmates, num_power_levels - power_levels_to_try)

        worst_case = max(melt, no_melt) + 1
        if minimum_trials is None:
            minimum_trials = worst_case
        minimum_trials = min(minimum_trials, worst_case)
    return minimum_trials

def max_trials_needed_dp(num_crewmates, num_power_levels):
    results_array = [[None] * (num_power_levels + 1) for _ in range(num_crewmates + 1)]
    for i in range(num_power_levels + 1):
        results_array[0][i] = 0
    for i in range(num_power_levels + 1):
        results_array[1][i] = i
    for i in range(num_crewmates + 1):
        results_array[i][0] = 0
    for i in range(2, num_crewmates + 1):
        for j in range(1, num_power_levels + 1):
            minimum_trials = None
            for power_levels_to_try in range(1, j + 1):
                # consider if crewmate melts
                melt = results_array[i - 1][power_levels_to_try - 1]
                # consider if crewmate doesn't melt
                no_melt = results_array[i][j - power_levels_to_try]

                worst_case = max(melt, no_melt) + 1
                if minimum_trials is None:
                    minimum_trials = worst_case
                minimum_trials = min(minimum_trials, worst_case)
            results_array[i][j] = minimum_trials
    # pprint.pprint(results_array)
    return results_array[-1][-1]

# Solution from https://brilliant.org/wiki/egg-dropping/
def binomial(x, n, k):
    answer = 0
    aux = 1
    for i in range(1, n + 1):
        aux *= x + 1 - i
        aux /= i
        answer += aux
        if answer > k:
            break
    return answer


def max_trials_needed_math(num_crewmates, num_power_levels):
    upper = num_power_levels
    inf = 0
    mid = (upper + inf) / 2
    while upper - inf > 1:
        mid = math.floor(inf + (upper - inf) / 2)
        if binomial(mid, num_crewmates, num_power_levels) < num_power_levels:
            inf = mid
        else:
            upper = mid
    return inf + 1

if __name__ == "__main__":
    print(max_trials_needed_math(2, 100))