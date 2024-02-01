import json
import yaml


def pars_file(path_file):
    if str(path_file).endswith(".json"):
        return json.load(open(path_file))
    if str(path_file).endswith(".yaml"):
        return yaml.load(open(path_file), Loader=yaml.SafeLoader)
