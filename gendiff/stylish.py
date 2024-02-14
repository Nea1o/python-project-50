def stylish(value, replacer='    ', space_count=1, level=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            if el[0] == "+":
                result += f'{replacer * space_count * (level - 1)}  + {el[2::]}: '
                result += stylish(val, replacer, space_count, level + 1) + '\n'
            elif el[0] == "-":
                result += f'{replacer * space_count * (level - 1)}  - {el[2::]}: '
                result += stylish(val, replacer, space_count, level + 1) + '\n'
            else:
                result += f'{replacer * space_count * level}{el}: '
                result += stylish(val, replacer, space_count, level + 1) + '\n'
        result += replacer * space_count * (level - 1) + '}'
    else:
        result = str(value)
    return result
