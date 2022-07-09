import sys
from io import StringIO

input1 = """1 2 3 4"""
input2 = """-1 0 1"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


def array_sum(array, index):
    if index == len(array) - 1:
        return array[index]

    return array[index] + array_sum(array, index + 1)


nums = [int(x) for x in input().split()]

print(array_sum(nums, 0))
