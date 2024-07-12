""" Configuration for project Inep.

Changelog
---------
.. versionadded::    24.07
    |br| first version of main (11)

|   **Open Source Notification:** This file is part of open source program **INEP**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
STOPWORDS = "https://gitlab.com/cetoli/spike/-/raw/master/src/neurocomp/conf/stopwords.txt"
"""Remove as stopwords da especificação"""
from configuration import TXT, TAG
from collections import Counter


class Text:
    TEXT = None

    def __init__(self):
        Text.TEXT = self if not Text.TEXT else Text.TEXT
        tags = " " + " ".join([a for _, a in TAG])
        self.original = TXT + tags
        self.clean = None

    def cleaner(self):
        import stop_words
        from string import punctuation
        stop = stop_words.get_stop_words('portuguese')

        # tx = Text()
        Text.TEXT = self
        text = self.original
        body = text.lower()  # .decode('utf-8')
        for sign in punctuation:
            body = body.replace(sign, "0")
        stop = stop + "através mediante incluir conclusão perfil".split()
        print('stops', stop[-20:])
        body = body.lower().replace('\n', ' ')
        list_body = body.split()

        # list_body = self.tokenize()
        # print(list_body[:40])
        # clean = u"{}".format(word) for word in list_body if word not in stop
        clean = [word for word in list_body if (word not in stop)
                 and ("\xa0" not in word) and ("<" not in word) and (word.isalpha())]
        # clean = list_body
        # print(clean[:40])
        self.original = clean
        self.clean = count = Counter(clean)
        tup = list(count.items())
        tup.sort(key=lambda x: x[1], reverse=True)
        print(tup[:100])
        return count


class SurveyText:
    """
    Varredura do texto

    O texto será percorrido usando uma janela de pertinência centrada em cada palavra
    """

    def __init__(self, text_dictionary, relevancy=2):
        def strip(w):
            return w[:-2] if w.endswith("es") else w[:-1] if w.endswith("s") else w

        self.text = text_dictionary
        self.relevant = [strip(word) for word, cnt in self.text.items() if cnt >= relevancy]
        self.pairs, self.levels = {}, {}
    '''
    def survey(self, window=10, forte=8):
        size = len(self.relevant)
        for here, word in enumerate(self.relevant):
            start = here - window if here >= window else 0
            ender = here + window if here + window <= size else size
            for other in self.relevant[start:ender]:
                if other == word:
                    continue
                entry = (other, word) if other < word else (word, other)
                self.pairs[entry] = self.pairs.setdefault(entry, 0) + 1
        self.levels = Counter([i for (i, j), _ in self.pairs.items()])
        levels = Counter([j for (i, j), _ in self.pairs.items()])
        levels.update({key: value for key, value in self.levels.items() if key not in levels})
        levels = {key: (levels[key] + self.levels.setdefault(key, 0)) for key in levels}
        self.levels = {key: value // 6 - 1 for key, value in levels.items() if value > forte}
    '''
    def survey(self, window=10, forte=8):
        original = Text.TEXT.original
        size = len(original)
        print("survey", size, original[:300])
        rlv = self.relevant
        for here, word in enumerate(original):
            start = here - window if here >= window else 0
            ender = here + window if here + window <= size else size
            for other in original[start:ender]:
                if other == word or other not in rlv or word not in rlv:
                    continue
                entry = (other, word) if other < word else (word, other)
                self.pairs[entry] = self.pairs.setdefault(entry, 0) + 1
        self.levels = Counter([i for (i, j), _ in self.pairs.items()])
        levels = Counter([j for (i, j), _ in self.pairs.items()])
        levels.update({key: value for key, value in self.levels.items() if key not in levels})
        levels = {key: (levels[key] + self.levels.setdefault(key, 0)) for key in levels}
        self.levels = {key: value // 6 - 1 for key, value in levels.items() if value > forte}

    def nodes(self, relevancy=2):
        # node = {name[0]: good for name, good in self.pairs.items() if good>relevancy}
        relevant = {na: good for (na, _), good in self.pairs.items() if good > relevancy}
        relevant.update({na: good for (_, na), good in self.pairs.items() if good > relevancy})
        node = {name: good for name, good in self.levels.items() if name in relevant}
        node = ({nd: cnt for nd, cnt in self.levels.items() if nd in node})
        # node.update({name[1]: good if good > node.setdefault(name[1], 0) else node[name[1]]
        #              for name, good in self.pairs.items() if good>relevancy})
        # return node.keys()
        # return node.items()
        # return self.levels.items()
        return node.items()

    def show(self, relevancy=20):
        tuple_list = list(self.pairs.items())
        # tuple_list = tuple_list.sort(key = lambda x: x[1], reverse=True)
        tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
        _list = [(_tuple[0], _tuple[1], good) for _tuple, good in tuple_list if good > relevancy]
        return _list

    # noinspection SpellCheckingInspection
    def paint(self, window=10, relevancy=20, cof=40):
        _ = self  # void statement to fool lint inspector
        st = SurveyText(Text.TEXT.clean)
        st.survey(window)
        print(st.show(relevancy))  # [:200])
        # print(st.nodes())

        import networkx as nx  # importing networkx package
        import matplotlib.pyplot as plt  # importing matplotlib package and pyplot is for displaying the graph on canvas
        # matrix = "yyyycccccccmmmmmmmmbbbbbbbbbggggggggggggrrrrrrrrrrrrrrrrrrr"
        matrix = "ycmgbr"*20
        lm = len(matrix)-1
        colors = {wg: cl for wg, cl in enumerate(matrix)}
        plt.rcParams["figure.figsize"] = [15.50, 8.50]
        plt.rcParams["figure.autolayout"] = True
        wg = nx.Graph()
        _ = [wg.add_node(node, size=size) for node, size in st.nodes(relevancy)]
        _ = [wg.add_edge(a, b, color=colors[max(lm, w-cof)], weight=w-cof) for a, b, w in st.show(relevancy)]
        sizes = [wg.nodes[s]['size'] * 100 for s in wg.nodes]
        color = [colors[wg.nodes[s]['size']] for s in wg.nodes]

        '''Node can be called by any python-hashable obj like string,number etc'''
        nx.draw(wg, with_labels=True, node_size=sizes, node_color=color)
        # draws the networkx graph containing nodes which are declared till before
        plt.show()  # displays the networkx graph on matplotlib canvas


def main():
    tx = Text().cleaner()
    sv = SurveyText(tx)
    sv.survey(20)
    sv.nodes(4)
    # [print(nd) for nd in sv.nodes(20)]
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # [print(nd) for nd in sv.show(40)]
    sv.paint(relevancy=8, cof=20)


if __name__ == '__main__':
    main()
