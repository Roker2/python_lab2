def obj_to_json(obj):
    if (str(type(obj)) == '<class \'int\'>') | (str(type(obj)) == '<class \'float\'>') \
            | (str(type(obj)) == '<class \'long\'>'):
        return "\"number\": " + str(obj)
    if str(type(obj)) == '<class \'str\'>':
        return "\"string\": \"" + obj + "\""
