import json
import yaml





file_1 = yaml.load(open("/home/tosh/code/python-project-50/gendiff/tests/fixtures/file3.yaml"), Loader=yaml.SafeLoader)
file_2 = yaml.load(open("/home/tosh/code/python-project-50/gendiff/tests/fixtures/file4.yaml"), Loader=yaml.SafeLoader)
print(file_1)
print(file_2)
