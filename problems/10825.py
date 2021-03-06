# https://www.acmicpc.net/problem/10825

import sys


input = sys.stdin.readline
n = int(input())
scores = [list(map(str, input().rstrip().split())) for _ in range(n)]

scores.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for score in scores:
    print(score[0])
