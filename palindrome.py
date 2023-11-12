import re

def palindrome(word):
    clean = re.sub(r'(\W|\s)', '', word.strip().lower())
    return clean == clean[::-1]

print(palindrome("A man, a plan, a canal Panama"))
