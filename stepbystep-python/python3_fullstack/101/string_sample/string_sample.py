def find(source_str, wanted_str):
    for item in source_str:
        if item == wanted_str:
            return wanted_str + ' is found'

        return wanted_str + ' is not found'
