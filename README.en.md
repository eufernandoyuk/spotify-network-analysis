<p align="right">
  <a href="README.md">Português</a> | <b>English</b>
</p>

# 🎧 Spotify - Complex Network Analysis of the Most Streamed Global Artists

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Gephi](https://img.shields.io/badge/Gephi-Graph_Analysis-orange?style=for-the-badge)](https://gephi.org/)
[![UFABC](https://img.shields.io/badge/UFABC-Communication_and_Networks-green?style=for-the-badge)](https://www.ufabc.edu.br/)

> Empirical study on cultural connectivity, music diffusion, and global hub identification during the COVID-19 pandemic (May 2020) using **Graph Theory** and **Complex Network Analysis**.

---

## 📌 Project Overview

This project was developed within the **Communication and Networks** course at the **Federal University of ABC (UFABC)**, under the supervision of Prof. Alexandre Hiroaki Kihara.

The primary objective was to model and analyze global music consumption dynamics during the onset of quarantine restrictions (May 2020), identifying:
- International market penetration and cross-border reach of artists.
- Cultural clustering vs. isolation across countries (linguistic and geographic communities).
- The topological properties of the music graph and the emergence of global superstar *hubs*.

---

## 👨‍💻 My Role & Technical Contributions

As a core developer and data analyst on the team, my direct responsibilities included:

1. **Data Extraction, Wrangling & Modeling (Python & Pandas):**
   - Developed Python data pipelines to process raw Kaggle charts data (*Spotify Top Songs by Country Charts - May 2020*).
   - Extracted and mapped unique entities (760 artists across 62 countries, totaling 822 nodes).
   - Engineered data transformations to construct **adjacency matrices** (Bipartite Graph *Artists × Countries* and Projected Co-occurrence Graph *Artists × Artists*).
   - Exported structured network datasets (`.csv`) tailored for graph analysis environments.

2. **Topological & Network Analysis in Gephi:**
   - Modeled, parameterized, and visualized graph architectures using **Gephi**.
   - Computed, analyzed, and evaluated core network and centrality metrics:
     - **Degree Centrality:** Assessed direct market overlap and connection volume.
     - **Betweenness Centrality:** Identified boundary-spanning bridge nodes connecting distinct music clusters.
     - **Closeness Centrality:** Measured structural distance and accessibility across the graph.
     - **Eigenvector Centrality:** Quantified prestige and influence based on connections to other prominent nodes.
     - **Modularity & Community Detection:** Uncovered affinity clusters and cultural/linguistic sub-networks.
     - **Network Density:** Evaluated structural sparsity and overall cohesion.

3. **Discussion & Business/Industry Insights:**
   - Synthesized statistical findings (e.g., extreme sparsity, heavy-tailed distributions) into actionable insights.
   - Formulated strategic proposals for artist positioning, crossover collaborations, and global streaming growth.

---

## 🧠 Key Findings & Insights

| Metric / Aspect | Value / Observation | Impact & Interpretation |
|---|---|---|
| **Total Nodes** | 822 (760 Artists + 62 Countries) | Broad representation of global streaming charts. |
| **Network Density** | `0.074` (~7.4%) | Highly sparse network with strong reliance on a few cross-regional bridges. |
| **Global Presence (>1 country)** | Only **20%** of artists (152) | 80% of artists are strictly local/domestic. |
| **Hyper-Hubs (>50% of countries)** | Only **2%** of artists (13) | Extreme superstar concentration dominating global attention. |

### 🌟 Global Influence Highlights:
- **Top Hub Artists:** Lady Gaga (59 countries), The Weeknd (59 countries), Dua Lipa (53 countries), Tones and I (52 countries), Powfu (52 countries).
- **Regional Communities:** Clear linguistic cluster for Spanish-speaking markets (Latin America + Spain) alongside distinct peripheral/isolated markets (Japan, Hong Kong, Taiwan, Brazil, Turkey, Italy).

---

## 🛠️ Tech Stack & Tools

- **Programming Language:** Python 3.x
- **Data Libraries:** `pandas`, `numpy`
- **Graph Modeling & Visualization:** [Gephi](https://gephi.org/)
- **Data Source:** [Kaggle - Spotify Top Songs by Country May 2020](https://www.kaggle.com/datasets/hkapoor/spotify-top-so-ngs-by-country-may-2020)

---

## 📁 Repository Structure

```bash
├── data/
│   ├── raw/                 # Raw dataset from Kaggle
│   └── processed/           # Adjacency matrices generated for Gephi
├── scripts/
│   ├── build_bipartite.py   # Pipeline to generate Countries x Artists matrix
│   └── build_coocurrence.py # Pipeline to generate Artists x Artists projected network
├── visualizacoes/           # Exported graph visualizations and statistical charts
├── docs/                    # Full scientific paper and presentation slides
└── README.md                # Project documentation