# 🎧 Spotify - Análise de Redes Complexas dos Artistas Mais Ouvidos no Mundo

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Gephi](https://img.shields.io/badge/Gephi-Graph_Analysis-orange?style=for-the-badge)](https://gephi.org/)
[![UFABC](https://img.shields.io/badge/UFABC-Comunicação_e_Redes-green?style=for-the-badge)](https://www.ufabc.edu.br/)

> Estudo empírico sobre conectividade cultural, difusão musical e identificação de *hubs* globais durante a pandemia de COVID-19 (Maio/2020) utilizando **Teoria dos Grafos** e **Análise de Redes Complexas**.

---

## 📌 Visão Geral do Projeto

Este projeto foi desenvolvido no âmbito da disciplina **Comunicação e Redes** na **Universidade Federal do ABC (UFABC)**, sob orientação do Prof. Alexandre Hiroaki Kihara.

O objetivo principal foi modelar e compreender o fluxo de consumo musical em escala global no início do isolamento social (maio de 2020), identificando:
- O nível de penetração de artistas em diferentes mercados internacionais.
- O isolamento ou agrupamento cultural entre países (comunidades linguísticas/regionais).
- A estrutura topológica da rede musical e a presença de superestrelas (*hubs* globais).

---

## 👨‍💻 Minha Atuação & Contribuições Técnicas

Como membro-chave do time de desenvolvimento e análise, minhas responsabilidades diretas envolveram:

1. **Extração, Tratamento e Modelagem dos Dados (Python & Pandas):**
   - Criação dos scripts em Python para processamento do dataset bruto do Kaggle (*Spotify Top Songs by Country Charts - May 2020*).
   - Extração de entidades únicas (760 artistas e 62 países, totalizando 822 vértices).
   - Transformação e engenharia de dados para geração das **matrizes de adjacência** (Grafo Bipartido *Artistas × Países* e Grafo Projetado Ponderado *Artistas × Artistas*).
   - Exportação estruturada para formatos legíveis por softwares de análise de grafos (`.csv`).

2. **Análise Topológica no Gephi:**
   - Modelagem e parametrização dos grafos no software **Gephi**.
   - Execução e interpretação das principais métricas de centralidade e topologia:
     - **Centralidade de Grau (*Degree Centrality*):** Identificação do volume direto de conexões compartilhadas.
     - **Centralidade de Intermediação (*Betweenness Centrality*):** Mapeamento de nós que atuam como pontes entre comunidades.
     - **Centralidade de Proximidade (*Closeness Centrality*):** Avaliação da distância média entre nós.
     - **Centralidade de Autovetor (*Eigenvector Centrality*):** Medição da influência baseada na conexão com nós de alta relevância.
     - **Modularidade & Detecção de Comunidades:** Segmentação dos clusters de afinidade musical e regional.
     - **Densidade da Rede:** Mensuração da conectividade global da estrutura gerada.

3. **Discussão dos Resultados e Insights de Negócio/Indústria:**
   - Interpretação aprofundada dos fenômenos estatísticos encontrados (como a baixa densidade e distribuição de cauda longa).
   - Formulação de hipóteses e conclusões estratégicas para a indústria musical e artistas independentes.

---

## 🧠 Principais Resultados & Insights

| Métrica / Aspecto | Valor / Observação | Impacto & Interpretação |
|---|---|---|
| **Vértices Totais** | 822 (760 Artistas + 62 Países) | Mapeamento representativo dos charts globais. |
| **Densidade da Rede** | `0,074` (~7,4%) | Rede esparsa com grande dependência de poucas conexões cruzadas. |
| **Presença Global (>1 país)** | Apenas **20%** dos artistas (152) | 80% do consumo é estritamente local/nacional. |
| **Hiper-Hubs (>50% dos países)** | Apenas **2%** dos artistas (13) | Altíssima concentração de alcance no topo da indústria. |

### 🌟 Destaques de Influência Global:
- **Top Artistas:** Lady Gaga (59 países), The Weeknd (59 países), Dua Lipa (53 países), Tones and I (52 países), Powfu (52 países).
- **Clusters Regionais:** Formação nítida de uma forte comunidade de música em língua hispânica (América Latina + Espanha) e isolamento relativo de mercados orientais (Japão, Hong Kong, Taiwan) e pontuais (Brasil, Turquia, Itália).

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.x
- **Bibliotecas:** `pandas`, `numpy`
- **Visualização & Modelagem de Redes:** [Gephi](https://gephi.org/)
- **Fonte de Dados:** [Kaggle - Spotify Top Songs by Country May 2020](https://www.kaggle.com/datasets/hkapoor/spotify-top-so-ngs-by-country-may-2020)

---

## 📁 Estrutura do Repositório

```bash
├── data/
│   ├── raw/                 # Dataset bruto extraído do Kaggle
│   └── processed/           # Matrizes de adjacência geradas para o Gephi
├── scripts/
│   ├── build_bipartite.py   # Script de geração da matriz Países x Artistas
│   └── build_coocurrence.py # Script de projeção da rede Artistas x Artistas
├── visualizacoes/           # Grafos exportados e distribuições estatísticas
├── docs/                    # Artigo científico completo e slides da apresentação
└── README.md                # Documentação do projeto