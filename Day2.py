###########################################
# Author: Malay Agarwal
# Problem: 
# Given a list of numbers and a number k, 
# return whether any two numbers from the 
# list add up to k.
###########################################

def main():
    k = 10
    k2 = k//2
    numbers = [1,53,2,7,3]
    goodnums = {k-x for x in numbers if x<=k2} & {x for x in numbers if x>k2}
    pairs = [(k-x, x) for x in goodnums]
    return bool(pairs)
print (main())
