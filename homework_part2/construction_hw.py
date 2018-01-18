n = int(input())
var = ({'global': set()})
parent = ({'global': None})
lst = []

def create(dict1, dict2, i, j):
    dict1[i] = set()
    dict2[i] = j
    return dict1, dict2

def add(dict, i, j):
    if i in dict:
        dict[i].add(j)
    return dict

def get(dict1, dict2, i, j):
    if j in dict1[i]:
        return i
    elif i == 'global':
        return None
    else:
        return get(dict1, dict2, dict2[i], j)

for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add(var, namesp, arg)
    elif cmd == 'create':
        create(var, parent, namesp, arg)
    elif cmd == 'get':
        get(var, parent, namesp, arg)
        lst.append(get(var, parent, namesp, arg))
for i in range(len(lst)):
    print(lst[i])