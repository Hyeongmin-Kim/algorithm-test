import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ropes = [0] * 10001

    for _ in range(n):
        ropes[int(input())] += 1

    m, result = 0, 0
    for i in range(10000, 0, -1):
        if ropes[i] == 0:
            continue
        m += ropes[i]
        result = max(result, i * m)
    sys.stdout.write('{0}'.format(result))

main()