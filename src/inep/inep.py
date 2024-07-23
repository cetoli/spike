""" Client generator for project Inep.

Changelog
---------
.. versionadded::    24.07
    |br| Initial screen (22)

|   **Open Source Notification:** This file is part of open source program **INEP**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from csv import DictReader
from pathlib import Path


class InepClient:
    def __init__(self, br):
        self.br = br
        self.doc = br.document["pydiv"]
        self.doc.html = ""
        self.cine = "../data/Logo_CINE_BRASIL_Horizontal.jpg"
        self.navbar()

    def navbar(self):
        html = self.br.html
        nav, div, a, span, img = html.NAV, html.DIV, html.A, html.SPAN, html.IMG
        ig = a(img(src="../data/inep-logo-1-1024x504.png", alt="INEP", width="30", height="28"), Class="navbar-item", href="/")
        ns = div(a("INEP", Class="navbar-item", href="/"), Class="navbar-start")
        mn = div(div([
            a("Ajuda", Class="navbar-item", href="/"),
            a("Sobre", Class="navbar-item", href="/")
            ], Id="right_menu", Class="navbar-end"), Class="navbar-menu")
        bg = span([span(), span(), span(),], Class="navbar-burger", data_target="navbar-menu")
        navbar = nav([div([ig, ns, bg], Class="navbar-brand"), mn], Class="navbar is-transparent")
        _ = self.doc <= navbar

    def header(self):
        html = self.br.html
        nav, div, a, span, img = html.NAV, html.DIV, html.A, html.SPAN, html.IMG
        hhs = div([
            html.H1("INEP", Class="title is-1 is-spaced"),
            html.H4("Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira", Class="subtitle is-4")
            ], Class="has-text-centered")
        ho = div(div(div(div(hhs, Class="has-text-centered"), Class="container"), Class="hero-body"), Class="hero")
        head = div(ho, Class="main-header")
        _ = self.doc <= head

    def content(self):
        html = self.br.html
        figure, div, a, span, img = html.FIGURE, html.DIV, html.A, html.SPAN, html.IMG
        cb = div(div([
            div(html.H4("Classificação Internacional de Cursos de Graduação"), Class="card-content-header"),
            div(figure(
                a(img(src=self.cine, width="400px"), Id="cine_brasil"), Class="image is-4by3"
            ), Class="card-image").bind("click", lambda event: Ies(self.br).table()),

            "Classificação Internacional Normalizada da Educação Adaptada para"
            " Cursos de Graduação e Sequenciais de Formação Específica do Brasil"
            ], Class="card"), Class="column is-4")

        content = div(div(cb, Class="columns is-multiline is-centered has-text-centered"), Class="container")
        _ = self.doc <= content


class Ies(InepClient):
    # def __init__(self, br):
    # 1775,"Centro Universitário Favip Wyden",1594810,"Devops","Tecnológico","0615S02 - Sistemas de informação"
    def table(self, cf="ines.csv"):
        # dados = Path(__file__).parent.parent / "data" / cf
        head = "ifs, nome da ifs,Curso,Tipo,Nível,Rótulo".split(",")
        dados = f"../data/{cf}"
        with open(dados, 'r', newline='') as csvfile:
            dw = DictReader(csvfile, head, delimiter=',', quotechar='"')
            csv = [d for d in dw]
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXX -> ", csv)
        html = self.br.html
        table, thead, tr, th, td, tbody = html.TABLE, html.THEAD, html.TR, html.TH, html.TD, html.BODY
        trs = [tr([td(value[:50]) for value in row.values()]) for row in csv]
        # trs = [tr([td(d[:20]) for d in (list(row.values()))]) for row in csv]
        headers = [th(h) for h in head]
        content = table([thead(tr(headers)), tbody(trs)], Class="table")
        _ = self.doc <= content


def main(br):
    for i in range(20000):
        _ = i ** 2
    ic = InepClient(br)
    ic.header()
    ic.content()
