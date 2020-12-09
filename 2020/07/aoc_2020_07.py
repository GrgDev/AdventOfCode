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
    bag_entries = {}
    for line in file_handler:
        bag_define, bag_contains = line.strip().strip('.').split(" contain ", maxsplit=1)
        bag_define = bag_define.rstrip('s')
        bag_contains = bag_contains.split(', ')
        processed_bag_contains = {}
        if len(bag_contains) == 1 and bag_contains[0] == "no other bags":
            bag_entries[bag_define] = processed_bag_contains
        else:
            for bag in bag_contains:
                count, bag_name = bag.split(" ", maxsplit=1)
                bag_name = bag_name.rstrip("s")
                processed_bag_contains[bag_name] = int(count)
            bag_entries[bag_define] = processed_bag_contains
    return bag_entries


def can_have_target_bag(target_bag, bag_entries, current_bag):
    if target_bag in bag_entries[current_bag].keys():
        return True
    for bag in bag_entries[current_bag].keys():
        if can_have_target_bag(target_bag, bag_entries, bag):
            return True
    return False


def how_many_bags_inside(bag_type, bag_entries, known_bag_counts=None):
    if known_bag_counts is None:
        known_bag_counts = {}
    contains = 0
    for bag, count in bag_entries[bag_type].items():
        bag_contains = count
        if bag not in known_bag_counts:
            known_bag_counts[bag] = how_many_bags_inside(bag, bag_entries, known_bag_counts)
        bag_contains += known_bag_counts[bag] * count
        contains += bag_contains
    return contains


# This function is here to isolate and organize the puzzle solving logic after input parsing.
def solve_puzzle(bag_entries, puzzle_part=1):
    target_bag = "shiny gold bag"
    if puzzle_part == 1:
        can_contain_target_bag = 0
        for bag_type in bag_entries.keys():
            if can_have_target_bag(target_bag, bag_entries, bag_type):
                can_contain_target_bag += 1
        print(f"Total bag types that can contain a {target_bag} is {can_contain_target_bag}.")
    elif puzzle_part == 2:
        print(f"The total bags inside of {target_bag} is {how_many_bags_inside(target_bag, bag_entries)}")


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
