def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result

words = ["salom", "kitob", "olma", "gul", "daraxt", "uy"]
result = group_by_length(words)
print(result)
