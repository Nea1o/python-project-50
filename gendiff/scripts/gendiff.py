import argparse
from gendiff.generate import generate_diff

parser = argparse.ArgumentParser(
    prog="gendiff",
    description="Compares two configuration files and shows a difference.",
    epilog="test"
)
parser.add_argument("first_file", type=str)
parser.add_argument("second_file", type=str)
parser.add_argument("-f", "--format", type=str)
args = parser.parse_args()


def main(file1, file2):
    return generate_diff(file1, file2)


if __name__ == "__main__":
    main(args.first_file, args.second_file)
