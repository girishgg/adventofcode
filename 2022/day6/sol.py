fn = "input.txt"
line = open(fn).read().strip()

def solve(offset: int) -> int:
  for i in range(len(line)):
    marker = line[i:i+offset]
    if len(set(marker)) == offset:
      return i+offset
    

print(f"Part 1: {solve(4)}")
print(f"Part 2: {solve(14)}")
