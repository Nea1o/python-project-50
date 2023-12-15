from gendiff.cli import argum_parse
from gendiff import generate_diff


def main():
    args = argum_parse()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
