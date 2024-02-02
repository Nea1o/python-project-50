import yaml
import json


def generate_diff(first_file, second_file):
    file1 = pars_file(first_file)
    file2 = pars_file(second_file)
    result_dict = {}
    for key in sorted(file1 | file2):
        if key not in file1 or key not in file2:
            if key in file1:
                result_dict[f"  - {key}"] = file1[key]
                print(result_dict[f"  - {key}"])
            if key in file2:
                result_dict[f"  + {key}"] = file2[key]
                print(result_dict[f"  + {key}"])
        if key in file1 and key in file2:
            result_dict[f"    {key}"] = file1[key]
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                generate_diff(file1[key], file2[key])
            else:
                result_dict[f"  - {key}"] = file1[key]
                result_dict[f"  + {key}"] = file2[key]

    result = stylish(result_dict)
    return result


"""        if key in file1 and key in file2 and file1[key] == file2[key]:
            print("2")
            result_dict[f"    {key}"] = file1[key]
            generate_diff(file1[key], file2[key])
        if key in file1 and key in file2 and file1[key] != file2[key]:
            print("3")
            result_dict[f"  - {key}"] = file1[key]
            result_dict[f"  + {key}"] = file2[key]"""


def dict_in_str(dct):
    result = "{ \n"
    for keys, values in dct.items():
        if type(values) is bool:
            result += f"{keys}: {str(values).lower()} \n"
        else:
            result += f"{keys}: {values} \n"
    result += "}"
    return result


def pars_file(path_file):
    if isinstance(path_file, str):
        if str(path_file).endswith(".json"):
            return json.load(open(path_file))
        if str(path_file).endswith(".yaml"):
            return yaml.load(open(path_file), Loader=yaml.SafeLoader)
    else:
        return path_file


def stylish(value, replacer='  ', space_count=1, _lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{replacer * space_count * _lvl}{el}: '
            result += stylish(val, replacer, space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        result = str(value)
    return result


print(stylish(generate_diff("/home/tosh/code/python-project-50/gendiff/tests/fixtures/file3.yaml",
                            "/home/tosh/code/python-project-50/gendiff/tests/fixtures/file4.yaml")))
