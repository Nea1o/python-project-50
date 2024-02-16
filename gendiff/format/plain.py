import json

import yaml


def plain_format(value, replacer='    ', space_count=1, level=1):
    if isinstance(value, dict):
        result = '{\n'
        result_plain = ''
        for el, val in value.items():
            if el[0] == "+":
                result += f'{replacer * space_count * (level - 1)} ' \
                          f' + {el[2::]}: '
                result += plain_format(val, replacer, space_count, level + 1) + '\n'
                if isinstance(val, dict):
                    result_plain += f"Property {el} was added with value: [complex value]"
                    result_plain += '\n'
                else:
                    result_plain += f"Property {el} was added with value {val}"
                    result_plain += '\n'
            elif el[0] == "-":
                result += f'{replacer * space_count * (level - 1)}' \
                          f'  - {el[2::]}: '
                result += plain_format(val, replacer, space_count, level + 1) + '\n'
                if isinstance(val, dict):
                    result_plain += f"Property {el} was removed with value: [complex value]"
                    result_plain += '\n'
                else:
                    result_plain += f"Property {el} was removed with value {val}"
                    result_plain += '\n'
            else:
                result += f'{replacer * space_count * level}{el}: '
                result += plain_format(val, replacer, space_count, level + 1) + '\n'
                result_plain += '\n'
                result_plain += f"Property {el} was updated with value {val}"

        result += replacer * space_count * (level - 1) + '}'
    else:
        result = str(value)
        result_plain = str(value)
    return result_plain


def pars_file1(path_file):
    if isinstance(path_file, str):
        if str(path_file).endswith(".json"):
            return json.load(open(path_file))
        if str(path_file).endswith(".yaml"):
            return yaml.load(open(path_file), Loader=yaml.SafeLoader)
    else:
        return path_file


def generate_diff1(first_file, second_file):
    result_dict = {}
    file1 = pars_file1(first_file)
    file2 = pars_file1(second_file)
    for key in sorted(file1 | file2):
        if key not in file1:
            result_dict[f"+ {key}"] = file2[key]
        elif key not in file2:
            result_dict[f"- {key}"] = file1[key]
        elif file1[key] == file2[key]:
            result_dict[f"{key}"] = file1[key]
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result_dict[f"{key}"] = generate_diff1(file1[key], file2[key])
        elif key in file1 and key in file2:
            result_dict[f"- {key}"] = file1[key]
            result_dict[f"+ {key}"] = file2[key]
    return plain_format(result_dict)


print(generate_diff1(first_file='/home/tosh/code/python-project-50/gendiff/tests/fixtures/file3.json',
                     second_file='/home/tosh/code/python-project-50/gendiff/tests/fixtures/file4.json', ))
