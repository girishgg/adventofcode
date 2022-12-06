with open('input.txt') as file:
    lines = file.readlines()
ans = 0
outcome = {}
outcome['A'] = {'X': 3, 'Y': 6, 'Z': 0}
outcome['B'] = {'X': 0, 'Y': 3, 'Z': 6}
outcome['C'] = {'X': 6, 'Y': 0, 'Z': 3}
shape = {'X': 1, 'Y': 2, 'Z': 3}
for line in lines:
    you, me = line.split()
    ans += outcome[you][me]
    ans += shape[me]
print(ans)
