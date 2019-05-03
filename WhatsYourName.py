#!/bin/python3
first_name = str(input())
last_name = str(input())

def print_full_name(first_name, last_name):
    if len(first_name) <=10 and len(last_name) <=10 :
        print("Hello " + first_name.capitalize() +" " + last_name.capitalize() +"! You just delved into python.")

print_full_name(first_name, last_name)
