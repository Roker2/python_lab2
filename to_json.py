def obj_to_json(obj):
    print(type(obj))
    if (str(type(obj)) == '<class \'int\'>') | (str(type(obj)) == '<class \'float\'>') \
            | (str(type(obj)) == '<class \'long\'>'):
        return "\"number\": " + str(obj)
    if str(type(obj)) == '<class \'str\'>':
        return "\"string\": \"" + obj + "\""
    if str(type(obj)) == '<class \'bool\'>':
        return "\"boolean\": " + str(obj).lower()
    if str(type(obj)) == '<class \'list\'>':
        string = "\"array\": [\n"
        for i in range(0, len(obj) - 1):
            string += obj_to_json(obj[i]) + ",\n"
        string += obj_to_json(obj[len(obj) - 1]) + "\n]"
        return string


def obj_with_to_json(obj, key):
    print(str(type(obj)) + key)
    if (str(type(obj)) == '<class \'int\'>') | (str(type(obj)) == '<class \'float\'>') \
            | (str(type(obj)) == '<class \'long\'>'):
        return "\"" + key + "\": " + str(obj)
    if str(type(obj)) == '<class \'str\'>':
        return "\"" + key + "\": \"" + obj + "\""
    if str(type(obj)) == '<class \'bool\'>':
        return "\"" + key + "\": " + str(obj).lower()
    if str(type(obj)) == '<class \'list\'>':
        string = "\"" + key + "\": [\n"
        for i in range(0, len(obj) - 1):
            string += obj_to_json(obj[i]) + ",\n"
        string += obj_to_json(obj[len(obj) - 1]) + "\n]"
        return string
