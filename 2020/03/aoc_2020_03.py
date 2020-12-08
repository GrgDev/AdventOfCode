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


def print_map(tree_map, x, y):
    print("*" * len(tree_map[0]))
    print(f"({x}, {y})")
    for line in tree_map:
        print(line)
    print("*" * len(tree_map[0]))


def tree_map_count(tile_map, slope_x, slope_y):
    tree_map = tile_map
    pos_x = 0
    pos_y = 0
    move_x = slope_x
    move_y = slope_y
    tree_count = 0
    finish_row = len(tree_map)
    while pos_y < finish_row:
        map_line = tree_map[pos_y]
        symbol = map_line[pos_x % len(map_line)]
        if symbol == '#':
            tree_count += 1
            symbol = 'X'
        else:
            symbol = 'O'
        #map_line = map_line[:pos_x % len(map_line)] + symbol + map_line[(pos_x % len(map_line)) + 1:]
        tree_map[pos_y] = map_line
        #print_map(tree_map, pos_x, pos_y)
        pos_x += move_x
        pos_y += move_y
    print(f"Tree count for slope ({slope_x}, {slope_y}): {tree_count}")
    return tree_count


def main():
    args = parse_args()
    tree_map = []
    tree_multiple = 1
    for line in args.input:
        tree_map.append(line.strip())
    tree_multiple *= tree_map_count(tree_map, 1, 1)
    tree_multiple *= tree_map_count(tree_map, 3, 1)
    tree_multiple *= tree_map_count(tree_map, 5, 1)
    tree_multiple *= tree_map_count(tree_map, 7, 1)
    tree_multiple *= tree_map_count(tree_map, 1, 2)
    print(f"Tree multiple = {tree_multiple}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
