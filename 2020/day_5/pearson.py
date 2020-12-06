import os


script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'pearson_input.txt')


def convert_binary_mapping(mapping):
    min_val = 0
    max_val = pow(2, len(mapping)) - 1
    for i in range(len(mapping)):
        val_range = pow(2, len(mapping) - i - 1)
        if mapping[i] in ['F', 'L']:
            max_val = max_val - val_range
        else:
            min_val = min_val + val_range
    if min_val == max_val:
        return min_val
    raise Exception(f'{mapping} did not coalsece to a precise value; range {min_val} to {max_val}')


with open(input_path) as f:
    max_seat_id = 0
    max_row = ''
    all_seat_ids = []
    for line in f:
        row = line[:7]
        column = line[7:].strip() # this is important
        row_num = convert_binary_mapping(row)
        col_num = convert_binary_mapping(column)
        seat_id = (row_num * 8) + col_num
        all_seat_ids.append(seat_id)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
            max_row = line

# part 1
print(f'highest value seat id: {max_seat_id}')
# highest value seat id: 933
print(max_row)
# BBBFBFFRLR

# part 2
all_seat_ids.sort()
all_possible_seats = set(range(min(all_seat_ids), max(all_seat_ids)))
print(all_possible_seats - set(all_seat_ids))
# {711}
