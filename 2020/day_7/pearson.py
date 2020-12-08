import os


script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'pearson_input.txt')

bag_rules = {}
with open(input_path) as f:
    for line in f:
        bag_rule = line.strip().split(' contain ')
        container = bag_rule[0].split('bag')[0].strip()
        contents_raw = bag_rule[1].split(', ')
        contents = []
        for allowed_bags in contents_raw:
            if any(char.isdigit() for char in allowed_bags):
                contents.append({
                    'num_bags': int(allowed_bags.split()[0]),
                    'color': ' '.join(allowed_bags.split()[1:3])
                })
        bag_rules[container] = contents


def get_valid_container(bag_color_to_contain, container):
    if len(bag_rules[container]) == 0:
        return False
    valid_contents = [bag_rule['color'] for bag_rule in bag_rules[container]]
    if bag_color_to_contain in valid_contents:
        return True
    return any([get_valid_container(bag_color_to_contain, bag_rule['color']) for bag_rule in bag_rules[container]])

valid_containers = set()
for container in bag_rules.keys():
    if get_valid_container('shiny gold', container):
        valid_containers.add(container)
print(f'part 1: {len(valid_containers)}')
# part 1: 265
