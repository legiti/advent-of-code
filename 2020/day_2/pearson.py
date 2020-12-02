import os


script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'pearson_input.txt')


def is_valid_input_pt_1(line):
    case = line.strip().split(' ')
    case_as_dict =  {
                        'case': case,
                        'character': case[1][0],
                        'min_occurences' : int(case[0].split('-')[0]),
                        'max_occurences' : int(case[0].split('-')[1]),
                        'password': case[2],
                    }
    char_count = case_as_dict['password'].count(case_as_dict['character'])
    return char_count <= case_as_dict['max_occurences'] and char_count >= case_as_dict['min_occurences']


def is_valid_input_pt_2(line):
    case = line.strip().split(' ')
    case_as_dict =  {
                        'case': case,
                        'character': case[1][0],
                        'position_1' : int(case[0].split('-')[0]) - 1,
                        'position_2' : int(case[0].split('-')[1]) - 1,
                        'password': case[2],
                    }
    return case_as_dict['password'][case_as_dict['position_1']] != case_as_dict['password'][case_as_dict['position_2']] \
        and (case_as_dict['password'][case_as_dict['position_1']] == case_as_dict['character'] \
        or case_as_dict['password'][case_as_dict['position_2']] == case_as_dict['character'] )

with open(input_path) as f:
    valid_inputs_pt_1 = list(filter(lambda x: x == True, [is_valid_input_pt_1(l) for l in f]))

# had to iterate through input twice :( )
with open(input_path) as f:
    valid_inputs_pt_2 = list(filter(lambda x: x == True, [is_valid_input_pt_2(l) for l in f]))


print(f'answer pt 1: {len(valid_inputs_pt_1)}')
print(f'answer pt 2: {len(valid_inputs_pt_2)}')

