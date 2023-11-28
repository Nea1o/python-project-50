import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    result_dict = {}
    for key in sorted(file1 | file2):
        if key in file1 and key not in file2:
            result_dict[f"- {key}"] = file1[key]
        if key in file2 and key not in file1:
            result_dict[f"+ {key}"] = file2[key]
        if key in file1 and key in file2 and file1[key] == file2[key]:
            result_dict[f"  {key}"] = file1[key]
        if key in file1 and key in file2 and file1[key] != file2[key]:
            result_dict[f"- {key}"] = file1[key]
            result_dict[f"+ {key}"] = file2[key]
    print(result_dict)
    return result_dict
