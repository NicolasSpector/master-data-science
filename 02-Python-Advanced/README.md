# 02. Python Advanced — IT Infrastructure Hostname Generator

## 📋 Overview

A realistic IT infrastructure dataset generator that procedurally creates **1,500 synthetic server hostnames** using weighted probability distributions. Each hostname encodes metadata about the server's OS, deployment environment, and geographic location — following patterns observed in real-world data centers.

The generated data is explored through statistical analysis and interactive visualizations (Matplotlib & Seaborn).

---

## 🎯 What This Project Demonstrates

✅ **Weighted Random Sampling** — modeling real-world probability distributions  
✅ **Modular Functions** — reusable code for string parsing and data encoding  
✅ **DataFrame Construction** — building structured data from scratch  
✅ **Data Persistence** — CSV export/import workflows  
✅ **Statistical Visualization** — grouped bar charts & multi-dimensional analysis  

---

## 🧠 Hostname Structure

Each hostname encodes 4 metadata fields using a **pattern-based format**:

```
[OS][ENV][COUNTRY][NODE_NUMBER]
Example: LPIRL055 → Linux · Production · Ireland · Node 55
```

| Field | Distribution |
|---|---|
| **OS** | Linux (40%) · Solaris (30%) · AIX (20%) · HP-UX (10%) |
| **Environment** | Production (30%) · Staging (25%) · Testing (25%) · Integration (10%) · Dev (10%) |
| **Country** | Ireland (30%) · Germany (23%) · Spain (16%) · Italy (16%) · France (9%) · Norway (6%) |
| **Node ID** | Auto-assigned & zero-padded (001, 002, ..., 500) |

---

## 📊 Dataset Output

**1,500 rows × 5 columns:**

| Column | Example | Type |
|---|---|---|
| `hostname` | `SSITA001` | string |
| `os` | `Solaris` | categorical |
| `environment` | `Staging` | categorical |
| `country` | `Italy` | categorical |
| `node` | `001` | numeric |

---

## 📈 Sample Visuals

<img width="661" height="604" alt="2026-06-18_19-58-44" src="https://github.com/user-attachments/assets/8b960bea-9ecd-4848-bb22-4dda1de52e21" />

<img width="1003" height="823" alt="image" src="https://github.com/user-attachments/assets/5e4e5c0f-e6bc-44be-aed9-d24ec356699d" />


---

## 📁 Repository Structure

```
02-Python-Advanced/
├── Python_Advanced.ipynb   # Full solution with explanations
├── hosts.csv               # Generated dataset (1,500 rows)
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/NicolasSpector/master-data-science.git
cd master-data-science/02-Python-Advanced

# Install dependencies
pip install pandas matplotlib seaborn jupyter

# Open notebook
jupyter notebook Python_Advanced.ipynb
```

The notebook is **fully executable** — run all cells to generate the dataset and visualizations.

---

## 💡 Technical Highlights

**Weighted Random Selection:**
```python
# Selecting OS with realistic probability distribution
os = random.choices(['Linux', 'Solaris', 'AIX', 'HP-UX'], 
                     weights=[40, 30, 20, 10])[0]
```

**Modular Design:**
- Separate functions for OS, environment, country, and node ID generation
- Reusable functions for hostname construction and DataFrame building
- Clean separation between data generation, transformation, and visualization

**Data Pipeline:**
- Generate → Structure → Persist (CSV) → Load → Analyze → Visualize

---

<p align="center">
  <a href="https://github.com/NicolasSpector">@NicolasSpector</a></i>
</p>
