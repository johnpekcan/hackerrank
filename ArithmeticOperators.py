#!/bin/python3
numberA = int(input())
numberB = int(input())

if 1 <= numberA and numberB <= 10**10:
    print(numberA+numberB)
    print(numberA-numberB)
    print(numberA*numberB)

else:
    print ("Not in range")