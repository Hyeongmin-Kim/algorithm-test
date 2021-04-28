n, m = input().split()
n, m = int(n), int(m)

pos_basket = 1
j = int(input())
pos_apple = []
for i in range(j):
    pos_apple.append(int(input()))

travel_distance = 0
for i in range(j):
    temp_distance = 0
    if (pos_basket+m-1) < pos_apple[i]:
        temp_distance += pos_apple[i] - (pos_basket+m-1)
        travel_distance += temp_distance
        pos_basket += temp_distance
    elif pos_basket > pos_apple[i]:
        temp_distance += pos_basket - pos_apple[i]
        travel_distance += temp_distance
        pos_basket -= temp_distance  
    else:
        continue

print(travel_distance)