def count_names(names: list[str]) -> dict[str, int]:
    """ismlarni sanash

    Args:
        names (list[str]): ismlar royxati

    Returns:
        dict[str, int]: natijasi
    """
    result = {}
    for name in names:
        result[name] = names.count(name)
        
    return result

name_list = ["ali","jon","bek","bob","vali","jon","bek","bob","ali","jon","bek"]
result = count_names(name_list)
print(result)

