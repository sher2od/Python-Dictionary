def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result = {}
    for index, number in enumerate(numbers):
        if number not in result:
            result[number] = []
        result[number].append(index)
    return result

input_str = input("Sonlarni kiriting (boshliq bilan): ")
enter_nums = list(map(int, input_str.split()))

result = group_indices(enter_nums)
print(result)





