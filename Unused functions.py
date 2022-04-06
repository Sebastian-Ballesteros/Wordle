url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

def five_dict_create(url, word_length):
    punctuation = "&',.-()?1234567890"
    words = []
    with urlopen(url) as fp:
        for line in fp:
            line = line.decode('utf-8-sig').strip("b'\n ")
            for p in punctuation:
                line = line.replace(p, "hello world")
            line = line.lower()
            if len(line) == word_length:
                words.append(line)
    return list(np.unique(words))
