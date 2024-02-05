import yaml
import json


def generate_diff(first_file, second_file):
    result_dict = {}
    file1 = pars_file(first_file)
    file2 = pars_file(second_file)
    for key in sorted(file1 | file2):
        if key not in file1:
            result_dict[f"+ {key}"] = file2[key]
        elif key not in file2:
            result_dict[f"- {key}"] = file1[key]
        elif file1[key] == file2[key]:
            result_dict[f"{key}"] = file1[key]
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result_dict[f"{key}"] = generate_diff(file1[key], file2[key])
        elif key in file1 and key in file2:
            result_dict[f"- {key}"] = file1[key]
            result_dict[f"+ {key}"] = file2[key]
    return result_dict


def pars_file(path_file):
    if isinstance(path_file, str):
        if str(path_file).endswith(".json"):
            return json.load(open(path_file))
        if str(path_file).endswith(".yaml"):
            return yaml.load(open(path_file), Loader=yaml.SafeLoader)
    else:
        return path_file


def stylish(value, replacer='    ', space_count=1, level=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            if el[0] == "+":
                result += f'{replacer * space_count * (level-1)}  + {el[2::]}: '
                result += stylish(val, replacer, space_count, level + 1) + '\n'
            elif el[0] == "-":
                result += f'{replacer * space_count * (level-1)}  - {el[2::]}: '
                result += stylish(val, replacer, space_count, level + 1) + '\n'
            else:
                result += f'{replacer * space_count * level}{el}: '
                result += stylish(val, replacer, space_count, level + 1) + '\n'
        result += replacer * space_count * (level - 1) + '}'
    else:
        result = str(value)
    return result


print(stylish(generate_diff("/home/tosh/code/python-project-50/gendiff/tests/fixtures/file3.yaml",
                            "/home/tosh/code/python-project-50/gendiff/tests/fixtures/file4.yaml")))
