import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    result_dict = {}
    for key in sorted(file1 | file2):
        if key in file1 and key not in file2:
            result_dict[f"  - {key}"] = file1[key]
        if key in file2 and key not in file1:
            result_dict[f"  + {key}"] = file2[key]
        if key in file1 and key in file2 and file1[key] == file2[key]:
            result_dict[f"    {key}"] = file1[key]
        if key in file1 and key in file2 and file1[key] != file2[key]:
            result_dict[f"  - {key}"] = file1[key]
            result_dict[f"  + {key}"] = file2[key]
    result = dict_in_str(result_dict)
    return result


def dict_in_str(dct):
    result = "{ \n"
    for keys, values in dct.items():
        if type(values) == bool:
            result += f"{keys}: {str(values).lower()} \n"
        else:
            result += f"{keys}: {values} \n"
    result += "}"
    return result
