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
# import pdfreader
from pdfreader import SimplePDFViewer
from pathlib import Path
from tinydb import TinyDB  # , Query


class Doc:
    def __init__(self, data, name, content, dbase=None, ifes=None, coid=None, course=None):
        self.ifes, self.coid, self.course = data or (ifes, coid, course)
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

    def extract_egresso(self):
        egr = self.content.find("Perfil Profissional do Egresso")
        egr2 = self.content.find("perfil do egresso")
        pegr = self.content[egr2: egr2 + 100] if egr2 else "None"
        print(f"egr: {egr, egr2}", self.name, pegr, self.content[:100])


class Main:
    DIRNAME = Path("/home/carlo/Documentos/doc/academia/projetos/inep/projetos_pedagógicos/PPCs cursos area 06")

    def __init__(self, dbase=None):
        """ open files in projects"""
        self.from_file(dbase) if not dbase.all() else self.from_dbase(dbase)

    @staticmethod
    def from_dbase(dbase):
        [Doc(None, None, **base_data) for base_data in dbase.all()]

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
    Main(db)
