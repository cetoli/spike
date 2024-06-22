""" Configuration for project Inep.

Changelog
---------
.. versionadded::    24.06
    |br| first version of config (22)

|   **Open Source Notification:** This file is part of open source program **INEP**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""

TAG = (
    ("0612B01", "Banco de dados"),
    ("0612D01", "Defesa cibernética"),
    ("0612D01", "Cibersegurança"),
    ("0612D01", "Segurança cibernética"),
    ("0612D01", "segurança de software"),
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
     "Programas abrangendo Computação e Tecnologias da Informação"
     " e Comunicação (TIC) em processo de definição da classificação"),
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

CURSO = [
    ("TECNOLOGIA EM AGROCOMPUTAÇÃO",
     """Projeta soluções computacionais para problemas identificados no contexto
     das ciências agrárias. Aplica e relaciona conceitos de engenharia de software,
     automação e ciências agrárias. Especifica requisitos mínimos de hardware e
     software para sistemas de agrocomputação. Desenvolve sistemas informatizados
     para a agricultura de precisão. Gerencia o processo de desenvolvimento de
     sistemas na área de agrocomputação. Aplica padrões nacionais e internacionais
     da indústria e do mercado nos sistemas de agrocomputação. Realiza estudos
     de viabilidade técnica e econômica na área. Avalia o impacto socioambiental
     de soluções computacionais no ambiente agrário. Aplica agrocomputação para
     a utilização racional de recursos naturais. Gerencia equipes técnicas na área.
     Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em sua área de
     formação.
     """),
    ("TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS",
     """Analisa, projeta, desenvolve, testa, implanta e mantém sistemas computacionais
     de informação. Avalia, seleciona, especifica e utiliza metodologias, tecnologias
     e ferramentas da Engenharia de Software, linguagens de programação e bancos
     de dados. Coordena equipes de produção de softwares. Vistoria, realiza perícia,
     avalia, emite laudo e parecer técnico em sua área de formação.
     """),
    ("TECNOLOGIA EM BANCO DE DADOS",
     """
     Projeta, modela, implementa, documenta, testa e gerencia bancos de dados
     centralizados ou distribuídos. Avalia e seleciona sistemas de gerenciamento
     de banco de dados. Avalia desempenho do banco de dados e propõe medidas
     para a melhoria do acesso. Elabora o planejamento da segurança e integridade.
     Desenvolve métodos para uso dos dados no apoio à tomada de decisões
     gerenciais. Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em
     sua área de formação.
     """),
    ("TECNOLOGIA EM DEFESA CIBERNÉTICA",
     """
     Analisa a operacionalidade das redes, os sistemas de conexão, e avalia as
     ameaças de invasão. Planeja, especifica e desenvolve sistemas de proteção de
     redes e de equipamentos de tecnologia da informação. Investiga e monitora
     ataques. Estabelece procedimentos contra invasão de redes e guerra eletrônica.
     Coordena equipes de trabalho. Vistoria, realiza perícia, avalia, lauda e emite
     parecer técnico em sua área de formação.
     """),
    ("TECNOLOGIA EM GESTÃO DA TECNOLOGIA DA INFORMAÇÃO",
     """
     Especifica e gerencia os recursos de hardware, software e pessoal de Tecnologia
     da Informação em articulação com os objetivos e o planejamento estratégico das
     organizações. Implementa e gerencia os sistemas informatizados nas empresas.
     Projeta soluções de TI para o processo de gerenciamento das empresas. Analisa
     e gerencia contratos de serviços de tecnologia. Avalia e emite parecer técnico
     em sua área de formação.
     """),
    ("TECNOLOGIA EM GESTÃO DE TELECOMUNICAÇÕES",
     """
     Especifica, planeja, gerencia e supervisiona serviços de telecomunicações.
     Coordena atividades relacionadas à comunicação móvel, comunicação de dados,
     gerência de redes e serviços, e infraestrutura. Avalia e propõe alternativas e
     melhorias englobando a área de negócios da empresa de telecomunicações.
     Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em sua área de
     formação.
     """),
    ("TECNOLOGIA EM JOGOS DIGITAIS",
     """
     Cria, projeta, implementa, testa, implanta e mantém jogos digitais de gêneros
     diversos em plataformas computacionais. Gerencia projetos de jogos digitais com
     equipes multidisciplinares. Avalia, seleciona e utiliza metodologias, tecnologias
     e ferramentas para o desenvolvimento de jogos digitais. Elabora e desenvolve
     roteiros, cenários, personagens e mecânicas para jogos digitais adequados
     às plataformas selecionadas. Avalia e emite parecer técnico em sua área de
     formação.
     """),
    ("TECNOLOGIA EM REDES DE COMPUTADORES",
     """
     Projeta, implanta, gerencia e integra redes de computadores. Identifica
     necessidades, dimensiona, elabora especificações e avalia soluções para
     segurança de redes de computadores. Desenvolve e documenta projetos em
     redes de pequeno, médio e grande portes. Avalia o desempenho da rede e
     propõe medidas para melhoria da qualidade de serviço. Vistoria, realiza perícia,
     avalia, emite laudo e parecer técnico em sua área de formação.
     """),
    ("TECNOLOGIA EM REDES DE TELECOMUNICAÇÕES",
     """
     Especifica, elabora, planeja, desenvolve, implanta, integra, certifica, mantém e
     gerencia projetos lógicos e físicos de redes de telecomunicações analógicas e
     digitais, locais e de longa distância. Analisa e propõe alternativas de integração
     e convergência de diferentes tipos de serviços. Avalia e propõe alternativas para
     o desempenho e a compatibilidade das redes de telecomunicações. Vistoria,
     realiza perícia, avalia, emite laudo e parecer técnico em sua área de formação.
     """),
    ("TECNOLOGIA EM SEGURANÇA DA INFORMAÇÃO",
     """Analisa, projeta, desenvolve, gerencia, testa, implanta, integra, propõe e avalia
     soluções para a garantia da confidencialidade, integridade e disponibilidade dos
     recursos de Tecnologia da Informação. Gerencia, aplica, administra e configura
     ambientes corporativos com requisitos de segurança. Realiza análises de riscos,
     gerencia sistemas de informações. Projeta e gerencia redes de computadores
     seguras. Realiza auditorias. Planeja contingências e recuperação das informações
     em caso de sinistros. Vistoria, realiza perícia, avalia, emite laudo e parecer
     técnico em sua área de formação.
     """),
    ("TECNOLOGIA EM SISTEMAS DE TELECOMUNICAÇÕES",
     """Especifica, projeta, planeja, desenvolve, implanta, integra, certifica, mantém e
     gerencia sistemas de telecomunicações incluindo a infraestrutura de informática
     e redes de telecomunicações. Analisa e propõe alternativas de integração,
     convergência, compatibilidade e eficiência da infraestrutura de sistemas de
     telecomunicações, considerando as redes e os equipamentos de informática
     envolvidos. Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em
     sua área de formação.
     """),
    ("TECNOLOGIA EM SISTEMAS EMBARCADOS",
     """Especifica e desenvolve software para microcontroladores, microprocessadores
     e dispositivos de lógica reconfigurável. Projeta hardware para sistemas
     embarcados. Aplica técnicas de engenharia de software, de projeto de circuitos
     eletroeletrônicos e de design de produto no desenvolvimento de sistemas
     embarcados. Testa e avalia o desempenho de sistemas embarcados. Especifica
     requisitos mínimos de hardware e software para sistemas embarcados. Utiliza
     adequadamente ferramentas, equipamentos, dispositivos e ambientes de
     programação, no projeto de sistemas embarcados. Participa de equipes de
     projeto e gerencia equipes técnicas na área de desenvolvimento de sistemas
     embarcados. Realiza estudos de viabilidade técnica e econômica na área. Vistoria,
     realiza perícia, avalia, emite laudo e parecer técnico em sua área de formação.
     """),
    ("TECNOLOGIA EM SISTEMAS PARA INTERNET",
     """Projeta, desenvolve, testa, implanta, mantém, avalia e analisa páginas para
     sites de Internet e intranets, sistemas de comércio eletrônico e aplicativos
     para plataformas móveis para a Internet. Avalia, especifica, seleciona e utiliza
     metodologias e ferramentas adequadas para o desenvolvimento das aplicações.
     Elabora e estabelece diretrizes para a criação de interfaces adequadas à aplicação
     de acordo com características, necessidades e público-alvo. Vistoria, realiza
     perícia, avalia, emite laudo e parecer técnico em sua área de formação.
     """),
    ("TECNOLOGIA EM TELEMÁTICA",
     """Especifica, projeta, planeja, desenvolve, implanta, integra e gerencia serviços
     informáticos por meio de redes de telecomunicações, estruturas físicas e lógicas
     de redes de telecomunicação e dados, redes de monitoramento e controle.
     Desenvolve protocolos e aplicações para comunicação de dados que associem
     meios de informática. Vistoria, realiza perícia, avalia, emite laudo e parecer
     técnico em sua área de formação.
     """)
]
SUPER = dict(
    a0617A01='TECNOLOGIA EM AGROCOMPUTAÇÃO',
    a0615S02='TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS',
    a0612B01='TECNOLOGIA EM BANCO DE DADOS',
    a0612D01='TECNOLOGIA EM DEFESA CIBERNÉTICA',
    a0612G01='TECNOLOGIA EM GESTÃO DA TECNOLOGIA DA INFORMAÇÃO',
    a0699P01='TECNOLOGIA EM GESTÃO DE TELECOMUNICAÇÕES',
    a0613J01='TECNOLOGIA EM JOGOS DIGITAIS',
    a0612R01='TECNOLOGIA EM REDES DE COMPUTADORES',
    a0616I01='TECNOLOGIA EM REDES DE TELECOMUNICAÇÕES',
    a0615S01='TECNOLOGIA EM SEGURANÇA DA INFORMAÇÃO',
    a0688P01='TECNOLOGIA EM SISTEMAS DE TELECOMUNICAÇÕES',
    a0616S01='TECNOLOGIA EM SISTEMAS EMBARCADOS',
    a0615S03='TECNOLOGIA EM SISTEMAS PARA INTERNET',
    a0616E01='TECNOLOGIA EM TELEMÁTICA',
)

TXT = """51CURSO SUPERIOR DE TECNOLOGIA EM AGROCOMPUTAÇÃO
2400 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusãoProjeta soluções computacionais para problemas identificados no contexto
das ciências agrárias. Aplica e relaciona conceitos de engenharia de software,
automação e ciências agrárias. Especifica requisitos mínimos de hardware e
software para sistemas de agrocomputação. Desenvolve sistemas informatizados
para a agricultura de precisão. Gerencia o processo de desenvolvimento de
sistemas na área de agrocomputação. Aplica padrões nacionais e internacionais
da indústria e do mercado nos sistemas de agrocomputação. Realiza estudos
de viabilidade técnica e econômica na área. Avalia o impacto socioambiental
de soluções computacionais no ambiente agrário. Aplica agrocomputação para
a utilização racional de recursos naturais. Gerencia equipes técnicas na área.
Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em sua área de
formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado. Laboratório de hardware.
Laboratório de computação embarcada e inteligência artificial.
Laboratório de geoprocessamento. Laboratório de processamento digital de
imagens e vídeo. Laboratório de agroautomação. Laboratório de agricultura
de precisão.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de irrigação de precisão.
Laboratório de sensores.
Campo de atuaçãoEmpresas de planejamento, desenvolvimento de projetos, assessoramento
técnico e consultoria.
Empresas de tecnologia.
Empresas e organizações do setor agrícola.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas2124-05 - Analista de desenvolvimento de sistemas.
2124-05 - Tecnólogo em análise de desenvolvimento de sistema.
Possibilidades de prosseguimento
de estudos na Pós-GraduaçãoPós-graduação na área de Ciência da Computação, entre outras.
51CURSO SUPERIOR DE TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusãoAnalisa, projeta, desenvolve, testa, implanta e mantém sistemas computacionais
de informação. Avalia, seleciona, especifica e utiliza metodologias, tecnologias
e ferramentas da Engenharia de Software, linguagens de programação e bancos
de dados. Coordena equipes de produção de softwares. Vistoria, realiza perícia,
avalia, emite laudo e parecer técnico em sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de redes de computadores.
Campo de atuaçãoEmpresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Empresas de tecnologia.
Empresas em geral (indústria, comércio e serviços).
Organizações não-governamentais.
Órgãos públicos.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas2124-05 -Tecnólogo em análise e desenvolvimento de sistemas.
2124-05 -Tecnólogo em processamento de dados.
Possibilidades de prosseguimento
de estudos na Pós-GraduaçãoPós-graduação na área de Ciência da Computação, entre outras.
52CURSO SUPERIOR DE TECNOLOGIA EM BANCO DE DADOS
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusão
Projeta, modela, implementa, documenta, testa e gerencia bancos de dados
centralizados ou distribuídos. Avalia e seleciona sistemas de gerenciamento
de banco de dados. Avalia desempenho do banco de dados e propõe medidas
para a melhoria do acesso. Elabora o planejamento da segurança e integridade.
Desenvolve métodos para uso dos dados no apoio à tomada de decisões
gerenciais. Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em
sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Campo de atuaçãoEmpresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Empresas de tecnologia.
Empresas em geral (indústria, comércio e serviços).
Organizações não-governamentais.
Órgãos públicos.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas
Possibilidades de prosseguimento
de estudos na Pós-Graduação
2123-05 - Tecnólogo em banco de dados.
2123-05 - Administrador de banco de dados.
Pós-graduação na área de Ciência da Computação, entre outras.
53CURSO SUPERIOR DE TECNOLOGIA EM DEFESA CIBERNÉTICA
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusão
Analisa a operacionalidade das redes, os sistemas de conexão, e avalia as
ameaças de invasão. Planeja, especifica e desenvolve sistemas de proteção de
redes e de equipamentos de tecnologia da informação. Investiga e monitora
ataques. Estabelece procedimentos contra invasão de redes e guerra eletrônica.
Coordena equipes de trabalho. Vistoria, realiza perícia, avalia, lauda e emite
parecer técnico em sua área de formação.
Infraestrutura mínima requerida
Campo de atuação
Biblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de redes de computadores.
Laboratório de tecnologia da informação e comunicações.
Empresas de tecnologia e segurança da informação.
Forças Armadas.
Órgãos públicos.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas2123-20 - Analista em segurança da informação.
2123-20 - Tecnólogo em segurança da informação.
2124-10 - Analista de redes e de comunicação de dados.
Possibilidades de prosseguimento
de estudos na Pós-GraduaçãoPós-graduação na área de Ciência da Computação.
Pós-graduação na área de Ciências Militares, entre outras.
54CURSO SUPERIOR DE TECNOLOGIA EM GESTÃO DA TECNOLOGIA DA INFORMAÇÃO
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusão
Especifica e gerencia os recursos de hardware, software e pessoal de Tecnologia
da Informação em articulação com os objetivos e o planejamento estratégico das
organizações. Implementa e gerencia os sistemas informatizados nas empresas.
Projeta soluções de TI para o processo de gerenciamento das empresas. Analisa
e gerencia contratos de serviços de tecnologia. Avalia e emite parecer técnico
em sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Campo de atuaçãoEmpresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Empresas de tecnologia.
Empresas em geral (indústria, comércio e serviços).
Órgãos públicos.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas1425-35 - Tecnólogo em gestão da tecnologia da informação.
1425-35 - Tecnólogo em gestão de sistema de informação.
Possibilidades de prosseguimento
de estudos na Pós-GraduaçãoPós-graduação na área de Ciência da Computação, entre outras.
55CURSO SUPERIOR DE TECNOLOGIA EM GESTÃO DE TELECOMUNICAÇÕES
2400 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusão
Especifica, planeja, gerencia e supervisiona serviços de telecomunicações.
Coordena atividades relacionadas à comunicação móvel, comunicação de dados,
gerência de redes e serviços, e infraestrutura. Avalia e propõe alternativas e
melhorias englobando a área de negócios da empresa de telecomunicações.
Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em sua área de
formação.
Infraestrutura mínima requerida
Campo de atuação
Biblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de redes de computadores.
Laboratório de telecomunicações.
Companhias operadoras de telefonia fixa e móvel e comunicação de dados.
Data centers.
Empresas de comercialização de componentes de telecomunicações.
Empresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Indústria de acessórios e componentes de telecomunicações.
Operadoras de TV aberta e por assinatura.
Provedores de serviço e acesso à internet.
Repetidoras de rádio e televisão.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas2143-70 - Especialista em telecomunicações (tecnólogo).
2143-70 - Tecnólogo em telecomunicações.
Possibilidades de prosseguimento
de estudos na Pós-GraduaçãoPós-graduação na área de Administração.
Pós-graduação na área de Engenharia Elétrica, entre outras.
56CURSO SUPERIOR DE TECNOLOGIA EM JOGOS DIGITAIS
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusão
Cria, projeta, implementa, testa, implanta e mantém jogos digitais de gêneros
diversos em plataformas computacionais. Gerencia projetos de jogos digitais com
equipes multidisciplinares. Avalia, seleciona e utiliza metodologias, tecnologias
e ferramentas para o desenvolvimento de jogos digitais. Elabora e desenvolve
roteiros, cenários, personagens e mecânicas para jogos digitais adequados
às plataformas selecionadas. Avalia e emite parecer técnico em sua área de
formação.
Infraestrutura mínima requerida
Campo de atuação
Ocupações CBO associadas
Possibilidades de prosseguimento
de estudos na Pós-Graduação
Biblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Acervo de jogos digitais.
Agências de publicidade.
Empresas de desenvolvimento de jogos digitais.
Instituições educacionais.
Produtoras de websites.
Veículos de comunicação em geral.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
2621-35 - Tecnólogo em produção audiovisual.
Pós-graduação na área de Ciência da Computação, entre outras.
57CURSO SUPERIOR DE TECNOLOGIA EM REDES DE COMPUTADORES
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusão
Projeta, implanta, gerencia e integra redes de computadores. Identifica
necessidades, dimensiona, elabora especificações e avalia soluções para
segurança de redes de computadores. Desenvolve e documenta projetos em
redes de pequeno, médio e grande portes. Avalia o desempenho da rede e
propõe medidas para melhoria da qualidade de serviço. Vistoria, realiza perícia,
avalia, emite laudo e parecer técnico em sua área de formação.
Infraestrutura mínima requerida
Campo de atuação
Ocupações CBO associadas
Possibilidades de prosseguimento
de estudos na Pós-Graduação
Biblioteca incluindo acervo específico e atualizado. Laboratório de hardware.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de redes de computadores.
Empresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Empresas de tecnologia.
Empresas em geral (indústria, comércio e serviços).
Organizações não-governamentais.
Órgãos públicos.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
2123-10 - Tecnólogo em redes de computadores.
2123-10 - Administrador de redes.
Pós-graduação na área de Ciência da Computação.
Pós-graduação na área de Engenharia Elétrica, entre outras.
58CURSO SUPERIOR DE TECNOLOGIA EM REDES DE TELECOMUNICAÇÕES
2400 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusão
Especifica, elabora, planeja, desenvolve, implanta, integra, certifica, mantém e
gerencia projetos lógicos e físicos de redes de telecomunicações analógicas e
digitais, locais e de longa distância. Analisa e propõe alternativas de integração
e convergência de diferentes tipos de serviços. Avalia e propõe alternativas para
o desempenho e a compatibilidade das redes de telecomunicações. Vistoria,
realiza perícia, avalia, emite laudo e parecer técnico em sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de redes de computadores.
Laboratório de telecomunicações.
Laboratório de telefonia.
Campo de atuaçãoCompanhias operadoras e empresas integradoras de telefonia fixa, móvel e
de internet.
Empresas de comunicação de dados.
Empresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria. Operadoras de TV aberta e por assinatura.
Provedores de serviços e acesso à internet.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas
Possibilidades de prosseguimento
de estudos na Pós-Graduação
2143-70 - Especialista em telecomunicações (tecnólogo).
2143-70 - Tecnólogo em redes de telecomunicações.
2143-70 - Tecnólogo em telecomunicações.
Pós-graduação na área de Engenharia Elétrica.
Pós-graduação na área de Ciência da Computação, entre outras.
59CURSO SUPERIOR DE TECNOLOGIA EM SEGURANÇA DA INFORMAÇÃO
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusãoAnalisa, projeta, desenvolve, gerencia, testa, implanta, integra, propõe e avalia
soluções para a garantia da confidencialidade, integridade e disponibilidade dos
recursos de Tecnologia da Informação. Gerencia, aplica, administra e configura
ambientes corporativos com requisitos de segurança. Realiza análises de riscos,
gerencia sistemas de informações. Projeta e gerencia redes de computadores
seguras. Realiza auditorias. Planeja contingências e recuperação das informações
em caso de sinistros. Vistoria, realiza perícia, avalia, emite laudo e parecer
técnico em sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado. Laboratório de redes de
computadores.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Campo de atuaçãoEmpresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Empresas de tecnologia.
Empresas em geral (indústria, comércio e serviços).
Organizações não-governamentais.
Órgãos públicos.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas
Possibilidades de prosseguimento
de estudos na Pós-Graduação
2123-20 - Analista em segurança da informação.
2123-20 - Tecnólogo em segurança da informação.
2123-20 - Administrador em segurança da informação.
2124-10 - Analista de redes e de comunicação de dados.
Pós-graduação na área de Ciência da Computação, entre outras.
60CURSO SUPERIOR DE TECNOLOGIA EM SISTEMAS DE TELECOMUNICAÇÕES
2400 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusãoEspecifica, projeta, planeja, desenvolve, implanta, integra, certifica, mantém e
gerencia sistemas de telecomunicações incluindo a infraestrutura de informática
e redes de telecomunicações. Analisa e propõe alternativas de integração,
convergência, compatibilidade e eficiência da infraestrutura de sistemas de
telecomunicações, considerando as redes e os equipamentos de informática
envolvidos. Vistoria, realiza perícia, avalia, emite laudo e parecer técnico em
sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de antenas.
Laboratório de redes de computadores.
Laboratório de telecomunicações.
Campo de atuaçãoCompanhias operadoras e empresas integradoras de telefonia fixa, móvel e
de internet.
Empresas de comunicação de dados.
Empresas de radiodifusão e radiotransmissão.
Empresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.Indústrias de equipamentos e dispositivos de telecomunicações
e telemática.
Provedores de serviços e acesso à internet.
Televisão aberta e por assinatura.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas2143-70 - Especialista em telecomunicações (tecnólogo).
2143-70 - Tecnólogo em sistemas de telecomunicações.
2143-70 - Tecnólogo em telecomunicações.
Possibilidades de prosseguimento
de estudos na Pós-GraduaçãoPós-graduação na área de Ciência da Computação.
Pós-graduação na área de Engenharia Elétrica, entre outras.
61CURSO SUPERIOR DE TECNOLOGIA EM SISTEMAS EMBARCADOS
2400 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusãoEspecifica e desenvolve software para microcontroladores, microprocessadores
e dispositivos de lógica reconfigurável. Projeta hardware para sistemas
embarcados. Aplica técnicas de engenharia de software, de projeto de circuitos
eletroeletrônicos e de design de produto no desenvolvimento de sistemas
embarcados. Testa e avalia o desempenho de sistemas embarcados. Especifica
requisitos mínimos de hardware e software para sistemas embarcados. Utiliza
adequadamente ferramentas, equipamentos, dispositivos e ambientes de
programação, no projeto de sistemas embarcados. Participa de equipes de
projeto e gerencia equipes técnicas na área de desenvolvimento de sistemas
embarcados. Realiza estudos de viabilidade técnica e econômica na área. Vistoria,
realiza perícia, avalia, emite laudo e parecer técnico em sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de hardware com microcontroladores, microprocessadores e
dispositivos de lógica reconfigurável.
Campo de atuaçãoEmpresas do setor automotivo.
Indústrias de equipamentos de automação e controle.
Indústrias de equipamentos de segurança.
Indústrias de equipamentos de telecomunicações.
Indústrias do setor eletroeletrônico.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas
Possibilidades de prosseguimento
de estudos na Pós-Graduação
2143-65 -Tecnólogo em eletrônica.
Pós-graduação na área de Ciência da Computação.
Pós-graduação na área de Engenharia Elétrica, entre outras.
62CURSO SUPERIOR DE TECNOLOGIA EM SISTEMAS PARA INTERNET
2000 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusãoProjeta, desenvolve, testa, implanta, mantém, avalia e analisa páginas para
sites de Internet e intranets, sistemas de comércio eletrônico e aplicativos
para plataformas móveis para a Internet. Avalia, especifica, seleciona e utiliza
metodologias e ferramentas adequadas para o desenvolvimento das aplicações.
Elabora e estabelece diretrizes para a criação de interfaces adequadas à aplicação
de acordo com características, necessidades e público-alvo. Vistoria, realiza
perícia, avalia, emite laudo e parecer técnico em sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Campo de atuaçãoEmpresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Empresas de tecnologia.
Empresas em geral (indústria, comércio e serviços).
Organizações não-governamentais.
Órgãos públicos.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Ocupações CBO associadas2124-05 - Analista de desenvolvimento de sistemas.
2124-05 - Analista de sistemas para internet.
2124-05 - Tecnólogo em análise de desenvolvimento de sistema.
2124-05 - Tecnólogo em sistemas para internet.
Possibilidades de prosseguimento
de estudos na Pós-GraduaçãoPós-graduação na área de Sistema de Computação, entre outras.
63CURSO SUPERIOR DE TECNOLOGIA EM TELEMÁTICA
2400 horas
Eixo Tecnológico: INFORMAÇÃO E COMUNICAÇÃO
Perfil profissional de conclusãoEspecifica, projeta, planeja, desenvolve, implanta, integra e gerencia serviços
informáticos por meio de redes de telecomunicações, estruturas físicas e lógicas
de redes de telecomunicação e dados, redes de monitoramento e controle.
Desenvolve protocolos e aplicações para comunicação de dados que associem
meios de informática. Vistoria, realiza perícia, avalia, emite laudo e parecer
técnico em sua área de formação.
Infraestrutura mínima requeridaBiblioteca incluindo acervo específico e atualizado.
Laboratório de informática com programas e equipamentos compatíveis com
as atividades educacionais do curso.
Laboratório de redes de computadores.
Laboratório de telecomunicações.
Institutos e Centros de Pesquisa.
Instituições de Ensino, mediante formação requerida pela legislação vigente.
Campo de atuaçãoEmpresas do setor da TV digital.
Empresas de planejamento, desenvolvimento de projetos, assistência técnica
e consultoria.
Indústrias e integradores de equipamentos e serviços de telemática.
Indústrias e empresas de automação que utilizem ou apliquem equipamentos
ou serviços de telemática.
Ocupações CBO associadas
Possibilidades de prosseguimento
de estudos na Pós-Graduação
2143-70 - Tecnólogo em telecomunicações.
Pós-graduação na área de Engenharia Elétrica.
Pós-graduação em Ciência da Computação, entre outras."""


def aux():
    areas = TXT.split("CURSO SUPERIOR DE ")
    areas = [area.split("00 horas") for area in areas if "00 horas" in area]
    begin, end = "Perfil profissional de conclusão", "Infraestrutura mínima requerida"
    areas = [(nome.split("\n")[0], perfil.split(begin)[1].split(end)[0]) for nome, perfil in areas]
    [print(f'("{nome}",\n"""{perfil}"""),') for nome, perfil in areas]


t =[c for c, p in CURSO]
tg = dict(TAG)
# [print(f"a{b}='{a}' #{c.replace(' ', '_')}") for a,(b, c) in zip(t, TAG)]
s = [(a, b, a[1:]) for a, b in SUPER.items()]
[print(f"a{b}='{a}'  # {tg[d].replace(' ', '_')}") for a, (b, c, d) in zip(t, s)]
