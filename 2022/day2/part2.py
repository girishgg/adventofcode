with open('input.txt') as file:
    lines = file.readlines()
ans = 0
outcome = {}
outcome['X'] = {'A': 'scissors', 'B': 'rock', 'C': 'paper'}
outcome['Y'] = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
outcome['Z'] = {'A': 'paper', 'B': 'scissors', 'C': 'rock'}
shape = {'rock': 1, 'paper': 2, 'scissors': 3}
ans = 0
for line in lines:
    you, me = line.split()
    res = outcome[me][you]
    ans += shape[res]
    i = ['X', 'Y', 'Z'].index(me)
    ans += i*3
print(ans)
