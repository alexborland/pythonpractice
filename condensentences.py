def get_input():
    sentences = []
    i = "init"
    while i != "":
        i = input("> ")
        sentences.append(i)
    del sentences[-1]
    return sentences

def left(word, size):
    if size > len(word):
        return word
    else:
        return word[:size]

def right(word, size):
    if size > len(word):
        return word
    else:
        return word[-size:]

def condense_sentence(sentence):
    words = sentence.split(" ")
    new_sentence = words[:]
    for i in range(len(words) - 1):
        for j in range(len(words[i]), 0, -1):
            if right(words[i], j) == left(words[i+1], j):
                new_sentence[i] = words[i] + right(words[i+1], len(words[i+1])-j)
                new_sentence[i+1] = ""
                break
    while "" in new_sentence:
        new_sentence.remove("")
    new_sentence = " ".join(new_sentence)
    if new_sentence == sentence:
        return sentence
    else:
        return condense_sentence(new_sentence)

for sentence in get_input():
    print(condense_sentence(sentence))
            
