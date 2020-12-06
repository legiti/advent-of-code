import os


script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'pearson_input.txt')

# part 1
count_answers = 0
with open(input_path) as f:
    answer_group = set()
    for line in f:
        if line != '\n':
            answer_group.update(set(line.strip()))
        else:
            count_answers = count_answers + len(answer_group)
            answer_group = set()
print(f'part 1: {count_answers} questions answered')

# part 2
count_all_answered_yes = 0
with open(input_path) as f:
    first_line = True
    answered_yes = []
    for line in f:
        if line != '\n':
            if first_line:
                first_line = False
                answered_yes = list(set(line.strip()))
            else:
                answered_yes_copy = answered_yes.copy()
                for answer in answered_yes:
                    if answer not in list(line.strip()):
                        answered_yes_copy.remove(answer)
                answered_yes = answered_yes_copy
        else:
            count_all_answered_yes = count_all_answered_yes + len(set(answered_yes))
            first_line = True
            answered_yes = []
print(f'part 2: {count_all_answered_yes} questions where all group members answered yes')