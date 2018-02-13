

with open("text.txt") as f, open("test_copy.txt", "w") as w:
    lst = []
    for line in f:
        lst.append(line)
    print(lst)
    for l in reversed(lst):
        w.write(l)
