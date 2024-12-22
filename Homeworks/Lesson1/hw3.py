import random


def learn(dataset: list[str]):
    begins = []
    ends = []
    word_pairs = dict()
    for sentence in dataset:
        begins.append(sentence.split()[0])
        ends.append(sentence.split()[-1])
        for n, word in enumerate(sentence.split()):
            # Очень плохая конструкция :>
            try:
                word_pairs[word].append(sentence.split()[n + 1])
            except IndexError:
                word_pairs[word].append(".")
            except Exception:
                try:
                    word_pairs[word] = [sentence.split()[n + 1]]
                except IndexError:
                    word_pairs[word] = ["."]
    return begins, ends, word_pairs


def generate(state: tuple[list, list, dict]) -> str:
    sentence = [random.choice(state[0])]
    while True:
        if sentence[-1] == ".":
            sentence = sentence[:-1]
            break
        sentence.append(random.choice(state[2][sentence[-1]]))
    return " ".join(sentence)