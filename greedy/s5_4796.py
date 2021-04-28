import sys

test_cases = []
for case in sys.stdin:
    test_cases.append(case.strip())
    if case.strip() == '0 0 0':
        break

for i in range(len(test_cases)-1):
    l, p, v = test_cases[i].split()
    l, p, v = int(l), int(p), int(v)

    time_spent = 0 
    while True:
        if v >= p:
            time_spent += l
            v -= p
        else:
            if v > l:
                time_spent += l
                break
            else:
                time_spent += v
                break
    
    print("Case {0}: {1}".format(i+1, time_spent))