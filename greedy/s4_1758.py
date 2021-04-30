import sys
input = sys.stdin.readline

n = int(input())
tips = [0] * 100001
for i in range(n):
    tips[int(input())] += 1

m = 0
res = 0
for i in range(100000, 0, -1):
    while tips[i] > 0:
        if i - m >= 0:
            res += i - m
        m += 1
        tips[i] -= 1

sys.stdout.write('{}'.format(res))