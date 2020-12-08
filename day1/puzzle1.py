import sys
import argparse


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
    input_file = parse_args().input
    expenses = []
    for line in input_file:
        expenses.append(int(line))
    print("\nTwo Entry Solution")
    print("*"*80)
    for i in expenses:
        for j in expenses:
            if (i + j) == 2020:
                print(f"i = {i}, j = {j}, i*j = {i * j}")
    print("\nThree Entry Solution")
    print("*" * 80)
    for i in expenses:
        for j in expenses:
            for k in expenses:
                if (i + j + k) == 2020:
                    print(f"i = {i}, j = {j}, k = {k}, i*j*k = {i * j * k}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
