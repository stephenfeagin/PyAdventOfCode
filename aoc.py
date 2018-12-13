import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("year", help="Desired year")
parser.add_argument("day", help="Desired day between 1 and 25, inclusive")
parser.add_argument("-f", "--file", help="Path to puzzle input (.txt)")
parser.add_argument("-q", "--quiet", help="Suppress messages?", action="store_true")

args = parser.parse_args()

available_years = ["2017", "2018"]

if args.year not in available_years:
    raise argparse.ArgumentTypeError(
        f"Invalid <year> argument: {args.year}. \n \
        <year> must be one of the following: {available_years}"
    )

try:
    if int(args.day) <= 25:
        args.day = args.day.rjust(2, "0")
    else:
        raise ValueError
except ValueError:
    raise argparse.ArgumentTypeError(
        f"Invalid <day> argument: {args.day}.\n \
        <day> must be an integer between 1 and 25, inclusive"
    )

if args.file is None:
    args.file = Path(f"./input-{args.year}/day_{args.day}.txt")
    if not args.quiet:
        print(f"No file provided. Attempting to locate input file {args.file}")

module = Path(f"./python/{args.year}/{args.day}.py")

try:
    with open(module, "r") as f:
        exec(f.read())
except FileNotFoundError:
    raise argparse.ArgumentTypeError(
        f"No Python solution for {args.year} / {args.day}"
    )
