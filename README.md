# Advent Of Code Practice Project
## Overview
Side project of trying out the solutions I come up with for the AOC puzzles.
If you find these useful, please let me know. I will try to make most solutions
work off of the `template.py` file I have which means they should all have the
same usage pattern unless the puzzle makes the template a terrible fit.

TODO: Find a way to standardize exceptions to the template.

## Usage
    python ./<year>/<day>/aoc_<year>_<day>.py -i <input_file> -p <part_number>
Where...
* `<year>` is the year the puzzle was published
* `<day>` is the day in December of `<year>` the puzzle was published
  * If `<day>` is less than 10, include a leading 0 such as `01` for the first day.
* `<input_file>` is the path to file containing the puzzle input
  * Solution scripts will usually come with a small input file containing an example
    extracted from the puzzle description called `example_input.txt` and a large
    input file containing the real puzzle input called `puzzle_input.txt`.
* `<part_number>` is the puzzle part you want the solution for, usually 1 or 2

You can also usually use the `-h` or `--help` flag on the individual scripts to get
the usage specific to that script. If a puzzle solution script has a non-standard
usage, this is how you would find out. For example, if you wanted to know how to use
the script specifically for the first day of the 2020 puzzles, you would use...

    python ./2020/01/aoc_2020_01.py -h

## License and legal usage
I was originally going to release this under the beerware license but considering
there might be some folks out there that have to run all their code references by
a legal department, I kept it simple with the BSD 3 Clause License. Still feel free
to buy me a beer if you happen to be in the same place and you found this useful.
Here's the legal summary from `tldrlegal.com`:

"The BSD 3-clause license allows you almost unlimited freedom with the software
so long as you include the BSD copyright and license notice in it (found in
Fulltext). "

## TODO List
* Catch up on previous years' challenges.
* Make a generic puzzle runner that can run from the project root
* Add proper testing setup for unit testing, etc