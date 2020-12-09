import argparse

# This file is a template file for all of my Advent of Code 2020 puzzle solutions.


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
    line_outputs = []
    for line in file_handler:
        pass  # TODO: Put file parsing code here
    return line_outputs


# This function is here to isolate and organize the puzzle solving logic after input parsing.
def solve_puzzle(parsed_contents, puzzle_part=1):
    pass  # TODO: Solve the rest of the fucking puzzle


def main(args=None):
    parsed_args = parse_args(args)
    input_handler = parsed_args.input
    puzzle_part = parsed_args.part
    parsed_input = parse_input(input_handler)
    solve_puzzle(parsed_input, puzzle_part)


if __name__ == '__main__':
    # See the parse_args() function comment at the top to understand the arg usage in the line below.
    main("-i ./example_input.txt -p 1".split())
    # Uncomment the line above if you want to run this code from the IDE and want to pass the args via code.
    # Uncomment the line below instead if you want to run this code from the CLI and pass args there as well.
    # main()
