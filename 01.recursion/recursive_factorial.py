import sys
from io import StringIO

input1 = """5"""
input2 = """10"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


def calc_fact(n):
    if n == 0:
        return 1
    return n * calc_fact(n - 1)


n = int(input())

print(calc_fact(n))
