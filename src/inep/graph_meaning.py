# noinspection SpellCheckingInspection
""" Configuration for project Inep.

Changelog
---------
.. versionadded::    24.07
    |br| first version of main (11)
    |br| added trim and rebuff (15)
    |br| review relevancy, equalize entries (18)

|   **Open Source Notification:** This file is part of open source program **INEP**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from cmath import log
from itertools import chain as ch
from configuration import TXT, TAG
from collections import Counter
STOPWORDS = "https://gitlab.com/cetoli/spike/-/raw/master/src/neurocomp/conf/stopwords.txt"
"""Remove as stopwords da especificação"""


def scan(here, word, original_text, word_relevancy_list, scanning_window, size):
    start, ender = max(0, here - scanning_window), min(size, here + scanning_window)
    return [min((other, word), (word, other))
            for other in original_text[start:ender]
            if other != word and other in word_relevancy_list and word in word_relevancy_list
            ]


class Text:
    """
    Limpeza e tokenization do texto

    Remove palavras de ligação
    """
    TEXT = None

    def __init__(self, txt=None):
        Text.TEXT = self if not Text.TEXT else Text.TEXT
        tags = " " + " ".join([a for _, a in TAG])
        self.original = txt or (TXT + tags)
        self.clean = None

    def cleaner(self):
        import stop_words
        from string import punctuation
        stop = stop_words.get_stop_words('portuguese')
        xtr = "nº cada si toda todas et al ii iii iv v vi vii viii ix xi xii xiii é a b c d e f g h i j x y z".split()
        stop.extend(xtr)

        # tx = Text()
        Text.TEXT = self
        text = self.original
        body = text.lower()  # .decode('utf-8')
        pontos = punctuation.replace("-", "") + '●'
        for sign in pontos:
            body = body.replace(sign, "")
        stop = stop + "através mediante incluir conclusão perfil".split()
        # print('stops', stop[-20:])
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
        # print(tup[:100])
        return count


class SurveyText:
    """
    Varredura do texto

    O texto será percorrido usando uma janela de pertinência centrada em cada palavra
    """

    def __init__(self, text_dictionary, original, relevancy=2):
        def strip(w):
            return w[:-2] if w.endswith("es") else w[:-1] if w.endswith("s") else w

        self.text = text_dictionary
        self.relevant = [strip(word) for word, cnt in self.text.items() if cnt >= relevancy]
        self.pairs, self.levels = {}, {}
        self.good = self.relevant
        self.relevancy = relevancy
        self.original = original

    def survey(self, window=10, forte=8):
        original = self.original
        size = len(original)
        # print("survey", size, original[:300])
        rlv = self.relevant
        import multiprocessing as mp
        # print("Number of processors: ", mp.cpu_count())
        pool = mp.Pool(mp.cpu_count())
        # pairs = [scanner(here, word, original, rlv, window, size) for here, word in enumerate(original)]
        pairs = pool.starmap(scan, [(here, word, original, rlv, window, size) for here, word in enumerate(original)])
        self.pairs = Counter(ch.from_iterable(pairs))
        # print([(a, b, c) for (a, b), c in self.pairs.items() if c > 20])
        pool.close()
        self.levels = Counter([i for (i, j), _ in self.pairs.items()])
        levels = Counter([j for (i, j), _ in self.pairs.items()])
        levels.update({key: value for key, value in self.levels.items() if key not in levels})
        levels = {key: (levels[key] + self.levels.setdefault(key, 0)) for key in levels}
        self.levels = {key: value // 6 - 1 for key, value in levels.items() if value > forte}

    def nodes(self, relevancy=2):
        relevant = {na: good for (na, nb), good in self.pairs.items()
                    if (good > relevancy) and (na in self.good) and (nb in self.good)
                    }
        relevant.update({na: good for (_, na), good in self.pairs.items() if good > relevancy and na in self.good})
        node = {name: good for name, good in self.levels.items() if name in relevant}
        # node = ({nd: cnt for nd, cnt in self.levels.items() if nd in node})
        return node.items()

    def show(self, relevancy=None):
        relevancy = relevancy or self.relevancy
        tuple_list = list(self.pairs.items())
        # tuple_list = tuple_list.sort(key = lambda x: x[1], reverse=True)
        tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
        _list = [(na, nb, good) for (na, nb), good in tuple_list
                 if (good > relevancy) and (na in self.good) and (nb in self.good)]
        return _list

    def trim(self, relevancy=None):
        relevancy = relevancy or self.relevancy
        relevant = self.show(relevancy=relevancy)
        relevant = [a for a, *_ in relevant]+[a for _, a, *_ in relevant]
        print(len(relevant))
        return list(set(relevant))

    def rebuff(self, window=4):
        def find_all(a_str, sub):
            start = 0
            while True:
                start = a_str.find(sub, start)
                if start == -1:
                    return
                yield start
                start += len(sub)  # use start += 1 to find overlapping matches

        mark = self.trim()
        original_text = " ".join(self.original)
        original = self.original
        rebuffed = []
        end = len(original)
        for word in mark:
            for begin in find_all(original_text, word):
                rebuffed.extend(original[max(0, begin-window):min(end, begin+window)])
        self.relevant = list(set(rebuffed))
        return self.relevant

    # noinspection SpellCheckingInspection
    def paint(self, relevancy=20, cof=90, top=80, size=30):
        # print(self.show(relevancy))  # [:200])
        import networkx as nx  # importing networkx package
        import matplotlib.pyplot as plt  # importing matplotlib package and pyplot is for displaying the graph on canvas
        import matplotlib
        ma = [x for x in matplotlib.colors.ColorConverter.colors.keys() if len(x) == 1]
        print(ma)
        matrix = "ycmgbr"*2000
        lm = len(matrix)-1
        colors = {wg: cl for wg, cl in enumerate(matrix)}
        col = [colors[min(lm, max(1, w-cof))] for _, __, w in self.show(relevancy)]
        plt.rcParams["figure.figsize"] = [15.50, 8.50]
        plt.rcParams["figure.autolayout"] = True
        wg = nx.Graph()
        skp = [
            'bloco', 'learning', 'além', 'oreilly', 'aluno', 'ser', 'área', 'disso', 'ainda', 'ed', 'durante',
            'instituição', 'aluno', 'reilly', 'view', 'oreilly', 'library', 'segurança', 'assim', 'contínua',
            'instituição', 'and', 'área', 'base', 'disponível', 'informação', 'curso', 'trabalho',
            'partir', 'processo', 'tempo', 'graduação', 'título', 'sendo', 'melhoria', 'própria', 'acordo',
            'longo', 'meio', 'professor', 'ensino', 'aprendizagem', 'coordenação', 'mercado', 'distância',
            'equipe', 'serviço', 'social', 'prática', 'forma', 'todo', 'parte', 'perfil', 'rede', 'egresso',
            'of', 'acesso', 'p', 'sempre', 'aprendizado', 'tanto', 'organização', 'arquitetura', 'educacional',
            'programa', 'bem', 'management', 'relação', 'sobre', 'guide', 'the', 'corpo',
            'security', 'curso', 'acervo', 'curricular', 'rio', 'janeiro', 'nível', 'modo', 'm',
            'lgpd', 'avaliação', 'infnet', 'todo', 'publishing', 'plano', 'lgpd', 'profissional', 'período', 'maior',
            'microsoft', 'quanto', 'neste', 'podem', 'formação', 'professor', 'uso', 'modalidade', 'extensão',
            "possui", "sp", "curitiba", "pearson", "bookman", "apoio", "brasil", "br", "cruzeiro", "horária", "rj",
            "alegre", "paulo", "porto", "sagah", "pode", "sul", "df", "desde", "carga", "favip",
            "portaria", "colegiado", "login", "bvirtual", "ebscohost", "minhabiblioteca", "wyden", "unifavip",
            "etc", "dentro", "parágrafo", "conformr", "mediante", "reitoria", "isbn", "deve", "art", "secretaria",
            "uniabeu", "número", "conforme", "único", "uniasselvi", "tabela", "vida", "leonardo", "vinci",
            "ºn", "nº", "sob", "nesta", "t", "l", "sc", "http", "permite", "unicesumar", "studeo", "ce", "ba", "pa"
            "garantir", "santa", "brasileira", "maringá", "nacional", "index", "mg", "ma", "pr", "doi", "pe",
            "sério", "têm", "jan", "qualquer", "conclusão", "junto", "matrícula", "capítulo", "onde",
            "ch", "william", "out", "min", "n", "ha", "considerando", "unicarioca", "issn", "º", "unipar",
            "umuarama", "degead", "vivo", "deste", "onde", "desta", "jundiaí", "saraiva", "gen", "silva",
            "anhanguera", "ampli", "capaz", "nesse", "paraná", "faveni", "abeu",
            "cinco", "ch", "hr", "editora", "ppt", "outro", "pucpr", 'nota', 'maneira'
        ]
        edger = relevancy

        [self.good.remove(ng) for ng in skp if ng in self.good]
        good = list(ch.from_iterable([[a, b] for a, b, _ in self.show(edger)]))
        siz = {node: size for node, size in self.nodes(relevancy) if node not in skp and node in good}
        print("--------------------", len(siz), len(good), )
        _ = [wg.add_node(node, size=size) for node, size in siz.items()]
        _ = [wg.add_edge(a, b, color=colors[max(lm, w-cof)], weight=(log((min(top, w-cof)+0.01)*20).real or 1)/100000)
             for a, b, w in self.show(edger)]
        sizes = [int(log(siz[s]+0.0001 if s in siz else 5).real * size) for s, n in wg.nodes.items()]
        # t = list(set(wg.nodes.keys()).difference(set(siz.keys())))
        # [print(t[a:a + 10]) for a in range(0, len(t), 10)]
        # print("--------------------", len(siz))
        # t = list(set(siz.keys()))
        # [print(t[a:a + 10]) for a in range(0, len(t), 10)]

        color = [colors[a] for a, _ in enumerate(wg.nodes)]
        # color = [colors[wg.nodes[s]['size']] for s in wg.nodes]

        '''Node can be called by any python-hashable obj like string,number etc'''
        nx.draw(wg, with_labels=True, node_size=sizes, edge_color=col, node_color=color)
        # draws the networkx graph containing nodes which are declared till before
        plt.show()  # displays the networkx graph on matplotlib canvas


def test2(text=None):
    tx = Text(text).cleaner()
    sv = SurveyText(tx, text)
    sv.survey(20)
    sv.nodes(4)
    # [print(nd) for nd in sv.nodes(20)]
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # [print(nd) for nd in sv.show(40)]
    # sv.plot()
    print(len(Text.TEXT.original))
    # [print(t[a:a+10]) for a in range(0, len(t), 20)]
    t = sorted(sv.rebuff(20))
    print(len(t))
    [print(t[a:a+10]) for a in range(0, len(t), 20)]
    sv.paint(relevancy=8, cof=20)


def test(text=None):
    from pathlib import Path
    from main import tokenize_into_words as strip
    dados = Path(__file__).parent.parent / "data" / "inep.json"
    from tinydb import TinyDB, Query
    db = TinyDB(dados)
    query = Query()
    cs = ['1598939', '1549921', '1594810', '1625436', '1620561', '1667219', '1617841', '1537675',
          '1517110', '1620488', '1588016', '1666036', '1599632', '1615338', '1671887', '1618022',
          '153693', '1550008', '1617840', '1617717', '1565359', '1619434', '1667554']

    x = db.search(query.coid == cs[14])[0]  # 3 7 -8 9 -11 -14=30k 16 ++18 ++21=10k
    t = text or x["content"]
    print(f"course id: {x['coid']} course name: {x['course']} instituto: {x['ifes']}")
    t = strip(t)
    releva = 6 * max(1, len(t)//12000)
    print("releva = ", releva)
    main(t, releva)


def test_survey(text=None):
    from pathlib import Path
    dados = Path(__file__).parent.parent / "data" / "inep.json"
    from tinydb import TinyDB, Query
    db = TinyDB(dados)
    query = Query()
    x = db.search(query.coid == '1620488')
    y = db.all()
    oid = [cs["coid"] for cs in y]
    print(oid)
    t = text or x[0]["content"]
    # main(t)


def main(text=None, releva=2):
    tc = Counter(text)

    sv = SurveyText(tc, text, relevancy=releva)
    sv.survey()
    # [print(t[a:a+10]) for a in range(0, len(t), 20)]
    # t.sort()
    t = sorted(sv.rebuff(20))
    print("X->> texto original:", len(text), " XX----->  tokens revisados:", len(t))
    # [print(t[a:a+10]) for a in range(0, len(t), 20)]
    sv.paint(relevancy=releva, cof=50, top=15, size=240)
    return t


if __name__ == '__main__':
    test()
    # test_survey()
