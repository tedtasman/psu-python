from psu_python import *

def process_text(text: str) -> str:
    """Remove every 3rd word from a string
    """
    words = split(text)
    i = 2
    while i < len(words):
        pop_index(words, i)
        i += 2
    
    return join(words, ",")


def difference_dicts(dict1: dict, dict2: dict) -> dict:
    """Take the difference of every matching value in two dictionaries, filtering out negatives
    """
    diff_dict = {}

    for key, value in get_items(dict1):
        diff_dict[key] = value - get_value(dict2, key, 0)
    
    for key, value in get_items(dict2):
        if key not in diff_dict:
            diff_dict[key] = -dict2[key]

    negatives = []
    for key, value in get_items(diff_dict):
        if value < 0:
            append(negatives, key)
    
    for key in negatives:
        pop_key(diff_dict, key)

    return diff_dict

print(process_text("hello my name is ted and this is a test"))
print(difference_dicts(
    dict(a=10, b=2, c=10),
    dict(b=3, c=5, d=6)
))