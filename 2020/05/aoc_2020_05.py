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


def parse_ticket(ticket_string):
    bit_7_values = [64, 32, 16, 8, 4, 2, 1]
    bit_3_values = [4, 2, 1]
    ticket_row_string = ticket_string[:7]
    ticket_col_string = ticket_string[7:]
    row_number = 0
    col_number = 0
    for i in range(0, 7):
        print(ticket_row_string[i], end="")
        if ticket_row_string[i] == 'B':
            row_number += bit_7_values[i]
    print("-", end="")
    for i in range(0, 3):
        print(ticket_col_string[i], end="")
        if ticket_col_string[i] == 'R':
            col_number += bit_3_values[i]
    print("\n")
    return {
        'row': row_number,
        'col': col_number,
        'id': row_number * 8 + col_number
    }


def main():
    args = parse_args()
    ticket_seats = []
    for line in args.input:
        ticket_seats.append(parse_ticket(line.strip()))
    seat_ids = []
    for seat in ticket_seats:
        if seat['id'] == 561 or seat['id'] == 563:
            print(seat)
        seat_ids.append(seat['id'])
    print(str(max(seat_ids)))
    seat_ids = sorted(seat_ids)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
