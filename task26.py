def merge_dicts(a: dict, b: dict) -> dict:
    merged = a.copy()      # a ni nusxalab olamiz
    merged.update(b)       #
    return merged
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

result = merge_dicts(dict1, dict2)
print(result)
