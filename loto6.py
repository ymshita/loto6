import itertools
import random

nums = {4,5,6,11,12,13,14,17,18,19,20,21,27,28,29,36,37,38,39,40}

combinations = set(itertools.combinations(nums, 6))
combinationList = list(combinations)
fixedList = []

for combination in combinationList:
    tmp = -1
    left = 0
    numArray = list(combination)
    for num in numArray:


count = 0

size = len(fixedList)
print("size: " + size)
while count < 30:
    print(fixedList[random.randint(0, size-1)])
    count += 1