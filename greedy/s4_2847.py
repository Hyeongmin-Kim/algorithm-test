import sys
input = sys.stdin.readline

n = int(input())

scores = []
for i in range(n):
    scores.append(int(input()))

res = 0
for i in range(n-1, 0, -1):
    if scores[i-1] >= scores[i]:
        res += scores[i-1] - scores[i] + 1
        scores[i-1] = scores[i] - 1 

sys.stdout.write('{}'.format(res))