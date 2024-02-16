import argparse


def argum_parse():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument('-V', '--version', help='output the version number')
    parser.add_argument('-f', '--format', nargs='?', default='stylish',
                        help='output format (default: "stylish")', type=str)
    return parser.parse_args()

