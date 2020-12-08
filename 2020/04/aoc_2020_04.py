import sys
import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input',
        type=open,
        help='Input File',
        required=True
    )
    return parser.parse_args()


def parse_batch_file(batch_file):
    passports = []
    passport = {}
    valid_passports = 0
    required_fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    }
    for line in batch_file:
        processed_line = line.strip()
        if processed_line != '':
            fields = processed_line.split()
            for field in fields:
                key, value = field.split(':')
                passport[key] = value
        else:
            if passport.keys() >= required_fields:
                passport['is_well_formed'] = True
                valid_passports += 1
            else:
                passport['is_well_formed'] = False
            passports.append(passport)
            passport = {}
    print(f"Total Passport Entries: {str(len(passports))}")
    print(f"Well Formed Passports: {str(valid_passports)}")
    return passports


valid_eye_colors = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
]


def main():
    args = parse_args()
    passports = parse_batch_file(args.input)
    well_formed_passports = []
    for passport in passports:
        if passport['is_well_formed']:
            well_formed_passports.append(passport)
    cm_match = re.compile(r'^1\d{2}cm$')
    inch_match = re.compile(r'^\d{2}in$')
    hair_match = re.compile(r'^#[0-9a-fA-F]{6}$')
    id_match = re.compile(r'^\d{9}$')
    valid_count = 0
    for passport in well_formed_passports:
        is_valid = True
        if 1920 > int(passport['byr']) or int(passport['byr']) > 2002:
            is_valid = False
        if 2010 > int(passport['iyr']) or int(passport['iyr']) > 2020:
            is_valid = False
        if 2020 > int(passport['eyr']) or int(passport['eyr']) > 2030:
            is_valid = False
        if cm_match.match(passport['hgt']) or inch_match.match(passport['hgt']):
            if cm_match.match(passport['hgt']):
                cm_height = int(passport['hgt'].strip('cm'))
                if 150 > cm_height or 193 < cm_height:
                    is_valid = False
            if inch_match.match(passport['hgt']):
                inch_height = int(passport['hgt'].strip('in'))
                if 59 > inch_height or 76 < inch_height:
                    print(f"\tInvalid IN Height: {inch_height}")
                    is_valid = False
        else:
            is_valid = False
        if not hair_match.match(passport['hcl']):
            is_valid = False
        if not passport['ecl'] in valid_eye_colors:
            is_valid = False
        if not id_match.match(passport['pid']):
            is_valid = False
        else:
            print(f"Valid PID: {passport['pid']}")
        passport['is_valid'] = is_valid
        if is_valid:
            valid_count += 1
    print(f"Valid Passport Count: {valid_count}")


if __name__ == '__main__':
    main()
