num_of_test = int(input())

num_quater = 0
num_dime = 0
num_nickel = 0
num_penny = 0

tests = []
for i in range(num_of_test):
    tests.append(int(input()))

for i in range(num_of_test):
    while (tests[i] > 0):
        if (tests[i] >= 25):
            tests[i] -= 25
            num_quater += 1
            continue
        elif (tests[i] >= 10):
            tests[i] -= 10
            num_dime += 1
            continue
        elif (tests[i] >= 5):
            tests[i] -= 5
            num_nickel += 1
            continue
        else:
            tests[i] -= 1
            num_penny += 1
            continue
    
    print(num_quater, num_dime, num_nickel, num_penny)
    num_quater, num_dime, num_nickel, num_penny = 0, 0, 0, 0