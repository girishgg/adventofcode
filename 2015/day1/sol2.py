with open('input.txt') as f:
    input_string = str(f.readlines())
count=0
pos=0
for i in input_string:
    if i=='(':
        count+=1
    elif i==')':
        count-=1
    if count == -1:
        print(pos-1)
        break
    pos+=1
