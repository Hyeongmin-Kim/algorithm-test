time_cooking = int(input())

num_A = 0
num_B = 0
num_C = 0

decision = True

while (time_cooking > 0):
    if (time_cooking >= 300):
        time_cooking -= 300
        num_A += 1
        continue
    elif (time_cooking >= 60):
        time_cooking -= 60
        num_B += 1
        continue
    elif (time_cooking >= 10):
        time_cooking -= 10
        num_C += 1
        continue
    else:
        decision = False
        break

if (decision == True):
    print(num_A, num_B, num_C)
else:
    print(-1)

