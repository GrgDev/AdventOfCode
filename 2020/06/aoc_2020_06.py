import argparse


# The parse_args function here generally just parses for two things: input file and puzzle part.
# I believe every AOC puzzle comes in two parts and so sometimes requires two code paths.
# Sometimes it is easier to implement two different code solutions per part but this gives you
# the option of using the same code in case there's a lot of logic overlap between the two parts.
# There's usually a lot of overlap.
#
# -i or --input should be set to the full file path of the input file
# -p or --part should be set to either 1 or 2 to denote if this is for the first or second puzzle part
def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input',
        type=open,
        help='Input File',
        required=True
    )
    parser.add_argument(
        '-p', '--part',
        type=int,
        help='Puzzle Part',
        required=True
    )
    return parser.parse_args(args)


# Just about every AOC puzzle gives you a large input file that you need to parse into some usable data structure.
# Do that here and return the collection of data structures to be handled by another function.
def parse_input(file_handler):
    parsed_groups = []
    group_answers = {}
    group_size = 0
    for line in file_handler:
        yes_answers = line.strip()
        if len(yes_answers) == 0:
            group_answers['size'] = group_size
            parsed_groups.append(group_answers)
            group_answers = {}
            group_size = 0
        else:
            group_size += 1
            for answer in yes_answers:
                if answer in group_answers:
                    group_answers[answer] += 1
                else:
                    group_answers[answer] = 1
    return parsed_groups


# This function is here to isolate and organize the puzzle solving logic after input parsing.
def solve_puzzle(parsed_contents, puzzle_part=1):
    if puzzle_part == 1:
        unique_answer_sum = 0
        for group_answers in parsed_contents:
            unique_answer_sum += (len(group_answers) - 1)  # Have to -1 here because of the added 'size' field
        print(f"Total Sum of Unique Group Answers: {unique_answer_sum}")
    if puzzle_part == 2:
        unanimous_answer_sum = 0
        for group_answers in parsed_contents:
            for answer, count in group_answers.items():
                if answer != "size" and count == group_answers['size']:
                    unanimous_answer_sum += 1
        print(f"Total Sum of Unanimous Group Answers: {unanimous_answer_sum}")


def main(args=None):
    parsed_args = parse_args(args)
    input_handler = parsed_args.input
    puzzle_part = parsed_args.part
    parsed_input = parse_input(input_handler)
    solve_puzzle(parsed_input, puzzle_part)


if __name__ == '__main__':
    # See the parse_args() function comment at the top to understand the arg usage in the line below.
    main("-i ./puzzle_input.txt -p 2".split())
    # Uncomment the line above if you want to run this code from the IDE and want to pass the args via code.
    # Uncomment the line below instead if you want to run this code from the CLI and pass args there as well.
    # main()
