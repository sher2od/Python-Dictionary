
def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}
    for person in people:
        age = person["age"]
        name = person["name"]
        if age not in result:
            result[age] = []
        result[age].append(name)
    return result


person = [
    {"name": "ali", "age": 20},
    {"name": "vali", "age": 19},
    {"name": "bek", "age": 21},
    {"name": "jon", "age": 22}
]

result = group_by_age(person)
print(result)


