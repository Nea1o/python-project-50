import argparse

parser = argparse.ArgumentParser(
    prog="gendiff",
    description="Compares two configuration files and shows a difference.",
    epilog="test"
)
parser.add_argument("first_file", type=str, help="первое слово")
parser.add_argument("second_file", type=str, help="второе слово")
parser.add_argument("-f", "--format", type=str)
args = parser.parse_args()


def main(first, two):
    return f"{first} {two}"


if __name__ == "__main__":
    main(args.first_file, args.two_file)
