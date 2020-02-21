def obj_to_json(obj):
    # print(type(obj))
    if (str(type(obj)) == '<class \'int\'>') | (str(type(obj)) == '<class \'float\'>') \
            | (str(type(obj)) == '<class \'long\'>'):
        return "\"number\": " + str(obj)
    if str(type(obj)) == '<class \'str\'>':
        return str_to_json(obj)
    if str(type(obj)) == '<class \'bool\'>':
        return bool_to_json(obj)
    if str(type(obj)) == '<class \'list\'>':
        return list_to_json(obj)
    if str(type(obj)) == '<class \'dict\'>':
        return dict_to_json(obj)


def obj_with_to_json(obj, key):
    # print(str(type(obj)) + key)
    if (str(type(obj)) == '<class \'int\'>') | (str(type(obj)) == '<class \'float\'>') \
            | (str(type(obj)) == '<class \'long\'>'):
        return "\"" + key + "\": " + str(obj)
    if str(type(obj)) == '<class \'str\'>':
        return str_to_json(obj, key)
    if str(type(obj)) == '<class \'bool\'>':
        return bool_to_json(obj, key)
    if str(type(obj)) == '<class \'list\'>':
        return list_to_json(obj, key)
    if str(type(obj)) == '<class \'dict\'>':
        return dict_to_json(obj, key)


def str_to_json(obj, key="string"):
    return "\"" + key + "\": \"" + obj + "\""


def bool_to_json(obj, key="boolean"):
    return "\"" + key + "\": " + str(obj).lower()


def list_to_json(obj, key="array"):
    string = "\"" + key + "\": [\n"
    for i in range(0, len(obj) - 1):
        string += obj_to_json(obj[i]) + ",\n"
    string += obj_to_json(obj[len(obj) - 1]) + "\n]"
    return string


def dict_to_json(obj, key="object"):
    string = "\"" + key + "\": {\n"
    for key in dict(obj).keys():
        string += obj_with_to_json(obj[key], key) + ",\n"
    string = string[:(len(string) - 2)] + string[(len(string) - 2):].replace(",\n", "")
    string += "\n}"
    return string
