# noinspection SpellCheckingInspection
""" Configuration for project Inep.

Changelog
---------
.. versionadded::    24.06
    |br| first version of main (21)
    |br| add bar and scatter plots (22)

.. versionadded::    24.07
    |br| using pdftotxt (16)
    |br| improve names (18)

|   **Open Source Notification:** This file is part of open source program **INEP**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from collections import Counter
import numpy as np
from pathlib import Path
from tinydb import TinyDB, Query  # , Query
from configuration import TAG, AREA

# noinspection SpellCheckingInspection
GLOVE = "/home/carlo/Documentos/inpe/cbow_s50.txt"


class SelfOrgMap:
    def __init__(self, ped=None):
        _ped = list(ped)
        tag_set = set([t for _, t, __ in _ped])
        ped_by_tag = [[(p, tg, n) for p, tg, n in _ped if tg == tis] for tis in tag_set]
        all_ped = [c for ct in ped_by_tag for c, *_ in ct if c]
        self.titles = titles = [t for ct in ped_by_tag for _, __, t in ct]
        # noinspection PyTypeChecker
        self.y = y = np.concatenate([[i] * len(p) for i, p in enumerate(ped_by_tag)])
        print(len(all_ped), tag_set, titles, y)
        # return

        def gimme_glove():
            with open(GLOVE, encoding='utf-8') as glove_raw:
                for line in glove_raw.readlines():
                    splitting = line.split(' ')
                    yield splitting[0], np.array(splitting[1:], dtype=float)

        self.all_ped = all_ped
        self.ped = self.tokenize()
        self.glove = {w: x for w, x in gimme_glove()}

        def poem_to_vec(tokens):
            words = [w for w in np.unique(tokens) if w in self.glove]
            return np.array([self.glove[w] for w in words])

        word_vector = [poem_to_vec(tokenized).mean(axis=0) for tokenized in self.ped]
        self.w = word_vector = np.array(word_vector)
        print(word_vector.shape, word_vector[0])

    def tokenize(self):
        from string import punctuation
        import stop_words
        stopwords = stop_words.get_stop_words('portuguese')
        xtr = ("nº cada si toda todas et al ii iii iv v vi vii viii ix xi xii  xiv xv xvi"
               " é a b c d e f g h i j x y z").split()
        stopwords.extend(xtr)

        def tokenize_poem(poem):
            poem = poem.lower().replace('\n', ' ')
            pontos = punctuation.replace("-", "") + '●'
            for sign in pontos:
                poem = poem.replace(sign, '')
            tokens = poem.split()
            tokens = [t for t in tokens if t not in stopwords and t != '']
            return tokens

        return [tokenize_poem(poem) for poem in self.all_ped]

    def som(self):
        from minisom import MiniSom
        import matplotlib.pyplot as plt
        # %matplotlib inline

        map_dim = 16
        word_vector = self.w

        # som = MiniSom(map_dim, map_dim, 50, sigma=1.0, random_seed=1)
        som = MiniSom(map_dim, map_dim, 50, sigma=0.5, random_seed=1)
        # som.random_weights_init(W)
        # som.train_batch(W, num_iteration=len(W) * 500, verbose=True)
        som.train_batch(word_vector, num_iteration=len(word_vector) * 15000, verbose=True)

        author_to_color = {0: 'chocolate',  # defesa
                           1: 'steelblue',  # segurança
                           2: 'dimgray',  # coisas
                           3: 'red',  # internet
                           4: 'green',  # informação
                           5: 'navy'}  # software
        color = [author_to_color[yy] for yy in self.y]

        from matplotlib.patches import Patch
        legend_elements = [Patch(facecolor=author_to_color[0], edgecolor='white', label='defesa cib'),
                           Patch(facecolor=author_to_color[1], edgecolor='white', label='segurança info'),
                           Patch(facecolor=author_to_color[2], edgecolor='white', label='int coisas'),
                           Patch(facecolor=author_to_color[3], edgecolor='white', label='sis internet'),
                           Patch(facecolor=author_to_color[4], edgecolor='white', label='sis informação'),
                           Patch(facecolor=author_to_color[5], edgecolor='white', label='eng software'), ]

        plt.figure(figsize=(20, 20))
        texts = []
        for i, (t, c, vec) in enumerate(zip(self.titles, color, word_vector)):
            winning_position = som.winner(vec)
            texts.append(plt.text(winning_position[0],
                                  winning_position[1] + np.random.rand() * .9,
                                  # t[:-5],
                                  t,
                                  color=c))

        plt.legend(handles=legend_elements, loc='lower right')
        plt.xticks(range(map_dim))
        plt.yticks(range(map_dim))
        plt.grid()
        plt.xlim([0, map_dim])
        plt.ylim([0, map_dim])
        plt.plot()
        plt.show()
        print("did")


class Doc:
    def __init__(self, data, name, content, dbase=None, ifes=None, coid=None, course=None,
                 instituto=None, nome=None, grau=None, tagger=None, tag_name=None,):
        self.ifes, self.coid, self.course = data or (ifes, coid, course)
        self.instituto, self. nome, self. grau = instituto,  nome,  grau
        self. tagger, self.tag_name = tagger,  tag_name
        self.tags, self.areas = {}, {}
        self.tag_count = 0
        self.name = name
        self.content = content
        print("DOC props", self.name, self.ifes, self.coid, self.course, (dbase is not None))
        self.from_file(data, content, name, dbase) if dbase is not None else dbase

    def from_file(self, data, doc, name, dbase):
        self.ifes, self.coid, self.course = data
        self.name = Path(name).name
        # self.content = [p.strings for p in doc]
        # self.content = " ".join("".join(p.strings) for p in doc)
        self.content = doc
        # dbase = TinyDB(Path(name).with_suffix('.json'))
        print("Doc", data, self.name, self.content[:50])
        dbase.insert(dict(ifes=self.ifes, coid=self.coid,
                          course=self.course, content=self.content))

    def count_areas(self):
        content = self.content.lower()
        self.areas = Counter({tag_name: sum(
            content.count(tag_value.lower()) for tag_value in tag_list)
                             for tag_name, tag_list in AREA.items()})
        print("self.areas", self.areas)
        return self

    def count_tags(self, normalize=True):
        content = self.content.lower()
        self.tags = Counter({tag_name: content.count(tag_value.lower())
                             for tag_name, tag_value in TAG})
        if not normalize:
            return self
        self.tag_count = all_tags = sum(self.tags.values()) or 1
        self.tags = Counter({tag_name: tag_value * 100 // all_tags
                             for tag_name, tag_value in self.tags.items()})
        print("self.tags", self.tags)
        return self

    def extract_egresso(self):
        egr = self.content.find("Perfil Profissional do Egresso")
        egr2 = self.content.find("perfil do egresso")
        egr_win = self.content[egr2: egr2 + 100] if egr2 else "None"
        print(f"egr: {egr, egr2}", self.name, egr_win, self.content[:100])


class Main:
    DIRNAME = Path("/home/carlo/Documentos/doc/academia/projetos/inep/projetos_pedagógicos/ppc_txt")

    def __init__(self, dbase=None):
        """ open files in projects"""
        self.base = dbase if dbase is not None else self.DIRNAME
        self.doc = []
        self.tag, self.areas = Counter(), Counter()
        self.from_file(dbase) if not dbase.all() else self.from_dbase(dbase)

    def _add_info_from(self, arc="../data/ines.csv"):
        from csv import reader
        from collections import namedtuple
        field_names = "ifes instituto coid nome grau tagger tag_name"
        fields = namedtuple("fields", field_names)
        query = Query()
        with open(arc, "r", encoding="utf-8") as filer:
            info = reader(filer)
            linfo = list(info)
            linfo = [fields(c, t, o, i, a, (ks := k.split(" - "))[0], ks[1])
                     for c, t, o, i, a, k, *_ in linfo]
            [print(li) for li in linfo]
            print(self.doc[0].coid, self.doc[0].course)
            ics = linfo[0].coid
            cs = self.base.search(query.coid == ics)
            print(cs[0]["ifes"], ics)
            dupper = [li._asdict() for li in linfo]
            print(dupper)
            [self.base.update(li._asdict(), query.coid == li.coid) for li in linfo]
            print(self.base.all()[0])

    def plot_bars(self):
        import matplotlib.pyplot as plt
        x_axis = [course.coid for course in self.doc]
        tags = self.tag.keys()
        delta = len(tags) // 2
        ydata = [(tag, [doc.tags[tag] for doc in self.doc]) for tag in tags]
        x_ticks = np.arange(len(x_axis))
        ax = plt.gca()
        [plt.bar(x_ticks + 0.1*(ort - delta), tg_dat, 0.1, label=lab)
         for ort, (lab, tg_dat) in enumerate(ydata)]
        ax.set_ylim([0, 90])
        plt.xticks(x_ticks, x_axis, rotation=45)
        plt.xlabel("Cursos")
        plt.ylabel("Count of references")
        plt.title("Number of References in each Course")
        plt.legend()
        plt.show()

    def scatter_plot(self):
        import matplotlib.pyplot as plt
        curso = [course.coid for course in self.doc]
        curso = range(len(curso))
        fig, ax = plt.subplots()
        tagger = ['0612R01', '0613E01']
        ydata, xdata = [[doc.tags[tag] for doc in self.doc] for tag in tagger]
        ia = [course.tags['0616I01']*10 for course in self.doc]
        ax.scatter(xdata, ydata, c=curso, s=ia, alpha=0.5)
        tagger = ['0612B01', '0612D01']
        ydata, xdata = [[doc.tags[tag] for doc in self.doc] for tag in tagger]
        ia = [course.tags['0615S02']*10 for course in self.doc]
        ax.scatter(xdata, ydata, c=curso, s=ia, alpha=0.5)
        ax.set_title('Volume and percent change')

        ax.grid(True)
        fig.tight_layout()
        plt.xlabel("Cursos")
        plt.ylabel("Count of references")
        plt.title("Number of References in each Course")
        plt.legend()
        plt.show()

    def trim_class(self, hold):
        [self.tag.update(doc.tags) for doc in self.doc]
        [self.areas.update(doc.tags) for doc in self.doc]
        self.tag = {tag: count for tag, count in self.tag.items() if count > hold}

    def from_dbase(self, dbase):
        self.doc = [Doc(None, None, **base_data) for base_data in dbase.all()]

    def tag_base(self):
        [doc.count_tags().count_areas() for doc in self.doc]
        return self

    def from_file(self, dbase):
        dirname = Main.DIRNAME
        if dirname.is_dir():
            dirname = dirname.resolve()
            print(dirname)
        files = dirname.glob("*.txt")
        f_list = list(files)
        [self.extract_course(doc) for doc in f_list
         if doc.name.startswith("COD") and "PPC" in doc.name]

        [Doc(self.extract_course(doc), *self.extract_section(doc), dbase=dbase)
         for doc in f_list if doc.name.startswith("COD") and "PPC" in doc.name]

    @staticmethod
    def extract_course(file_name):
        fd = file_name.name
        fd = fd.split(".")[0]
        fd = fd.split("_")
        fd = fd[2], fd[-1], "_".join(fd[4:-1])
        return fd

    @staticmethod
    def extract_section(file_name):
        with open(file_name, 'r', encoding='utf-8') as fd:
            doc = fd.read()
        return file_name, doc


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


def tokenize_all_files_in_dir():

    dirname = Main.DIRNAME
    if dirname.is_dir():
        dirname = dirname.resolve()
        print(dirname)
    files = list(dirname.glob("*.pdf"))
    file_names = [doc for doc in files if doc.name.startswith("COD")]
    print(file_names[0])
    file_name = file_names[0]
    file_text = str(file_name).replace(".pdf", ".txt").replace(
        "PPCs cursos area 06", "ppc_txt")

    with open(file_text, 'r', encoding='utf-8') as fd:
        t = fd.read()
        print(t)
        t = tokenize_into_words(t)
        st = 15
        [print(t[a:a + st]) for a in range(0, len(t), st)]
    return


def convert_pdf_to_txt_in_dir():
    def args(file_name):
        file_text = str(file_name).replace(".pdf", ".txt").replace(
            "PPCs cursos area 06", "ppc_txt")
        return "pdftotext", file_name, file_text

    import subprocess
    dirname = Main.DIRNAME
    files = list(dirname.glob("*.pdf"))
    [subprocess.call(args(doc)) for doc in files if doc.name.startswith("COD") and "PPC" in doc.name]
    # print(file_text)
    # subprocess.call(["pdftotext", file_name, file_text])
    # subprocess.call(f"pdftotext {file_name} {file_text}", shell=True)


def test2():
    dados = Path(__file__).parent.parent / "data" / "inep.json"
    db = TinyDB(dados)
    # print(dados, len(db.all()), db)
    main_instance = Main(db)
    # [print(d.name) for d in main_instance.doc]
    t = main_instance.doc[11].content
    t = tokenize_into_words(t)
    st = 15
    [print(t[a:a + st]) for a in range(0, len(t), st)]


def main():
    dados = Path(__file__).parent.parent / "data" / "inep.json"
    db = TinyDB(dados)
    # print(dados, len(db.all()), db)
    main_instance = Main(db).tag_base()
    # tags = Counter()
    # [tags.update(doc.tags) for doc in main_instance.doc]
    main_instance.trim_class(30)
    # print(main_instance.tag)
    # som = SelfOrgMap([(cd.content, cd.tag_name, cd.nome) for cd in main_instance.doc if cd.tag_name])
    # som.som()
    # main_instance.add_info()
    # main_instance.add()
    # main_instance.plot_bars()
    # main_instance.scatter_plot()
    # [print(doc.coid, doc.course, len(doc.content), doc.tag_count) for doc in main_instance.doc]
    # doc16 = list(doc for doc in main_instance.doc if str(doc.coid) == "1620488")[0]
    # doc16.content = doc16.content.replace("■", " ").replace("○", " ")
    # print(doc16.content)
    # Fruit = Query()
    # db.search(Fruit.coid == '1620488')
    # db.update(dict(content=doc16.content), Fruit.coid == '1620488')


if __name__ == '__main__':
    test2()
    # test4()
    # main()
