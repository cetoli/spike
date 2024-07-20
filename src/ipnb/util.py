import numpy as np
GLOVE = "/home/carlo/Documentos/inpe/cbow_s50.txt"


def gimme_glove():
    with open(GLOVE, encoding='utf-8') as glove_raw:
        for line in glove_raw.readlines():
            splitting = line.split(' ')
            yield splitting[0], np.array(splitting[1:], dtype=float)


GLOVER = {w: x for w, x in gimme_glove()}


def tokenize_into_words(text):
    def tokenize(poems):
        from string import punctuation
        import stop_words
        stopwords = stop_words.get_stop_words('portuguese')
        xtr = "nº cada si toda todas et al ii iii iv v vi vii viii ix xi xii xiii é a b c d e f g h i j x y z".split()
        stopwords.extend(xtr)

        def tokenize_poem(poem):
            poem = poem.lower().replace('\n', ' ')
            pontos = punctuation.replace("-", "") + '●■○'
            # print(pontos)
            for sign in pontos:
                poem = poem.replace(sign, ' ')
            tokens = poem.split()
            tokens = [tt for tt in tokens if
                      (tt != '') and (tt not in stopwords) and tt.isalpha()]
            return tokens

        return tokenize_poem(poems)
    return tokenize(text)


def euclid(vec0, vec1):
    return np.linalg.norm(vec0 - vec1)


def vetorize(tokens):
    _words = [w for w in np.unique(tokens) if w in GLOVER]
    return np.array([GLOVER[w] for w in _words]).mean(axis=0)


def vetorizes(words):

    def poem_to_vec(tokens):
        _words = [w for w in np.unique(tokens) if w in GLOVER]
        return np.array([GLOVER[w] for w in _words])

    word_vector = [poem_to_vec(tokenized).mean(axis=0) for tokenized in words]
    return np.array(word_vector)
