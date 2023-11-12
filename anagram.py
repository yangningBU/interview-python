def is_anagram(first, second):
    return sorted(first) == sorted(second)

first = "not"
second = "ton"
third = "ate"
fourth = "eat"
fifth = "other"

print(is_anagram(first, second))
print(is_anagram(third, fourth))
print(not is_anagram(fourth, fifth))
