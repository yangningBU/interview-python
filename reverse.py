# reverse (no built-in functions or slicing)
def reverse(string):
    reversed = []
    for i, _ in enumerate(string):
        reversed.append(string[len(string) - 1 - i])
    return "".join(reversed)

first = "Merry Christmas"
second = "samtsirhC yrreM"
print(reverse(first) == second)
