import operator
def main():
    print(x + y +  "!" for x in "abc" if x != "b" for y in "123")

    result = []
    for x in "abc":
        if x != "b":
            result.append(x + "!")
    # map
    input = [23,54,2,54]
    result = []
    for x in input:
        result.append(double(x))
    print(result)
    print(list(map(double, input)))
    result = (operator.mul(x, 2) for x in input)
    print(tuple(result))
    lambda x: x * 2
    print(list(map(lambda x: x * 2, input)))


def double(x):
    return x * 2  


if __name__ == "__main__":
    main()