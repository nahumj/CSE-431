
class LCG:
    def __init__(self, seed):
        self.seed = seed
        self.a = 2
        self.c = 4
        self.m = 1000000
    
    def get_rand(self):
        # https://en.wikipedia.org/wiki/Linear_congruential_generator
        self.seed = (self.a * self.seed + self.c) % self.m # X(n)
        return self.seed


class MiddleSquare:
    def __init__(self, seed):
        self.seed = seed
    
    def get_rand(self):
        self.seed *= self.seed
        self.seed = (self.seed // 1000) % 1000000
        return self.seed



def time_until_repeat(rng):
    seen = set()
    steps = 0

    while True:
        value = rng.get_rand()
        if value in seen:
            break
        seen.add(value)
        steps += 1
    
    return steps


# uint64_t x = 0, w = 0, s = 0xb5ad4eceda1ce2a9;
# inline static uint32_t msws() {
# x *= x; x += (w += s); return x = (x>>32) | (x<<32);
# }

class MiddleSquareWeyl:
    def __init__(self, seed):
        self.seed = seed # x
        self.w = 0
        self.s = 0xb5ad4eceda1ce2a9

    
    def get_rand(self):
        self.seed *= self.seed
        self.w += self.s
        self.seed += self.w
        self.seed = self.seed % (2**64)
        self.seed = (self.seed >> 32) | (self.seed << 32)
        return self.seed

def main():
    # lcg_generator = LCG(0)
    # # for _ in range(10):
    # #     print(lcg_generator.get_rand())
    # steps = time_until_repeat(lcg_generator)
    # print(f"It took {steps} steps to repeat!")

    # middlesquare_generator = MiddleSquare(2020)
    # # for _ in range(10):
    # #     print(middlesquare_generator.get_rand())
    # steps = time_until_repeat(middlesquare_generator)
    # print(f"It took {steps} steps to repeat!")

    middlesquareweyl_generator = MiddleSquareWeyl(2020)
    # for _ in range(10):
    #     print(middlesquareweyl_generator.get_rand())
    steps = time_until_repeat(middlesquareweyl_generator)
    print(f"It took {steps} steps to repeat!")


if __name__ == "__main__":
    main()
        