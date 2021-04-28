sentence = input()

num_zero = 0
num_one = 0
check = False
while check != True:   
    idx = 0
    if sentence[0] == '0':
        while sentence[idx] != '1':
            idx += 1
            if idx == len(sentence):
                idx -= 1
                check = True
                break
        num_zero += 1
        sentence = sentence[idx:]
    else:
        while sentence[idx] != '0':
            idx += 1
            if idx == len(sentence):
                idx -= 1
                check = True
                break
        num_one += 1
        sentence = sentence[idx:]

print(min(num_zero, num_one)) 