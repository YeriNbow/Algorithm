# https://www.acmicpc.net/problem/11057

import sys

input = sys.stdin.readline

n = int(input())

dp = [1] * 10

for i in range(n-1):
    for j in range(1, 10):
        dp[j] = (dp[j] + dp[j-1]) % 10007

print(sum(dp)%10007)
