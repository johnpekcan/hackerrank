#!/bin/python3
number = int(input())
array = map(int, input().split())
answer = []

if 2 <= number <= 10:
   for arg in array:
       if -100 <= arg <= 100:
           if arg not in answer:
               answer.append(arg)
       else:
           print("Scores need to be in between -100 and 100")
else:
    print("The number of score cards must be between 2 and 10")

close = sorted(answer)
print(close[-2])
