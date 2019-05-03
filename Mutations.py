#!/bin/python3
s = str(input())
i, c = input().split()

def mutate_string(s, i, c):
    before = str(s[:int(i)])
    after = str(s[int(i+1):])    
    return before + str(c) + after

s_new = mutate_string(s, int(i), c)
print(s_new)