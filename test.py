# ファイル読み込み
input_data = open('input.txt', 'r')

# 整形
input_data = input_data.readlines()

input_m = int(input_data[-1:][0].rstrip('\n'))
input_data = input_data[:-1]
# print(input_m )

formating_data = []
for input_line in input_data:
    input_line = input_line.split(':')
    input_line[0] = int(input_line[0])
    input_line[1] = input_line[1].rstrip('\n')
    # print(input_line)
    formating_data.append(input_line)
# print(formating_data)
sorted_formating_data = sorted(formating_data)

# 出力
output_string = ''
for line in sorted_formating_data:
    if input_m % line[0] == 0:
        output_string += line[1]
        # print(line)

print(output_string)
