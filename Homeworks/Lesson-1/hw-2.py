from string import ascii_lowercase as al

def play(words: list[str]) -> list[int]:
    good_words = []
    errors = []
    for n, word in enumerate(words):
        if len(word) != len(list(filter(lambda x: x in al, list(word)))):
            errors.append(n + 1)
            continue
        if word in good_words:
            errors.append(n + 1)
            continue
        if good_words:
            if good_words[-1][-1].lower() != word[0].lower():
                errors.append(n + 1)
                continue
        good_words.append(word)
    return errors