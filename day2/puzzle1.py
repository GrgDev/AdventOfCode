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


def main():
    args = parse_args()
    policies = []
    for line in args.input:
        policies.append(line)
    print("\nOld Password Policy Validator")
    print("*" * 80)
    valid_password_count = 0
    for policy in policies:
        match_range, match_letter, match_password = policy.split()
        match_letter = match_letter.strip(':')
        match_range = match_range.split('-')
        match_count = len(re.findall(match_letter, match_password))
        if int(match_range[0]) <= match_count <= int(match_range[1]):
            valid_password_count += 1
    print(f"Valid Password Count: {valid_password_count}")

    print("\nNew Password Policy Validator")
    print("*" * 80)
    valid_password_count = 0
    for policy in policies:
        match_range, match_letter, match_password = policy.split()
        match_letter = match_letter.strip(':')
        match_range = match_range.split('-')
        # Using an != as a logical equivalent as XOR because... that actually works?! It's the same?! *mind blown*
        if (match_password[int(match_range[0])-1] == match_letter) != (match_password[int(match_range[1])-1] == match_letter):
            valid_password_count += 1
    print(f"Valid Password Count: {valid_password_count}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
