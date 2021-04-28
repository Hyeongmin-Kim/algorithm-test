import sys

sentences = []
for line in sys.stdin:
    sentences.append(line)

for i in range(len(sentences)):
    s, t = sentences[i].split()
    check = True
    check_list = []
    for j in range(len(s)):
        check_list.append(s[j])
        if check_list[j] in t:
            idx = t.find(check_list[j])
            t = t[idx+1:]  
        else:
            check = False
            break
    
    if check == True:
        print('Yes')
    else:
        print('No')
