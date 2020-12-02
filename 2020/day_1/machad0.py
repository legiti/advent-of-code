from functools import reduce
from itertools import combinations
from operator import mul

with open('../inputs/day1.txt') as f:
    input = [int(l.strip()) for l in f]

_head = lambda seq: list(seq)[0]

def find_2020_sum(n=2, input=input):
    return reduce(mul, (_head(filter(lambda x: sum(x) == 2020, combinations(input, n)))))

# part 1
print(find_2020_sum())

# part 2
print(find_2020_sum(n=3))
