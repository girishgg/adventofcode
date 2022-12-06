with open('input.txt') as f:
    input_string = f.readlines()
#input_string = "Test())"
up_count = str(input_string).count('(')
down_count = str(input_string).count(')')
print("Floor count:" + str(up_count - down_count))

