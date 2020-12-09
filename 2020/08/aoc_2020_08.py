import argparse
import copy
from pprint import pprint


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
        instruction_parts = line.strip().split()
        instruction = {
            'code': instruction_parts[0],
            'offset': int(instruction_parts[1])
        }
        line_outputs.append(instruction)
    return line_outputs


def execute_instructions(instructions):
    line_counter = 0
    accumulator = 0
    while line_counter < len(instructions) and 'visit' not in instructions[line_counter]:
        instruction = instructions[line_counter]
        line_counter += 1
        if instruction['code'] == 'acc':
            accumulator += instruction['offset']
        elif instruction['code'] == 'jmp':
            line_counter += instruction['offset'] - 1  # To offset the earlier +1 to the line counter
        instruction['visit'] = True
    return {
        'count': line_counter,
        'acc': accumulator,
        'halts': line_counter >= len(instructions)
    }


# This function is here to isolate and organize the puzzle solving logic after input parsing.
def solve_puzzle(instructions, puzzle_part=1):
    if puzzle_part == 1:
        result = execute_instructions(instructions)
    elif puzzle_part == 2:
        possibly_corrupted = []
        for i in range(len(instructions)):
            if instructions[i]['code'] == 'nop' or instructions[i]['code'] == 'jmp':
                possibly_corrupted.append(i)
        for i in possibly_corrupted:
            instructions_copy = copy.deepcopy(instructions)
            if instructions_copy[i]['code'] == 'nop':
                instructions_copy[i]['code'] = 'jmp'
            elif instructions_copy[i]['code'] == 'jmp':
                instructions_copy[i]['code'] = 'nop'
            result = execute_instructions(instructions_copy)
            if result['halts']:
                print(f"Found halt! Instruction at {str(i)} changed to {instructions_copy[i]['code']}.")
                print(f"Final Line Counter: {result['count']}, Final Accumulator Value: {result['acc']}")
                return


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
