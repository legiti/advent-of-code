import os
import re

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'pearson_input.txt')

passports = []
valid_passports_pt_1 = []
valid_passports_pt_2 = []
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def is_valid_birth_year(year):
    try:
        year_as_int = int(year)
        return year_as_int >= 1920 and year_as_int <= 2002
    except ValueError:
        return False


def is_valid_issue_year(year):
    try:
        year_as_int = int(year)
        return year_as_int >= 2010 and year_as_int <= 2020
    except ValueError:
        return False


def is_valid_expiration_year(year):
    try:
        year_as_int = int(year)
        return year_as_int >= 2020 and year_as_int <= 2030
    except ValueError:
        return False


def is_valid_height(height):
    if height[-2:] == 'cm':
        try:
            height_cm = int(height[:-2])
            return height_cm >= 150 and height_cm <= 193
        except ValueError:
            return False
    if height[-2:] == 'in':
        try:
            height_in = int(height[:-2])
            return height_in >= 59 and height_in <= 76
        except ValueError:
            return False
    return False


def is_valid_hair_color(hair_color):
    pattern = re.compile('[0-9a-f]{6}', re.IGNORECASE)
    return hair_color[0] == '#' and len(hair_color) == 7 and bool(pattern.match(hair_color[1:]))


def is_valid_eye_color(eye_color):
    valid_eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return eye_color in valid_eye_colors


def is_valid_passport_id(pid):
    if len(pid) == 9:
        try:
            pid_as_int = int(pid)
            return True
        except ValueError:
            return False
    return False


def is_valid_pt_2(passport_as_dict):
    return is_valid_birth_year(passport_as_dict['byr']) \
        and is_valid_issue_year(passport_as_dict['iyr']) \
        and is_valid_expiration_year(passport_as_dict['eyr']) \
        and is_valid_height(passport_as_dict['hgt']) \
        and is_valid_hair_color(passport_as_dict['hcl']) \
        and is_valid_eye_color(passport_as_dict['ecl']) \
        and is_valid_passport_id(passport_as_dict['pid'])


with open(input_path) as f:
    passport = ''
    for line in f:
        if line != '\n':
            passport = passport + line.strip() + ' '
        else: # i had to cheat and add an extra newline to the input, otherwise it would ignore the last input
            passport_as_dict = {k: v for k, v in [field.split(':') for field in passport.strip().split(' ')]}
            passports.append(passport_as_dict)
            passport_as_dict_keys = set(passport_as_dict.keys())
            if required_fields.issubset(passport_as_dict_keys):
                valid_passports_pt_1.append(passport_as_dict)
                if is_valid_pt_2(passport_as_dict):
                    valid_passports_pt_2.append(passport_as_dict)
            # reset passport string
            passport = ''

print(f'part 1: {len(valid_passports_pt_1)} valid passports')
# part 1: 213 valid passports
print(f'part 2: {len(valid_passports_pt_2)} valid passports')
# part 2: 147 valid passports