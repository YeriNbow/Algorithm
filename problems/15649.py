# https://www.acmicpc.net/problem/15649

import sys
import itertools

input = sys.stdin.readline
n, m = map(int, input().split())

for r in itertools.permutations(range(1, n+1), m):
    print(' '.join(map(str, r)))
