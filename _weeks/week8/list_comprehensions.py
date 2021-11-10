import math
import itertools
# Make a list of square roots of all the numbers from 1-9
result_a = []
for i in range(1, 9 + 1):
    result_a.append(math.sqrt(i))

result_a = [math.sqrt(i) for i in range(1, 9 + 1)]
print(result_a)

# Remove all non-integers from the list you just made
result_b = [elem for elem in result_a if elem == int(elem)]
result_b = [math.sqrt(i) for i in range(1, 9 + 1) if math.sqrt(i) == int(math.sqrt(i))]

print(result_b)


# Take 3 inputs from stdin and then store them in a list
#result_c = [input() for i in range(3)]
#result_c = [input(), input(), input()]
#print(result_c)

# Find all Pythagorean triples (sets of three integers between 1-30 such that a^2+b^2 == c^2)
result_d = [(a, b, c) for a in range(1,30+1) for b in range(1,30+1) for c in range(1,30+1) if a*a + b*b == c*c]
result_d = [elem for elem in itertools.product(range(1,30+1), repeat=3) if elem[0]*elem[0] + elem[1]*elem[1] == elem[2]*elem[2]]
print(result_d)

print(list(range(2, 20, 3)))
# implement a generator function named my_range that copies range's talents
def my_range(start, stop, step):
    result = start
    while (result < stop):
        yield result
        result += step

# make this function "return" each value twice 
def repeat_twice(gen_function, a, b, c):
    for i in gen_function(a, b, c):
        yield i
        yield i

print(list(repeat_twice(my_range, 2, 20, 3)))

# your version of the itertools.product version with two iterables
print(list(itertools.product([1, 2, 3], ["a", "b", "c", "d"])))

def my_product(iter_a, iter_b):
    for elem_a in iter_a:
        for elem_b in iter_b:
            yield elem_a, elem_b


print(list(my_product([1, 2, 3], ["a", "b", "c", "d"])))

print(list((a, b) for a in [1, 2, 3] for b in ["a", "b", "c", "d"]))
