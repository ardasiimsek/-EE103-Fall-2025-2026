# Tuples: Returning more than one value


def name_splitter(full_name):
    """ Returns (first_name, surname). Everything before the last space
    is the first name, so 'Ali Can Yilmaz' -> ('Ali Can', 'Yilmaz') """
    full_name = full_name.strip()
    space = full_name.rfind(' ')
    if space == -1:
        return (full_name, '')
    first_name = full_name[:space]
    surname = full_name[space + 1:]
    return (first_name, surname)


def char_counts(s):
    """ s is a string of lowercase chars
    Return a tuple where the first element is the number of vowels in s and
    the second element is the number of consonants in s """
    vowels = 0
    consonants = 0
    for ch in s:
        if ch in "aeiou":
            vowels += 1
        elif 'a' <= ch <= 'z':     # skip spaces, digits etc.
            consonants += 1
    return (vowels, consonants)


first, last = name_splitter("Arda Simsek")
print(f"First name: {first}, Surname: {last}")
print(name_splitter("Ali Can Yilmaz"))

print(char_counts("abcd"))            # (1, 3)
print(char_counts("programming"))     # (3, 8)
