#!/bin/python3
acceptable_values = list(range(1900, (10**5)+1))
def is_leap(year):
    success = True
    nope = False
    
    # Write your logic here
    if year in acceptable_values:
        if (year % 4) != 0 :
            return nope
        elif (year % 4) == 0 and (year % 100) == 0:
            if (year % 400) == 0:
                return success
            else:
                return nope
        elif (year %4) == 0:
            return success

    elif year not in acceptable_values:
        print ("Out of range")

year = int(input())
print(is_leap(year))