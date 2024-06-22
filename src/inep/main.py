""" Configuration for project Inep.

Changelog
---------
.. versionadded::    24.06
    |br| first version of config (21)

|   **Open Source Notification:** This file is part of open source program **INEP**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from collections import Counter

# import pdfreader
from pdfreader import SimplePDFViewer
from pathlib import Path
from tinydb import TinyDB  # , Query

TAG = (
    ("0612B01", "Banco de dados"),
    ("0612D01", "Defesa cibernética"),
    ("0612D01", "Cibersegurança"),
    ("0612G01", "Gestão da tecnologia da informação"),
    ("0612G01", "Gestão de ti"),
    ("0612R01", "Redes de computadores"),
    ("0613E01", "Engenharia de software"),
    ("0613J01", "Jogos digitais"),
    ("0614C01", "Ciência da computação"),
    ("0614I01", "Inteligência artificial"),
    ("0615S01", "Segurança da informação"),
    ("0615S02", "Sistemas de informação"),
    ("0615S03", "Sistemas para internet"),
    ("0616E01", "Engenharia de computação"),
    ("0616E01", "Engenharia da computação"),
    ("0616I01", "Internet das coisas"),
    ("0616S01", "Sistemas embarcados"),
    ("0617A01", "Agrocomputação"),
    ("0617C01", "Ciência de dados"),
    ("0617C02", "Computação e Tecnologias da Informação e Comunicação (TIC) em biociências e saúde"),
    ("0617C02", "biociências e saúde"),
    ("0617C03", "Criação digital"),
    ("0688P01", "Programas interdisciplinares abrangendo computação e Tecnologias da Informação e Comunicação (TIC)"),
    ("0699P01",
     "Programas abrangendo Computação e Tecnologias da Informação e Comunicação (TIC) em processo de definição da classificação"),
)
AREA = dict(
    A611=[
        "Uso da internet",
        "Uso de software para cálculo em planilhas",
        "Uso de software para editoração eletrônica",
        "Uso de software para processamento de dados",
        "Uso de software para processamento de texto",
        "Uso do computador",
        # "internet",
        "software para cálculo em planilhas",
        "software para editoração eletrônica",
        "software para processamento de dados",
        "software para processamento de texto",
        "cálculo em planilhas",
        "editoração eletrônica",
        "processamento de dados",
        "processamento de texto",
        # "computador"
    ],
    A0612=[
        "Administração de banco de dados",
        "Administração de rede",
        "Administração de tecnologia da informação",
        "Administração e gestão de computadores",
        "Aplicações de mídia de computador",
        "Design de web",
        "Manutenção de redes informáticas",
        "Instalação de redes informáticas",
        "Instalação e manutenção de redes informáticas",
        "Projeto de rede",
        "Segurança da tecnologia da informação",
        "Segurança da informação",
    ],
    A0613=[
        "Análise de sistemas de computador"
        "Ciência da computação",
        "Desenvolvimento de linguagens de programação",
        "Desenvolvimento de software",
        "Design de sistemas informáticos",
        # "Informática",
        "Programação de computadores",
        "Programação de software",
        # "Sistemas operacionais",
    ]
)


class Doc:
    def __init__(self, data, name, content, dbase=None, ifes=None, coid=None, course=None):
        self.ifes, self.coid, self.course = data or (ifes, coid, course)
        self.tags, self.areas = {}, {}
        self.name = name
        self.content = content
        print("DOC props", self.name, self.ifes, self.coid, self.course, (dbase is not None))
        self.from_file(data, content, name, dbase) if dbase is not None else dbase

    def from_file(self, data, doc, name, dbase):
        self.ifes, self.coid, self.course = data
        self.name = Path(name).name
        # self.content = [p.strings for p in doc]
        self.content = "".join("".join(p.strings) for p in doc)
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

    def count_tags(self):
        content = self.content.lower()
        self.tags = Counter({tag_name: content.count(tag_value.lower())
                             for tag_name, tag_value in TAG})
        print("self.tags", self.tags)
        return self

    def extract_egresso(self):
        egr = self.content.find("Perfil Profissional do Egresso")
        egr2 = self.content.find("perfil do egresso")
        pegr = self.content[egr2: egr2 + 100] if egr2 else "None"
        print(f"egr: {egr, egr2}", self.name, pegr, self.content[:100])


class Main:
    DIRNAME = Path("/home/carlo/Documentos/doc/academia/projetos/inep/projetos_pedagógicos/PPCs cursos area 06")

    def __init__(self, dbase=None):
        """ open files in projects"""
        self.doc = []
        self.tag, self.areas = Counter(), Counter()
        self.from_file(dbase) if not dbase.all() else self.from_dbase(dbase)

    def plot_bars(self, hold):
        import numpy as np
        import matplotlib.pyplot as plt
        X = [course.coid for course in self.doc]
        tags = self.tag.keys()
        delta = len(tags) //2
        ydata = [(tag, [doc.tags[tag] for doc in self.doc]) for tag in tags]
        X_axis = np.arange(len(X))
        ax = plt.gca()
        [plt.bar(X_axis+ 0.1*(ort - delta), tg_dat, 0.1, label=lab)
         for ort, (lab, tg_dat) in enumerate(ydata)]
        ax.set_ylim([0, 50])
        plt.xticks(X_axis, X, rotation=45)
        plt.xlabel("Cursos")
        plt.ylabel("Count of references")
        plt.title("Number of References in each Course")
        plt.legend()
        plt.show()

    def scatter_plot(self, hold):
        import matplotlib.pyplot as plt
        tags = self.tag.keys()
        delta = len(tags) //2
        curso = [course.coid for course in self.doc]
        curso = range(len(curso))
        fig, ax = plt.subplots()
        # tagger = ['0612B01', '0612D01']
        tagger = ['0612R01', '0613E01']
        ydata, xdata = [[doc.tags[tag] for doc in self.doc] for tag in tagger]
        ia = [course.tags['0616I01']*10 for course in self.doc]
        ax.scatter(xdata, ydata, c=curso, s=ia, alpha=0.5)
        tagger = ['0612B01', '0612D01']
        ydata, xdata = [[doc.tags[tag] for doc in self.doc] for tag in tagger]
        ia = [course.tags['0615S02']*10 for course in self.doc]
        ax.scatter(xdata, ydata, c=curso, s=ia, alpha=0.5)

        # ax.set_xlabel(r'$\Delta_i$', fontsize=15)
        # ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
        ax.set_title('Volume and percent change')

        ax.grid(True)
        fig.tight_layout()
        # plt.xticks(X_axis, X, rotation=45)
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
        files = dirname.glob("*.pdf")
        f_list = list(files)
        ifes = [self.extract_course(doc) for doc in f_list if doc.name.startswith("COD")]

        docs = [Doc(self.extract_course(doc), *self.extract_section(doc), dbase=dbase)
                for doc in f_list if doc.name.startswith("COD")]

    @staticmethod
    def extract_course(file_name):
        fd = file_name.name
        fd = fd.split(".")[0]
        fd = fd.split("_")
        fd = fd[2], fd[-1], "_".join(fd[4:-1])
        return fd

    @staticmethod
    def extract_section(file_name):
        fd = open(file_name, "rb")

        doc = SimplePDFViewer(fd)
        return file_name, doc


if __name__ == '__main__':
    dados = Path(__file__).parent.parent / "data" / "inep.json"
    db = TinyDB(dados)
    print(dados, len(db.all()), db)
    main = Main(db).tag_base()
    # tags = Counter()
    # [tags.update(doc.tags) for doc in main.doc]
    main.trim_class(30)
    print(main.tag)
    # main.plot_bars(30)
    main.scatter_plot(30)
