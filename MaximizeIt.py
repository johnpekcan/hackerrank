#!/bin/python3
from itertools import product

first_line = input().split()
K = int(first_line[0])
M = int(first_line[1])
tally_man = list()

for each in range(K):
    ignore, *line = input().split()
    row = list(map(int, line))
    tally_man.append(row)
# print(tally_man)

results = map(lambda x: sum(i ** 2 for i in x) % M, product(*tally_man))
print(max(results))
