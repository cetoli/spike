""" Syllabi for project Inep.

Changelog
---------
.. versionadded::    24.06
    |br| first version of horas (22)

.. versionadded::    24.07
    |br| betters csv generation (18)

|   **Open Source Notification:** This file is part of open source program **INEP**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from pathlib import Path
from configuration import TAG
TAG_DICT = {k.lower(): val for val, k in TAG}
DICT_TAG = {val: k.lower()  for val, k in TAG[::-1]}
j = {
    "1666036": [
        ('Projeto Integrador - Elementos e Conceitos de CiberSegurança', '70'),
        ('Sistemas Computacionais para CiberSegurança', '63'),
        ('Estudo do Espaço Cibernético', '63'),
        ('Lógica Matemática', '63'),
        ('Teologia e Fenômeno Humano', '32'),
        ('Vida Universitária e Desenvolvimento Integral', '32'),
        ('Programa de Formação Complementar em Matemática', '32'),
        ('Tecnologias para Cibersegurança', '32'),
        ('Projeto Integrador - CiberSegurança e Criptografia', '70'),
        ('Algoritmo e Estrutura de Dados', '95'),
        ('Princípios Matemático de Criptografia', '32'),
        ('CiberSegurança em Sistemas Operacionais', '63'),
        ('Métodos, Normas e Padrões em CiberSegurança', '63'),
        ('Ética e Antropologia Teológica', '32'),
        ('PF - Práticas de Formação I', '16'),
        ('Projeto Integrador - CiberSegurança em Redes e Infraestrutura', '70'),
        ('Algoritmo e Estrutura de Dados', '95'),
        ('Organização e Arquitetura de Computadores - CiberSegurança', '63'),
        ('CiberSegurança em Redes de Computadores', '95'),
        ('Computação Forense', '32'),
        ('Atividades Complementares I - CiberSegurança', '65'),
        ('Projeto Integrador - CiberSegurança em Programação Segura', '70'),
        ('Cibersegurança em Banco de Dados', '95'),
        ('Criptografia Simétrica e Assimétrica', '32'),
        ('Programação Orientada a Objetos - CiberSegurança', '63'),
        ('Desenvolvimento Seguro de Software', '63'),
        ('Teologia e Sociedade', '48'),
        ('PF: Práticas de Formação II', '16'),
        ('Projeto Integrador - CiberSegurança de Borda e em Sistemas Distribuídos', '70'),
        ('Inteligência Artificial em CiberSegurança', '63'),
        ('Sistemas Paralelos e Distribuídos - Programação e Segurança', '63'),
        ('Sistemas Ciberfísicos e IoT', '32'),
        ('Técnicas Avançadas de Criptografia', '32'),
        ('Engenharia Reversa de Software', '63'),
        ('Educação em Direitos Humanos: História, Cultura e Meio Ambiente', '48'),
        ('Projeto Integrador - Computação em Nuvem e Novos Model', 'os'),
        ('Computacionais de CiberSegurança', '70'),
        ('CiberSegurança em Computação em Nuvem', '63'),
        ('Programação para WEB e dispositivos Móveis', '95'),
        ('CiberSegurança de Sistemas', '63'),
        ('Modelagem de Ameaças', '63'),
        ('PF: Práticas de Formação III', '16'),
        ('Atividades Complementares II - CiberSegurança', '65'),
        ('Tópicos em CiberSegurança I', '63'),
        ('Projeto Aplicado I - CiberSegurança1', '01'),
        ('Governança de CiberSegurança', '32'),
        ('Gestão de Riscos em CiberSegurança', '32'),
        ('Segurança Defensiva e Ofensiva', '63'),
        ('Sistemas de Detecção e Prevenção de Intrusão', '63'),
        ('Atividades Complementares III - CiberSegurança', '65'),
        ('Tópicos em CiberSegurança II', '63'),
        ('Projeto Aplicado II - CiberSegurança1', '01'),
        ('Plano de Privacidade em CiberSegurança', '63'),
        ('Direito Digital Nacional e Internacional', '32'),
        ('Inteligência e Espionagem em CiberSegurança', '32'),
        ('Relações Internacionais e CiberSegurança', '32'),
        ('Usabilidade e Experiência do Usuário em CiberSegurança', '32'),
        ('Atividades Complementares IV - CiberSegurança', '59'),
        ('__TOTAL__', '3204')  # este item deve ter esse nome __TOTAL__ seguido do número de horas
    ],
    "1671887":
    """Cód.
3847(Fev/Jun)Ambientação Digital0,510100
3741(fev)Algoritmos4806020
1446(mar.)Sistemas Operacionais3605010
2661(abr.)Computação em Nuvem480800
2662(mai.)Segurança da Informação480800
1338(jun.)Programação de Computadores2401030
Plano de Acompanhamento de Carreira em Cibersegurança0,510100
2,550050
TOTAL20,5-300110
TOTAL EM HORAS-RELÓGIO410
Cód Novo Fev/jun)
Atividades de Extensão
9845
(Fev/Jun)
Integração de Competências para Transformar o Eu28
Cód.
Disc.
Ordem
Oferta
2º Semestre
C/H
SemanalCHR
TotalCHR
TeóricaCHR
Prática
Disciplinas do Curso
2653(ago.)Tecnologias de Redes4806020
1578(set.)Análise e Controle de Risco480800
2667(Out.)Administração de Serviços3602040
3887(nov.)Segurança de Sistemas para Internet2401030
2657(dez.)Sistemas Linux3602040
Plano de Acompanhamento de Carreira em Cibersegurança I0,510100
Integração de Competências para Transformar o Eu, o Outro e a
2,5
Sociedade.50050
-200180
Cód. Novo (ago/dez)
Atividades de Extensão
9845
(ago/dez)
TOTAL19
TOTAL EM HORAS-RELÓGIO38029
Cód. Disc.
Ordem
Oferta
3º Semestre
C/H
SemanalCHR
TotalCHR
TeóricaCHR
Prática
Disciplinas do Curso
11524(fev.)Criptografia480800
1802(mar.)Modelos de Governança da Tecnologia da Informação480800
Cód. Novo(mar.)Programação de Redes2401030
11526(abr.)Gestão e Análise de Riscos480800
(mai.)Segurança em Sistemas Operacionais4806020
Cód. Novo(jun.)Tópicos Especiais em Cibersegurança I360600
Cód. Novo(fev/jun.)Projeto Integrado Transdisciplinar em Cibersegurança I3601050
50050
-380150
11528
Atividades de Extensão
Cód. Novo
(fev/jun)
Atividade de Extensão: Integração de Competências em Cibersegurança
2,5
I
TOTAL26,5
TOTAL EM HORAS-RELÓGIO53030
Cód. Disc.
Ordem
Oferta
4º Semestre
C/H
SemanalCHR
TotalCHR
TeóricaCHR
Prática
Disciplinas do Curso
Cód. Novo(ago.)Computação Forense4806020
Cód. Novo
11539(set.)Segurança Defensiva – Blue Team4804040
(out.)Tópicos Avançados em Segurança da Informação480800
Cód. Novo(nov.)Tópicos Especiais em Cibersegurança II360600
11540(dez.)Ethical Hacking480800
Cód. Novo(ago/dez.)Projeto Integrador Transdisciplinar em Cibersegurança II3601050
50050
-330160
Atividades de Extensão
Cód. Novo
(ago/dez.)
Atividade de Extensão: Integração de Competências em Cibersegurança
2,5
II
TOTAL24,5
TOTAL EM HORAS-RELÓGIO49031
Resumo da Matriz Curricular
Cibersegurança (Experimental)
do
Curso
Superior
de
Tecnologia
em
CHR TeóricaCHR Prática
Disciplinas do Curso1210400
Atividades de Extensão-200
Atividades Complementares150-
·40-
TOTAL1.400600
TOTAL EM HORAS-RELÓGIO2.000
Temas Transversais"""
}
h = {
    "1666036": [
        ('Projeto Integrador - Elementos e Conceitos de CiberSegurança', '70'),
        ('Sistemas Computacionais para CiberSegurança', '63'),
        ('Estudo do Espaço Cibernético', '63'),
        ('Lógica Matemática', '63'),
        ('Teologia e Fenômeno Humano', '32'),
        ('Vida Universitária e Desenvolvimento Integral', '32'),
        ('Programa de Formação Complementar em Matemática', '32'),
        ('Tecnologias para Cibersegurança', '32'),
        ('Projeto Integrador - CiberSegurança e Criptografia', '70'),
        ('Algoritmo e Estrutura de Dados', '95'),
        ('Princípios Matemático de Criptografia', '32'),
        ('CiberSegurança em Sistemas Operacionais', '63'),
        ('Métodos, Normas e Padrões em CiberSegurança', '63'),
        ('Ética e Antropologia Teológica', '32'),
        ('PF - Práticas de Formação I', '16'),
        ('Projeto Integrador - CiberSegurança em Redes e Infraestrutura', '70'),
        ('Algoritmo e Estrutura de Dados', '95'),
        ('Organização e Arquitetura de Computadores - CiberSegurança', '63'),
        ('CiberSegurança em Redes de Computadores', '95'),
        ('Computação Forense', '32'),
        ('Atividades Complementares I - CiberSegurança', '65'),
        ('Projeto Integrador - CiberSegurança em Programação Segura', '70'),
        ('Cibersegurança em Banco de Dados', '95'),
        ('Criptografia Simétrica e Assimétrica', '32'),
        ('Programação Orientada a Objetos - CiberSegurança', '63'),
        ('Desenvolvimento Seguro de Software', '63'),
        ('Teologia e Sociedade', '48'),
        ('PF: Práticas de Formação II', '16'),
        ('Projeto Integrador - CiberSegurança de Borda e em Sistemas Distribuídos', '70'),
        ('Inteligência Artificial em CiberSegurança', '63'),
        ('Sistemas Paralelos e Distribuídos - Programação e Segurança', '63'),
        ('Sistemas Ciberfísicos e IoT', '32'),
        ('Técnicas Avançadas de Criptografia', '32'),
        ('Engenharia Reversa de Software', '63'),
        ('Educação em Direitos Humanos: História, Cultura e Meio Ambiente', '48'),
        ('Projeto Integrador - Computação em Nuvem e Novos Modelos Computacionais de CiberSegurança', '70'),
        ('Computacionais de CiberSegurança', '70'),
        ('CiberSegurança em Computação em Nuvem', '63'),
        ('Programação para WEB e dispositivos Móveis', '95'),
        ('CiberSegurança de Sistemas', '63'),
        ('Modelagem de Ameaças', '63'),
        ('PF: Práticas de Formação III', '16'),
        ('Atividades Complementares II - CiberSegurança', '65'),
        ('Tópicos em CiberSegurança I', '63'),
        ('Projeto Aplicado I - CiberSegurança', '101'),
        ('Governança de CiberSegurança', '32'),
        ('Gestão de Riscos em CiberSegurança', '32'),
        ('Segurança Defensiva e Ofensiva', '63'),
        ('Sistemas de Detecção e Prevenção de Intrusão', '63'),
        ('Atividades Complementares III - CiberSegurança', '65'),
        ('Tópicos em CiberSegurança II', '63'),
        ('Projeto Aplicado II - CiberSegurança', '101'),
        ('Plano de Privacidade em CiberSegurança', '63'),
        ('Direito Digital Nacional e Internacional', '32'),
        ('Inteligência e Espionagem em CiberSegurança', '32'),
        ('Relações Internacionais e CiberSegurança', '32'),
        ('Usabilidade e Experiência do Usuário em CiberSegurança', '32'),
        ('Atividades Complementares IV - CiberSegurança', '59'),
        ('__TOTAL__', '3204')  # este item deve ter esse nome __TOTAL__ seguido do número de horas
    ],
    "1671887": [
        ('Ambientação Digital', '10'),
        ('Algoritmos', '80'),
        ('Sistemas Operacionais', '60'),
        ('Computação em Nuvem', '80'),
        ('Segurança da Informação', '80'),
        ('Programação de Computadores', '40'),
        ('Plano de Acompanhamento de Carreira em Cibersegurança', '10'),
        ('Integração de Competências para Transformar o Eu', '50'),
        ('Tecnologias de Redes', '80'),
        ('Análise e Controle de Risco', '80'),
        ('Administração de Serviços', '60'),
        ('Segurança de Sistemas para Internet', '40'),
        ('Sistemas Linux', '60'),
        ('Plano de Acompanhamento de Carreira em Cibersegurança I', '10'),
        ('Integração de Competências para Transformar o Eu, o Outro e a Sociedade', '50'),
        ('Criptografia', '80'),
        ('Modelos de Governança da Tecnologia da Informação', '80'),
        ('Programação de Redes', '40'),
        ('Gestão e Análise de Riscos', '80'),
        ('Segurança em Sistemas Operacionais', '80'),
        ('Tópicos Especiais em Cibersegurança I', '60'),
        ('Projeto Integrado Transdisciplinar em Cibersegurança I', '60'),
        ('Atividade de Extensão: Integração de Competências em Cibersegurança I', '50'),
        ('Computação Forense', '80'),
        ('Segurança Defensiva – Blue Team', '80'),
        ('Tópicos Avançados em Segurança da Informação', '80'),
        ('Tópicos Especiais em Cibersegurança II', '60'),
        ('Ethical Hacking', '80'),
        ('Projeto Integrador Transdisciplinar em Cibersegurança II', '60'),
        ('Atividade de Extensão: Integração de Competências em Cibersegurança II', '50'),
        ('Língua Brasileira de Sinais', '40'),
        ('__TOTAL__', '2000')
    ],
    "1598939": [
        ('Ambientação Digital', '20'),
        ('Aplicações para Internet', '80'),
        ('Engenharia de Requisitos e Processos de Software', '40'),
        ('Tratamento de Imagens Gráfica e Digital', '40'),
        ('Língua Portuguesa', '80'),
        ('Interface Humano-Computador', '80'),
        ('Programação de Computadores', '40'),
        ('Sistemas Operacionais Mobiles', '60'),
        ('Plano de Acompanhamento de Carreira em Desenvolvimento Mobile', '10'),
        ('Atividades de Extensão: Integração de Competências para Transformar o Eu', '50'),
        ('Processos Ágeis de Desenvolvimento', '60'),
        ('Modelagem de Dados', '80'),
        ('Técnicas de Desenvolvimento de Algoritmos', '80'),
        ('Design de Experiência do Usuário', '40'),
        ('Programação Web', '80'),
        ('Programação Orientada a Objetos', '80'),
        ('Plano de Acompanhamento de Carreira em Desenvolvimento Mobile I', '10'),
        ('Atividades de Extensão: Integração de Competências para Transformar o Eu, o Outro e a Sociedade', '50'),
        ('Banco de Dados', '40'),
        ('Arquitetura para Aplicações Móveis', '40'),
        ('Soluções Web/Mobile', '80'),
        ('Computação em Nuvem', '80'),
        ('Desenvolvimento Mobile I', '40'),
        ('Segurança em Dispositivos Móveis', '60'),
        ('Tópicos Especiais em Desenvolvimento Mobile I', '40'),
        ('Plano de Acompanhamento de Carreira em Desenvolvimento Mobile II', '10'),
        ('Atividades de Extensão: Integração de Competências em Desenvolvimento Mobile I', '50'),
        ('Arquitetura de Sistemas Distribuídos', '40'),
        ('Desenvolvimento Mobile II', '80'),
        ('Negócios Digitais', '60'),
        ('Tópicos Especiais em Dispositivos Móveis', '80'),
        ('Desenvolvimento de Aplicações para Internet das Coisas', '60'),
        ('Tópicos Especiais em Desenvolvimento Mobile II', '40'),
        ('Projeto Integrador Transdisciplinar em Desenvolvimento Mobile', '60'),
        ('Plano de Acompanhamento de Carreira em Desenvolvimento Mobile III', '10'),
        ('Atividades de Extensão: Integração de Competências em Desenvolvimento Mobile II', '50'),
        ('Língua Brasileira de Sinais', '40'),
        ('__TOTAL__', '2000')
    ],
    "1565359": [
        ('Arquitetura e Organização de Computadores', '90'),
        ('Legislação Aplicada à Tecnologia da Informação', '90'),
        ('Algoritmos e Fundamentos de Programação de Computadores', '90'),
        ('Fundamentos de Programação Mobile', '90'),
        ('Língua Brasileira de Sinais – LIBRAS', '90'),
        ('Noções de Ciências Sociais', '90'),
        ('Desenvolvimento Mobile', '90'),
        ('Empreendedorismo e Processos de Negócios', '90'),
        ('Sistemas Operacionais Mobile', '90'),
        ('Programação Orientada a Objetos', '90'),
        ('Tecnologias de Animação e Programação', '90'),
        ('Banco de Dados', '90'),
        ('Análise e Modelagem de Sistemas Mobile', '90'),
        ('Programação e Desenvolvimento de Banco de Dados Mobile', '90'),
        ('Inovação e Design Thinking', '90'),
        ('Design de Interfaces Humano/Computador', '90'),
        ('Programação de Dispositivos Móveis', '90'),
        ('Implementação de IoT', '90'),
        ('Desenvolvimento de Aplicações Android', '90'),
        ('Desenvolvimento de Aplicações IOS', '90'),
        ('Segurança para Sistemas Mobile', '90'),
        ('__TOTAL__', '2067')
    ],
    "1550008": [
        ('SISTEMAS OPERACIONAIS', '60'),
        ('GOVERNANÇA CORPORATIVA', '60'),
        ('REDES DE COMPUTADORES', '60'),
        ('SOCIEDADE BRASILEIRA E CIDADANIA', '60'),
        ('PROJETO INTEGRADO I', '90'),
        ('LINGUAGEM DE PROGRAMAÇÃO', '60'),
        ('MODELAGEM DE DADOS', '60'),
        ('LÓGICA E MATEMÁTICA COMPUTACIONAL', '60'),
        ('ALGORITMOS E PROGRAMAÇÃO ESTRUTURADA', '60'),
        ('PROGRAMAÇÃO E DESENVOLVIMENTO DE BANCO DE DADOS', '60'),
        ('PROJETO DE EXTENSÃO I - CIBERSEGURANÇA', '115'),
        ('ARQUITETURA DE REDES', '60'),
        ('ARQUITETURA DE SEGURANÇA', '60'),
        ('SEGURANÇA EM ENGENHARIA DE SOFTWARE', '60'),
        ('GOVERNANÇA DE SEGURANÇA', '60'),
        ('PRIVACIDADE E PROTEÇÃO DE DADOS', '60'),
        ('PROJETO INTEGRADO II', '90'),
        ('ADMINISTRAÇÃO DE SISTEMAS OPERACIONAIS', '60'),
        ('GESTÃO DE CONTINUIDADE DE NEGÓCIO', '60'),
        ('SEGURANÇA OFENSIVA - ETHICAL HACKING - RED TEAM', '60'),
        ('SEGURANÇA DA INFORMAÇÃO E DE REDES', '60'),
        ('PROJETO DE EXTENSÃO II - CIBERSEGURANÇA', '115'),
        ('COMPUTAÇÃO EM NUVEM', '60'),
        ('GERENCIAMENTO DE REDES', '60'),
        ('PERÍCIA FORENSE EM SEGURANÇA DA INFORMAÇÃO', '60'),
        ('PROGRAMAÇÃO PARA REDES', '60'),
        ('SEGURANÇA DEFENSIVA - BLUE TEAM', '60'),
        ('CRIPTOGRAFIA', '60'),
        ('PROJETO INTEGRADO III', '90'),
        ('LIBRAS - LÍNGUA BRASILEIRA DE SINAIS', '60'),
        ('DIREITO CIBERNÉTICO', '60'),
        ('ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES', '60'),
        ('ARQUITETURA DE COMPUTAÇÃO EM NUVEM', '60'),
        ('RESPONSABILIDADE SOCIAL E AMBIENTAL', '60'),
        ('__TOTAL__', '2100')
    ],
    "1537675": [
        ('PROJETO DE SOFTWARE', '60'),
        ('ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES', '60'),
        ('SEGURANÇA E AUDITORIA DE SISTEMAS', '60'),
        ('INTERFACE E USABILIDADE', '60'),
        ('PROJETO INTEGRADO I', '110'),
        ('ENGENHARIA DE SOFTWARE', '60'),
        ('LINGUAGEM DE PROGRAMAÇÃO', '60'),
        ('LÓGICA E MATEMÁTICA COMPUTACIONAL', '60'),
        ('ALGORITMOS E PROGRAMAÇÃO ESTRUTURADA', '60'),
        ('ANÁLISE E MODELAGEM DE SISTEMAS', '60'),
        ('PROJETO DE EXTENSÃO I - DESENVOLVIMENTO MOBILE', '90'),
        ('ANÁLISE ORIENTADA A OBJETOS', '60'),
        ('LINGUAGEM ORIENTADA A OBJETOS', '60'),
        ('MODELAGEM DE DADOS', '60'),
        ('DESENVOLVIMENTO MOBILE', '60'),
        ('PROGRAMAÇÃO E DESENVOLVIMENTO DE BANCO DE DADOS', '60'),
        ('PROJETO INTEGRADO II', '110'),
        ('DESENVOLVIMENTO DE APLICAÇÕES ANDROID', '60'),
        ('DESENVOLVIMENTO DE APLICAÇÕES IOS', '60'),
        ('PROJETOS DE DESENVOLVIMENTO DE GAMES', '60'),
        ('SOCIEDADE BRASILEIRA E CIDADANIA', '60'),
        ('SISTEMAS OPERACIONAIS MOBILE', '60'),
        ('PROJETO DE EXTENSÃO II - DESENVOLVIMENTO MOBILE', '90'),
        ('LIBRAS - LÍNGUA BRASILEIRA DE SINAIS', '60'),
        ('CRIPTOGRAFIA', '60'),
        ('REDES DE COMPUTADORES', '60'),
        ('COMPUTAÇÃO EM NUVEM', '60'),
        ('PRIVACIDADE E PROTEÇÃO DE DADOS', '60'),
        ('RESPONSABILIDADE SOCIAL E AMBIENTAL', '60'),
        ('__TOTAL__', '1700')
    ],
    "153693": [
        ('PROJETO DE SOFTWARE', '60'),
        ('ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES', '60'),
        ('SEGURANÇA E AUDITORIA DE SISTEMAS', '60'),
        ('SOCIEDADE BRASILEIRA E CIDADANIA', '60'),
        ('PROJETO INTEGRADO I', '110'),
        ('ENGENHARIA DE SOFTWARE', '60'),
        ('LINGUAGEM DE PROGRAMAÇÃO', '60'),
        ('LÓGICA E MATEMÁTICA COMPUTACIONAL', '60'),
        ('ALGORITMOS E PROGRAMAÇÃO ESTRUTURADA', '60'),
        ('ANÁLISE E MODELAGEM DE SISTEMAS', '60'),
        ('PROJETO DE EXTENSÃO I', '90'),
        ('ANÁLISE ORIENTADA A OBJETOS', '60'),
        ('PROGRAMAÇÃO E DESENVOLVIMENTO DE BANCO DE DADOS', '60'),
        ('MODELAGEM DE DADOS', '60'),
        ('INFRAESTRUTURA ÁGIL', '60'),
        ('REDES E SISTEMAS DISTRIBUÍDOS', '60'),
        ('PROJETO INTEGRADO II', '110'),
        ('DESENVOLVIMENTO E MONITORAMENTO DE DASHBOARDS', '60'),
        ('MONITORAMENTO E INDICADORES', '60'),
        ('LINGUAGEM ORIENTADA A OBJETOS', '60'),
        ('ENTREGA E IMPLANTAÇÃO CONTÍNUA', '60'),
        ('QUALIDADE E AUTOMAÇÃO DE TESTES', '60'),
        ('PROJETO DE EXTENSÃO II', '90'),
        ('LIBRAS - LÍNGUA BRASILEIRA DE SINAIS', '60'),
        ('RESPONSABILIDADE SOCIAL E AMBIENTAL', '60'),
        ('PRIVACIDADE E PROTEÇÃO DE DADOS', '60'),
        ('GESTÃO DE PROJETOS', '60'),
        ('SISTEMAS DE INFORMAÇÃO GERENCIAL', '60'),
        ('__TOTAL__', '1700')
    ],
    "1625436": [
        ('RACIOCÍNIO LÓGICO', '60'),
        ('FUNDAMENTOS DE REDES DE COMPUTADORES', '60'),
        ('ARQUITETURA DE COMPUTADORES', '60'),
        ('FUNDAMENTOS DE SEGURANÇA CIBERNÉTICA', '60'),
        ('BANCO DE DADOS', '60'),
        ('MATEMÁTICA PARA COMPUTAÇÃO', '60'),
        ('PROGRAMAÇÃO PYTHON', '60'),
        ('ARQUITETURA DE REDES DE COMPUTADORES', '60'),
        ('SISTEMAS OPERACIONAIS', '60'),
        ('ÉTICA E RESPONSABILIDADE SOCIAL', '60'),
        ('COMPUTAÇÃO EM NUVEM', '60'),
        ('MÉTODOS DE CRIPTOGRAFIA', '60'),
        ('CONFIGURAÇÃO E SERVIÇO DE REDES', '60'),
        ('ADMINISTRAÇÃO DE REDES WINDOWS E LINUX', '60'),
        ('FORENSE COMPUTACIONAL', '60'),
        ('INTERNET DAS COISAS', '60'),
        ('SEGURANÇA CIBERNÉTICA COM INTELIGENCIA ARTIFICIAL', '60'),
        ('PROJETO DE DESENVOLVIMENTO SEGURO DE REDES NETSEC E OWASP', '60'),
        ('TRATAMENTO DE INCIDENTES DE SEGURANÇA', '60'),
        ('SEGURANÇA CIBERNÉTICA: ETHICAL HACKING', '60'),
        ('OPERAÇÕES DE SEGURANÇA NOC E SOC', '60'),
        ('SEGURANÇA DE AUTOMAÇÃO', '60'),
        ('ORIENTAÇÃO E PRÁTICAS DE EXTENSÃO EM SEGURANÇA DIGITAL', '60'),
        ('PROJETO DE PROTEÇÃO DE SISTEMAS OPERACIONAIS CYBEROPS', '160'),
        ('__TOTAL__', '1600')
    ],
    "1617717": [
        ('Redes de Computadores', '80'),
        ('Fundamentos e Arquitetura de Computadores', '80'),
        ('GO - Projeto de Vida', '80'),
        ('Gestão de Serviços em TI', '80'),
        ('Produção do Conhecimento Científico, Tecnológico e Disrupção', '80'),
        ('Sistemas Operacionais', '80'),
        ('Cibersegurança', '80'),
        ('Linguagem de Programação', '80'),
        ('Mentalidade Criativa e Empreendedora', '80'),
        ('Segurança e Auditoria de Sistemas', '80'),
        ('Administração de Redes Windows', '80'),
        ('Técnicas de Hacking em Hardware', '80'),
        ('Perícia Forense Computacional', '80'),
        ('Administração de Redes Linux', '80'),
        ('Imersão Profissional: Administração de SO e Serviços', '60'),
        ('Inteligência e Ameaça Cibernética', '80'),
        ('Gestão de Projetos Tecnológicos', '80'),
        ('Imersão Profissional: Controle de Ameaça Cibernética', '60'),
        ('Análise de Malware e Engenharia Reversa', '80'),
        ('Cloud Computing', '80'),
        ('Estudo Contemporâneo e Transversal: Autonomia Intelectual, Relação de Consumo e Sustentabilidade', '40'),
        ('Imersão profissional: Prática de Engenharia Reversa', '60'),
        ('Direito Digital', '80'),
        ('Ethical Hacker', '80'),
        ('Estudo Contemporâneo e Transversal: Relações Étnico-Raciais, Cultura e Direitos Humanos', '40'),
        ('Imersão profissional: Avaliação da Segurança de Sistemas', '60'),
        ('LIBRAS', '80'),
        ('__TOTAL__', '2178')
    ],
    "1615338": [
        ('INTERFACE HUMANO-COMPUTADOR', '80'),
        ('FUNDAMENTOS E ARQUITETURA DE COMPUTADORES', '80'),
        ('GO PROJETO DE VIDA', '80'),
        ('PROGRAMAÇÃO FRONT END', '80'),
        ('PRODUÇÃO DO CONHECIMENTO CIENTÍFICO, TECNOLÓGICO E DISRUPÇÃO', '80'),
        ('ENGENHARIA DE SOFTWARE', '80'),
        ('ALGORITMOS E LÓGICA DE PROGRAMAÇÃO', '80'),
        ('LINGUAGEM DE PROGRAMAÇÃO', '80'),
        ('MENTALIDADE CRIATIVA E EMPREENDEDORA', '80'),
        ('ANÁLISE E PROJETO ORIENTADO A OBJETOS', '80'),
        ('PROJETO DE APLICAÇÕES MÓVEIS', '80'),
        ('DESIGN GRÁFICO', '80'),
        ('BANCO DE DADOS', '80'),
        ('BANCO DE DADOS NoSQL', '80'),
        ('IMERSÃO PROFISSIONAL: PROJETO DE BANCO DE DADOS PARA APLICATIVO', '60'),
        ('PROGRAMAÇÃO ORIENTADA A OBJETOS', '80'),
        ('GESTÃO DE PROJETOS TECNOLÓGICOS', '80'),
        ('IMERSÃO PROFISSIONAL: PROJETO DE APLICATIVO ORIENTADO A OBJETOS', '60'),
        ('DESENVOLVIMENTO DE APLICAÇÕES ANDROID', '80'),
        ('CLOUD COMPUTING', '80'),
        ('IMERSÃO PROFISSIONAL: CRIANDO UMA APLICAÇÃO ANDROID', '60'),
        ('ESTUDO CONTEMPORÂNEO E TRANSVERSAL: AUTONOMIA INTELECTUAL, RELAÇÃO DE CONSUMO E SUSTENTABILIDADE', '40'),
        ('DESENVOLVIMENTO DE APLICAÇÕES IOS', '80'),
        ('APLICAÇÕES HÍBRIDAS E IOT', '80'),
        ('IMERSÃO PROFISSIONAL: FÁBRICA DE SOFTWARE – APLICAÇÃO HÍBRIDA', '60'),
        ('ESTUDO CONTEMPORÂNEO E TRANSVERSAL: RELAÇÕES ÉTNICO-RACIAIS, CULTURA E DIREITOS HUMANOS', '40'),
        ('LIBRAS', '80'),
        ('__TOTAL__', '2178')
    ],
    "1617840": [
        ('PERSPECTIVAS PROFISSIONAIS', '80'),
        ('ARQUITETURA DE COMPUTADORES', '80'),
        ('LÓGICA E TÉCNICAS DE PROGRAMAÇÃO', '80'),
        ('SEGURANÇA E TECNOLOGIA DA INFORMAÇÃO', '80'),
        ('IMERSÃO PROFISSIONAL: CARREIRA E SUCESSO', '40'),
        ('PRODUÇÃO DO CONHECIMENTO CIENTÍFICO E TECNOLOGIAS IMERGENTES', '80'),
        ('INFRAESTRUTURA DE TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO', '80'),
        ('CIBERSEGURANÇA', '80'),
        ('SISTEMAS E APLICAÇÕES DISTRIBUÍDAS', '80'),
        ('IMERSÃO PROFISSIONAL: DESAFIOS CONTEMPORÂNEOS', '40'),
        ('EMPREENDEDORISMO CRIATIVO', '80'),
        ('TEORIA GERAL DO DIREITO DIGITAL', '80'),
        ('HACKING EM HARDWARE', '80'),
        ('PERÍCIA DIGITAL', '80'),
        ('IMERSÃO PROFISSIONAL: HACKING E PERÍCIA DIGITAL', '40'),
        ('CIDADANIA E PROTAGONISMO SOCIAL', '80'),
        ('CLOUD COMPUTING E DEPLOY NA NUVEM', '80'),
        ('SISTEMAS OPERACIONAIS PARA REDES', '80'),
        ('AMEAÇA CIBERNÉTICA E INTELIGÊNCIA', '80'),
        ('IMERSÃO PROFISSIONAL: PREVENÇÃO DE ATAQUES CIBERNÉTICOS', '40'),
        ('ESTUDO CONTEMPORÂNEO E TRANSVERSAL: INDÚSTRIA, TRANSFORMAÇÃO DIGITAL E INOVAÇÃO', '10'),
        ('FUNDAMENTOS DE ETHICAL HACKING', '80'),
        ('ENGENHARIA REVERSA E ANÁLISE DE MALWARE', '80'),
        ('GERENCIAMENTO DE PROJETO E GOVERNANÇA DE TI', '80'),
        ('TECNOLOGIAS EMERGENTES EM CIBERSEGURANÇA', '80'),
        ('IMERSÃO PROFISSIONAL: ENGENHARIA REVERSA E DEFESA CIBERNÉTICA', '40'),
        ('ESTUDO CONTEMPORÂNEO E TRANSVERSAL: PROPRIEDADE INTELECTUAL, LEITURA DE IMAGENS, GRÁFICOS E MAPAS', '10'),
        ('__TOTAL__', '2063')
    ],
    "1617841": [
        ('PERSPECTIVAS PROFISSIONAIS', '80'),
        ('SEGURANÇA EM DISPOSITIVOS MÓVEIS E AMBIENTE WEB', '80'),
        ('LÓGICA E TÉCNICAS DE PROGRAMAÇÃO', '80'),
        ('INTERAÇÃO HUMANO COMPUTADOR', '80'),
        ('IMERSÃO PROFISSIONAL: CARREIRA E SUCESSO', '40'),
        ('PRODUÇÃO DO CONHECIMENTO CIENTÍFICO E TECNOLOGIAS IMERGENTES', '80'),
        ('ENGENHARIA E PROJETO DE SOFTWARE', '80'),
        ('FUNDAMENTOS DE REDES DE COMPUTADORES', '80'),
        ('INTRODUÇÃO AO DESENVOLVIMENTO DE SISTEMAS WEB', '80'),
        ('IMERSÃO PROFISSIONAL: DESAFIOS CONTEMPORÂNEOS', '40'),
        ('EMPREENDEDORISMO CRIATIVO', '80'),
        ('BANCO DE DADOS', '80'),
        ('GERÊNCIA DE PROJETOS', '80'),
        ('DESENVOLVIMENTO DE APLICAÇÕES MÓVEIS', '80'),
        ('IMERSÃO PROFISSIONAL: PROJETO DE APLICAÇÕES MÓVEIS', '40'),
        ('CIDADANIA E PROTAGONISMO SOCIAL', '80'),
        ('ANÁLISE ORIENTADA A OBJETOS', '80'),
        ('PROGRAMAÇÃO ORIENTADA A OBJETOS', '80'),
        ('DESENVOLVIMENTO DE APLICAÇÕES PARA ANDROID', '80'),
        ('IMERSÃO PROFISSIONAL: PROJETO DE APLICATIVO ANDROID', '40'),
        ('ESTUDO CONTEMPORÂNEO E TRANSVERSAL: INDÚSTRIA, TRANSFORMAÇÃO DIGITAL E INOVAÇÃO', '10'),
        ('DESENVOLVIMENTO DE APLICAÇÕES PARA IOS', '80'),
        ('DESENVOLVIMENTO DE APLICAÇÕES HÍBRIDAS E IOT', '80'),
        ('PROGRAMAÇÃO PARA WEB', '80'),
        ('MARKETING DIGITAL E MÍDIAS SOCIAIS', '80'),
        ('IMERSÃO PROFISSIONAL: PROJETO DE APLICAÇÃO HÍBRIDA', '40'),
        ('ESTUDO CONTEMPORÂNEO E TRANSVERSAL: PROPRIEDADE INTELECTUAL, LEITURA DE IMAGENS, GRÁFICOS E MAPAS', '10'),
        ('__TOTAL__', '2067')
    ],
    "1517110": [
        ('Formação Inicial em Educação a Distância', '40'),
        ('Estudos das Relações Étnico-Raciais e para o Ensino de História e Cultura Afro-Brasileira e Africana', '65'),
        ('Libras', '40'),
        ('Lógica de Programação e Algoritmos', '65'),
        ('Interface Humano - Computador', '65'),
        ('Bancos de dados', '65'),
        ('Análise de Sistemas', '65'),
        ('Engenharia de Software', '65'),
        ('Matemática Computacional', '65'),
        ('Programação Orientada a Objetos', '65'),
        ('Sistema Gerenciador de Banco de Dados', '65'),
        ('Atividades Extensionistas I - Tecnologia aplicada à Inclusão Digital - Levantamento', '110'),
        ('Inteligência Artificial Aplicada', '65'),
        ('Estética e Design Aplicado a Publicidade', '65'),
        ('Metodologia de Design e Concepção', '65'),
        ('Segurança em Sistemas de Informação', '65'),
        ('Aplicação Web e Móveis', '65'),
        ('Computação em Nuvem', '65'),
        ('Programação I', '65'),
        ('Gestão de Startups', '65'),
        ('Banco de Dados NoSQL', '65'),
        ('Design para Aplicativos Móveis', '65'),
        ('Programação II', '65'),
        ('Segurança em Dispositivos Móveis', '65'),
        ('Atividades Extensionistas II - Tecnologia aplicada à Inclusão Digital - Projeto', '110'),
        ('Internet das Coisas', '65'),
        ('Gestão de Projetos', '65'),
        ('Programação III', '65'),
        ('Legislação, Ética e Conformidade', '65'),
        ('Arquitetura e Desenvolvimento de APIs para Back-end', '65'),
        ('Testes de Aplicativos Móveis', '65'),
        ('Programação IV', '65'),
        ('Direito Cibernético', '65'),
        ('__TOTAL__', '2145')
    ],
    "1599632": [
        ('Desvendando essa caixa preta', '88'),
        ('Vamos iniciar a jornada!', '88'),
        ('Estruturando os dados', '88'),
        ('Conhecendo um novo paradigma', '88'),
        ('Colocando tudo em ordem', '88'),
        ('Meu primeiro site "cringe"', '88'),
        ('Descobrindo o Javascript', '88'),
        ('Meu primeiro Framework', '88'),
        ('Conhecendo outro Framework', '88'),
        ('Vamos colocar o Framework para acessar um banco', '88'),
        ('Iniciando o caminho pelo Java', '88'),
        ('Vamos manter as informações', '88'),
        ('Back-End sem banco não tem', '88'),
        ('Vamos integrar sistemas', '88'),
        ('Por que não paralelizar', '88'),
        ('Vamos de Python para BackEnd', '88'),
        ('O bom e velho PHP', '88'),
        ('E o C# também funciona', '88'),
        ('Organizando as ideias', '88'),
        ('Vamos criar um App', '88'),
        ('Posso criar um App de outra forma', '88'),
        ('Lidando com sensores em dispositivos móveis', '88'),
        ('Tirando proveito da nuvem para projetos de software', '88'),
        ('Vamos interligar as coisas com a nuvem', '88'),
        ('Vamos conhecer outra nuvem', '88'),
        ('Agora vamos de outra abordagem de computação em nuvem', '88'),
        ('Projeto de Mobile integrado com a nuvem', '88'),
        ('Vamos gerenciar um projeto', '88'),
        ('Empregando métodos ágeis', '88'),
        ('Tratando a imensidão dos dados', '88'),
        ('Dando inteligência ao software', '88'),
        ('Software sem segurança não serve', '88'),
        ('TÓPICOS EM LIBRAS: SURDEZ E INCLUSÃO', '88'),
        ('__TOTAL__', '2260')
    ],
    "1594810": [
        ('ARQUITETURA DE COMPUTADORES', '80'),
        ('FUNDAMENTOS DE REDES DE COMPUTADORES', '80'),
        ('INTRODUÇÃO À PROGRAMAÇÃO ESTRUTURADA EM C', '80'),
        ('INTRODUÇÃO À SEGURANÇA DA INFORMAÇÃO', '80'),
        ('SISTEMAS DE INFORMAÇÃO E SOCIEDADE', '80'),
        ('BANCO DE DADOS', '80'),
        ('COMPUTAÇÃO EM NUVEM', '80'),
        ('DESENVOLVIMENTO WEB EM HTML5, CSS, JAVASCRIPT E PHP', '80'),
        ('PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON', '80'),
        ('ENGENHARIA E MODELAGEM DE SOFTWARE', '80'),
        ('DESENVOLVIMENTO RÁPIDO DE APLICAÇÕES EM PYTHON', '80'),
        ('GESTÃO E CONFIGURAÇÃO DE SERVIÇOS DE REDES WINDOWS', '80'),
        ('MÉTODOS ÁGEIS COM SCRUM', '80'),
        ('PROGRAMAÇÃO ORIENTADA A OBJETOS EM JAVA', '80'),
        ('QUALIDADE E TESTE DE SOFTWARE', '80'),
        ('APLICATIVO DE CLOUD, IOT E INDÚSTRIA 4.0 EM PYTHON', '80'),
        ('GESTÃO DE SERVIÇOS DE TI', '80'),
        ('GESTÃO E CONFIGURAÇÃO DE SERVIÇOS DE REDES LINUX', '80'),
        ('SEGURANÇA CIBERNÉTICA', '80'),
        ('DESENVOLVIMENTO E OPERAÇÕES INTEGRADOS (DEVOPS)', '100'),
        ('PROGRAMAÇÃO PARA DISPOSITIVOS MÓVEIS EM ANDROID', '80'),
        ('TÓPICOS EM LIBRAS: SURDEZ E INCLUSÃO', '80'),
        ('__TOTAL__', '1620')
    ],
    "1667219": [
        ('Introdução ao EAD', '60'),
        ('Lógica de programação e algoritmo', '60'),
        ('Estrutura de dados', '60'),
        ('Fundamentos De Redes De Computadores', '60'),
        ('Arquitetura de computadores', '60'),
        ('Políticas Sociais e Ambientais', '60'),
        ('Gestão de segurança da informação', '60'),
        ('Segurança de dados', '60'),
        ('Introdução ao banco de dados', '60'),
        ('Metodologia científica', '60'),
        ('Computação gráfica', '60'),
        ('Manutenção e otimização de banco de dados', '60'),
        ('Linguagem de programação', '60'),
        ('Respostas a incidentes de segurança', '60'),
        ('Criptografia', '60'),
        ('Análise de vulnerabilidades', '60'),
        ('Ética em cibersegurança', '60'),
        ('Modelagem de Sistemas', '60'),
        ('Sistemas operacionais seguros', '60'),
        ('Segurança defensiva', '60'),
        ('Segurança ofensiva', '60'),
        ('Perícia forense em segurança da informação', '60'),
        ('Direito eletrônico', '60'),
        ('Segurança em sistemas móveis', '60'),
        ('Eletiva I', '60'),
        ('segurança em nuvem', '60'),
        ('Gerenciamento de riscos e compliance', '60'),
        ('Hacking ético e testes de penetração', '60'),
        ('Ética e Responsabilidade Social', '60'),
        ('Eletiva II', '60'),
        ('Inovação em Negócios e Oportunidades', '60'),
        ('Trabalho Conclusão de Curso', '60'),
        ('Atividades de Curricularização de Extensão I', '36'),
        ('Atividades de Curricularização de Extensão II', '36'),
        ('Atividades de Curricularização de Extensão III', '42'),
        ('Atividades de Curricularização de Extensão IV', '36'),
        ('Atividades de Curricularização de Extensão V', '42'),
        ('Novas tecnologias aplicadas à comunicação', '60'),
        ('Empreendedorismo, criatividade e inovação', '60'),
        ('Práticas de Gestão Corporativa', '60'),
        ('Libras – Língua Brasileira de Sinais', '60'),
        ('__TOTAL__', '2020')
    ],
    "1618022": [
        ('Introdução ao EAD', '60'),
        ('Lógica de programação e algoritmo', '60'),
        ('Estrutura de dados', '60'),
        ('Fundamentos De Redes De Computadores', '60'),
        ('Arquitetura de computadores', '60'),
        ('Políticas Sociais e Ambientais', '60'),
        ('Atividades de Curricularização de Extensão I', '36'),
        ('Gestão de segurança da informação', '60'),
        ('Segurança de dados', '60'),
        ('Introdução ao banco de dados', '60'),
        ('Metodologia científica', '60'),
        ('Computação gráfica', '60'),
        ('Manutenção e otimização de banco de dados', '60'),
        ('Atividades de Curricularização de Extensão II', '36'),
        ('Linguagem de programação', '60'),
        ('Respostas a incidentes de segurança', '60'),
        ('Criptografia', '60'),
        ('Análise de vulnerabilidades', '60'),
        ('Ética em cibersegurança', '60'),
        ('Modelagem de Sistemas', '60'),
        ('Sistemas operacionais seguros', '60'),
        ('Atividades de Curricularização de Extensão III', '42'),
        ('Segurança defensiva', '60'),
        ('Segurança ofensiva', '60'),
        ('Perícia forense em segurança da informação', '60'),
        ('Direito eletrônico', '60'),
        ('Segurança em sistemas móveis', '60'),
        ('Eletiva I', '60'),
        ('Atividades de Curricularização de Extensão IV', '36'),
        ('segurança em nuvem', '60'),
        ('Gerenciamento de riscos e compliance', '60'),
        ('Hacking ético e testes de penetração', '60'),
        ('Ética e Responsabilidade Social', '60'),
        ('Eletiva II', '60'),
        ('Inovação em Negócios e Oportunidades', '60'),
        ('Trabalho Conclusão de Curso', '60'),
        ('Atividades de Curricularização de Extensão V', '42'),
        ('Novas tecnologias aplicadas à comunicação', '60'),
        ('Empreendedorismo, criatividade e inovação', '60'),
        ('Práticas de Gestão Corporativa', '60'),
        ('Libras – Língua Brasileira de Sinais', '60'),
        ('__TOTAL__', '2020')
    ],
    "1619434": [
        ('Comunicação, cultura e sociedade', '60'),
        ('Estatística', '60'),
        ('Estrutura de Dados', '60'),
        ('Inteligência Artificial', '60'),
        ('Introdução a EAD', '60'),
        ('Modelo de Gestão', '60'),
        ('Politicas Sociais e Ambientais', '60'),
        ('Computação Gráfica', '60'),
        ('Engenharia de Software', '60'),
        ('Introdução a Banco de Dados', '60'),
        ('Manutenção e Otimização de Banco de Dados', '60'),
        ('Metodologia Cientifica', '60'),
        ('Segurança de Dados', '60'),
        ('Arquitetura de Aplicativos Móveis', '60'),
        ('CRIPTOGRAFIA', '60'),
        ('Design de Interfaces para Dispositivos Móveis', '60'),
        ('Eletiva I', '60'),
        ('Gestão de Segurança da Informação', '60'),
        ('Integração de Aplicativos Móveis com APIs de Terceiros', '60'),
        ('Segurança e Privacidade de dados', '60'),
        ('Desenvolvimento de Serviços Web para Dispositivos Móveis', '60'),
        ('Eletiva II', '60'),
        ('Inovação em Negócios e Oportunidades', '60'),
        ('Novas Tecnologias Aplicadas a Comunicação', '60'),
        ('Programação Orientada a Objeto', '60'),
        ('SEGURANÇA EM APLICATIVOS MÓVEIS', '60'),
        ('Trabalho de Conclusão de Curso', '60'),
        ('__TOTAL__', '1620')
    ],
    "1620561": [
        ('Introdução ao EAD', '60'),
        ('Lógica de programação e algoritmo', '60'),
        ('Estrutura de Dados', '60'),
        ('Estatística', '60'),
        ('Arquitetura de computadores', '60'),
        ('Comunicação, cultura e sociedade', '60'),
        ('Políticas Sociais e Ambientais', '60'),
        ('Fundamentos de BIG DATA', '60'),
        ('Segurança de dados', '60'),
        ('Introdução ao Banco de Dados', '60'),
        ('Metodologia científica', '60'),
        ('Engenharia de Software', '60'),
        ('Manutenção e otimização de banco de dados', '60'),
        ('Design de interfaces para dispositivos móveis', '60'),
        ('Sistemas Operacionais Mobile', '60'),
        ('Criptografia', '60'),
        ('Desenvolvimento de jogos para dispositivos móveis', '60'),
        ('Segurança e privacidade de dados', '60'),
        ('Gestão de segurança da informação', '60'),
        ('Eletiva I', '60'),
        ('Desenvolvimento de aplicações Android', '60'),
        ('Desenvolvimento de Aplicações IOT', '60'),
        ('Desenvolvimento Mobile', '60'),
        ('Programação orientada a objetos', '60'),
        ('Segurança em aplicativos móveis', '60'),
        ('Eletiva II', '60'),
        ('Trabalho de Conclusão de curso', '60'),
        ('Novas tecnologias aplicadas à comunicação', '60'),
        ('Empreendedorismo, criatividade e inovação', '60'),
        ('Práticas de Gestão Corporativa', '60'),
        ('Libras – Língua Brasileira de Sinais', '60'),
        ('__TOTAL__', '1720')
    ],
    "1620488": [
        ('Acolhida', '45'),
        ('Projeto de Curso e Carreira', '16'),
        ('Projeto em Arquitetura de Computadores, Redes e Sistemas Operacionais I', '45'),
        ('Arquitetura de Computadores e Sistemas Operacionais', '90'),
        ('Fundamentos de Redes de Computadores', '90'),
        ('Projeto em Arquitetura de Computadores, Redes e Sistemas Operacionais II', '45'),
        ('Segurança da Informação', '90'),
        ('Redes de Computadores', '90'),
        ('Projeto em Gestão de Projetos e Programas de Segurança da Informação I', '45'),
        ('Início e Planejamento de Projetos', '90'),
        ('Cybersecurity Capstone', '90'),
        ('Projeto em Gestão de Projetos e Programas de Segurança da Informação II', '45'),
        ('Execução, Monitoramento, Controle e Encerramento de Projetos', '90'),
        ('Programa e Política de Segurança da Informação', '90'),
        ('Projeto em Segurança de Redes, Certificação Digital, Firewall e IDS I', '45'),
        ('Fundamentos da Administração de Sistemas Operacionais Open Source', '90'),
        ('Defesa Cibernética I', '90'),
        ('Projeto em Segurança de Redes, Certificação Digital, Firewall e IDS II', '45'),
        ('Administração de Sistemas Open Source: Avançado', '90'),
        ('Defesa Cibernética II', '90'),
        ('Projeto em Gestão de Riscos de Segurança da Informação com LGPD I', '45'),
        ('Gestão de Riscos de Segurança da Informação I', '90'),
        ('Privacidade, Proteção de Dados e Marcos Legais', '90'),
        ('Projeto em Gestão de Riscos de Segurança da Informação com LGPD II', '45'),
        ('Gestão de Riscos de Segurança da Informação II', '90'),
        ('Gestão de Serviços de TI para Segurança', '90'),
        ('Introdução a Libras', '27'),
        ('__TOTAL__', '2558')
    ],
    "1667554": [
        ('Algoritmos e Programação Estruturada', '40'),
        ('Business Architecture', '80'),
        ('Prática Extensionista', '60'),
        ('Arquitetura de Software', '80'),
        ('Relações Étnico-raciais e Responsabilidade Social', '40'),
        ('Engenharia de Software', '80'),
        ('Redes Convergentes, Sistemas Distribuídos e Virtualização', '80'),
        ('Leitura e Produção de Textos', '40'),
        ('Data Mining', '80'),
        ('Software Design and Architecture', '80'),
        ('Empreendedorismo', '40'),
        ('Cálculo', '80'),
        ('Cloud Computing', '80'),
        ('Desenvolvimento e Monitoramento de DashBoards', '40'),
        ('Design Thinking', '80'),
        ('Sistemas Operacionais', '80'),
        ('Computational Thinking', '80'),
        ('Prática Extensionista', '60'),
        ('Core Devops', '80'),
        ('Continuous Integration (CI) e Deployment (CD)', '40'),
        ('Segurança e Auditoria de Sistemas', '80'),
        ('Monitoramento e Gerenciamento Server', '80'),
        ('Administração Kubernetes, Rancher', '40'),
        ('Prática Extensionistas', '80'),
        ('Digital Management', '80'),
        ('Soft e Hard Skills', '40'),
        ('Metodologia Ágeis', '80'),
        ('Qualidade e Automação de Testes', '80'),
        ('Transformação Digital em Estratégias Organizacionais', '40'),
        ('Projeto de Software', '80'),
        ('Língua Brasileira de Sinais (optativa) e demais optativas', '40'),
        ('__TOTAL__', '2040')
    ],
    "1588016": [
        ('ALGORITMOS PARA DEV', '40'),
        ('DESENVOLVIMENTO EM JAVASCRIPT', '80'),
        ('LÓGICA COMPUTACIONAL', '80'),
        ('PROGRAMAÇÃO ESTRUTURADA PARA DEV', '40'),
        ('PROGRAMAÇÃO PARA INTERNET EM FRONT-END', '80'),
        ('SOCIEDADE BRASILEIRA E CIDADANIA', '80'),
        ('WEB DESIGN', '80'),
        ('ANÁLISE ORIENTADA A OBJETOS', '80'),
        ('BANCOS DE DADOS NÃO-CONVENCIONAIS', '80'),
        ('DESENVOLVIMENTO COM FRAMEWORK PHP', '80'),
        ('INTERFACE E USABILIDADE', '80'),
        ('MODELAGEM DE DADOS', '80'),
        ('PROGRAMAÇÃO E DESENVOLVIMENTO DE BANCO DE DADOS', '80'),
        ('PROGRAMAÇÃO PARA INTERNET EM BACK-END', '80'),
        ('ANÁLISE E DESENVOLVIMENTO DE SISTEMAS', '80'),
        ('DESENVOLVIMENTO COM FRAMEWORK ANGULAR', '80'),
        ('DESENVOLVIMENTO COM FRAMEWORK NODE.JS', '80'),
        ('DESENVOLVIMENTO COM FRAMEWORK REACT', '80'),
        ('DIREITO CIBERNÉTICO', '80'),
        ('OPTATIVA I', '80'),
        ('ENGENHARIA DE SOFTWARE', '80'),
        ('GERENCIAMENTO E QUALIDADE DE SOFTWARE', '80'),
        ('OPTATIVA II', '80'),
        ('PROCESSOS ÁGEIS PARA DESENVOLVIMENTO DE SOFTWARE', '80'),
        ('PROJETO DE SISTEMAS PARA INTERNET', '80'),
        ('REDES E SISTEMAS DISTRIBUÍDOS', '80'),
        ('ATIVIDADES COMPLEMENTARES', '100'),
        ('__TOTAL__', '2100')
    ],
    "1549921": [
        ('Experiência Criativa. Navegando em Segurança e Privacidade da Informação', '120'),
        ('Aspectos Legais de Segurança e Privacidade', '80'),
        ('Raciocínio Algorítmico', '120'),
        ('Fundamentos de Sistemas Ciberfísicos', '80'),
        ('Filosofia', '80'),
        ('Criptografia Aplicada', '80'),
        ('Normas e Padrões de Segurança', '80'),
        ('Programação Web', '80'),
        ('Conectividade em Sistemas Ciberfísicos', '80'),
        ('Arquitetura de Bancos de Dados', '120'),
        ('Programação Imperativa', '80'),
        ('Experiência Criativa: Implementando Sistemas com Criptografia', '120'),
        ('Segurança de Serviços e Servidores', '80'),
        ('Programação Orientada e Objetos', '120'),
        ('Performance em Sistemas Ciberfísicos', '80'),
        ('Clínica de TIC', '40'),
        ('Ética', '40'),
        ('Sistemas de Detecção e Prevenção de Intrusão', '80'),
        ('Segurança de Sistemas', '80'),
        ('Resolução de Problemas Estruturados em Computação', '80'),
        ('Redes Convergentes', '80'),
        ('Sistemas Operacionais Ciberfísicos', '80'),
        ('Ethical Hacking', '80'),
        ('Teologia e Sociedade', '40'),
        ('Experiência Criativa: Protegendo o Ambiente Computacional de Intrusões', '120'),
        ('Gestão de Segurança e Auditoria de Sistemas', '120'),
        ('Forense Computacional', '80'),
        ('Software Seguro', '80'),
        ('Cloud Computing', '80'),
        ('Cibersegurança para Sistemas Ciberfísicos', '80'),
        ('Análise de Malware e Engenharia Reversa', '80'),
        ('Privacidade da Informação', '80'),
        ('Aprendizagem de Máquina', '80'),
        ('Big Data Analytics', '80'),
        ('Gestão de Projetos e Métodos Ágeis', '120'),
        ('Experiência Criativa: Usando o mindset do adversário na Cibersegurança', '120'),
        ('Segurança e Privacidade para Ambiente Web', '120'),
        ('Resposta a Incidentes de Cibersegurança', '80'),
        ('DevSecOps', '120'),
        ('Segurança e Privacidade no Ciberespaço', '40'),
        ('Experiência Criativa: Criando Soluções com Cibersegurança by Design no Ciberespaço', '120'),
        ('Usabilidade e Fatores Humanos em Cibersegurança', '80'),
        ('Governança de Cibersegurança', '80'),
        ('Blockchain', '80'),
        ('Empreendedorismo e Inovação em TI', '40'),
        ('Data Hiding', '80'),
        ('__TOTAL__', '3200')
    ],
}


def from_file(arc="../data/ines.csv"):
    DIRNAME = Path("/home/carlo/Documentos/doc/academia/projetos/inep/projetos_pedagógicos/ppc_txt")

    def clean(field):
        return field.replace("DESENV_APP_MÓVEIS", "DESENVOLVIMENTO_MOBILE").replace("_COD_CURSO", "").replace(
            "REF_DESENVOLVIMENTO_", "").replace("FULL_", "DESENVOLVIMENTO_FULL").replace(
            "DESENV_APP_DISPOSITIVOS_MÓVEIS", "DESENVOLVIMENTO_MOBILE").replace(
            "SEGURANÇA_INFORMAÇÃO_", ""
        )

    def extract_course(file_name):
        fd = file_name.name
        fd = fd.split(".")[0]
        fd = fd.split("_")
        # fd = fd[2], fd[-1], "_".join(fd[4:-1])
        nome = clean("_".join(fd[4:-1]))
        tag_name = " ".join(nome.split("_")).lower()
        tagger = TAG_DICT[tag_name]
        name_tag = DICT_TAG[tagger]
        fld = fields(fd[2], "", fd[-1], nome, "GRAD", tagger, name_tag)
        return fld

    from csv import reader
    from collections import namedtuple
    field_names = "ifes instituto coid nome grau tagger tag_name"
    fields = namedtuple("fields", field_names)
    files = DIRNAME.glob("*.txt")
    f_list = list(files)
    docs = [extract_course(doc) for doc in f_list
            if doc.name.startswith("COD") and "PPC" in doc.name]
    # [print(d) for d in docs]
    docs = {o: fields(c, t, o, i, a, k, n)
                 for c, t, o, i, a, k, n in docs}
    # [print(d) for d in docs.values()]
    with open(arc, "r", encoding="utf-8") as filer:
        info = reader(filer)
        linfo = list(info)
        linfo = {o: fields(c, t, o, i, a, (ks := k.split(" - "))[0], ks[1])
                 for c, t, o, i, a, k, *_ in linfo}
        docs.update(linfo)
        [print(li) for li in docs.values()]
        return docs


def main():
    from csv import DictWriter
    dados = Path(__file__).parent.parent / "data" / 'horas.csv'
    base = Path(__file__).parent.parent / "data" / "inep.json"
    from tinydb import TinyDB, Query
    db = TinyDB(base)
    query = Query()
    rotula = {oid: db.search(query.coid == oid)[0].keys() for oid in h.keys()}
    print(rotula)
    campo = from_file()

    coid_, name_, rotulo_, hour_, nomeado_ = "curso_id", "nome_disciplina", "rotulo", "horas", "nomeado"
    items = [{k: val for k, val in
              zip([coid_, name_, rotulo_, hour_, nomeado_],
                  [coid, name, campo[coid].tagger + "-" + campo[coid].tag_name if coid in campo else "",
                   hour, campo[coid].tag_name])}
             for coid, names in h.items() for name, hour in names]
    # print(items[:100])

    with open(dados, 'w', newline='') as csvfile:
        dw = DictWriter(csvfile, items[0].keys(), delimiter=',')
        dw.writeheader()
        dw.writerows(items)
    # text = h['1671887']
    # text = [md.split("Cód.")[1] if "Cód." in md else '' for md in text.split('TOTAL EM HORAS') if md]
    # text = [[t for t in tx.split('\n') if "(" in t] for tx in text]
    # [print(t) for t in text]


if __name__ == '__main__':
    main()
    # hh = list(h.values())[0].split("\n")
    # hh = [(v[:-2], v[-2:]) for v in hh]
    # lin = list(hh.values())  # [0]  # .split("\n")
    # [print(f"{ln},") for ln in hh]
