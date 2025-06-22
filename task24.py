def most_common_char(text: str) -> str:
    collections = {}
    for ch in text:
        collections[ch] = text.count(ch)
    
    most_char = collections[text[0]]
    for ch in text:
        if collections[ch] > most_char:
            most_char = collections[ch]
    
    return most_char

text = "kdjfgnbqiuerskjfvkjqbhsmdjbhv"
result = most_common_char(text)
print(result)

