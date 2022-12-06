with open('input.txt') as f:
    input_string = f.readlines()
ribbon_total=0
for i in input_string:
    temp_list = i.split('x')
    temp_list = list(map(int, temp_list))
    l,w,h = temp_list
    ribbon_total += l*w*h
    temp_list.sort()
    cubic_feet=(temp_list[0]+temp_list[1]) *2
    ribbon_total+=cubic_feet
print(ribbon_total)
