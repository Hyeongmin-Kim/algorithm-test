price = int(input())
change = 1000 - price
num_of_coin = 0

while (change > 0):
    if (change >= 500):
        change -= 500
        num_of_coin += 1
    elif (change >= 100):
        change -= 100
        num_of_coin += 1
    elif (change >= 50):
        change -= 50
        num_of_coin += 1
    elif (change >= 10):
        change -= 10
        num_of_coin += 1
    elif (change >= 5):
        change -= 5
        num_of_coin += 1
    else:
        change -= 1
        num_of_coin += 1

print(num_of_coin)