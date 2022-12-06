import string

letters = string.ascii_lowercase + string.ascii_uppercase
def prio(c):
    return letters.index(c) + 1

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

stuff = []
for i in range(0,len(lines),3):
    a,b,c = lines[i:i+3]
    common = set(a).intersection(b).intersection(c)
    stuff.append(''.join(common))

print(sum(map(prio, stuff)))
