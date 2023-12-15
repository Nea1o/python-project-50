import argparse


def argum_parse():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
        epilog="test"
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument('-f', '--format', help='set format of output', type=str)
    return parser.parse_args()
