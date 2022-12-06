with open('input.txt') as f:
    input_string = f.readlines()
paper_total=0
for i in input_string:
    temp_list = i.split('x')
    temp_list = list(map(int, temp_list))
    l,w,h = temp_list
    paper_total += (2*l*w)+(2*w*h)+(2*h*l)
    temp_list.sort()
    smallest_area=temp_list[0]*temp_list[1]
    paper_total+=smallest_area
print(paper_total)
