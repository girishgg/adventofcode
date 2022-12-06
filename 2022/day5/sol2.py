part1 = False
with open("input.txt", "r") as f:
    stacks = [[] for i in range(9)]
    lns = f.readlines()
    loc = lns.index("\n")
    for l in lns[:loc - 1]:
        for i in range(9):
            if 1 + 4 * i < len(l):
                c = l[1+4*i]
                if c != " ":
                    stacks[i].append(c)
    for i in range(9):
        stacks[i] = stacks[i][::-1]
    for l in lns[loc+1:]:
            z = l.split(" ")
            from_ = int(z[3]) - 1
            to_ = int(z[5]) - 1
            cnt = int(z[1])
            stk = stacks[from_][-cnt:]
            if part1:
                stk = stk[::-1]
            stacks[to_] += stk
            stacks[from_] = stacks[from_][:-cnt]
    print(''.join([s[-1] for s in stacks]))
