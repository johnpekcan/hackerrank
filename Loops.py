#!/bin/python3
num = int(input())
acceptable_values = list(range(1, 21))
N = 0
while 0 <= N < num:
    print(N**2)
    N+= 1
