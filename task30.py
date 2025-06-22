def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}
    for key, value in d.items():
        if value != 0:
            result[key] = value
    return result
data = {"a": 3, "b": 0, "c": 5, "d": 0}
filtered = filter_non_zero(data)
print(filtered)
