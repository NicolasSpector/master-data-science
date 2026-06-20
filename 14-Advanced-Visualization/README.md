# 14. Advanced Visualization — 120 Years of Olympic History

## 📋 Project Overview

Comprehensive data visualization project analyzing 120 years of Olympic history (1896-2016). The analysis explores athlete demographics, gender participation evolution, medal distribution by country, and regional performance trends using interactive and static visualizations.

**Dataset:** [120 Years of Olympic History: Athletes and Results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) (Kaggle)  
**Records:** 271,116 athlete records | **Sports:** 42 disciplines | **Time Range:** 1896-2016

---

## 🎯 Research Questions

1. **Athlete Demographics** — How are athletes distributed by physical characteristics (height, weight, age) and gender?
2. **Gender Participation Evolution** — How has women's participation changed over time?
3. **Medal Dominance** — Which countries dominate Olympic medals across genders and sports?
4. **Performance Trends** — How have regional and national performances shifted across Olympic Games?

---

## 📊 Analysis & Visualizations

### Part 1: Athlete Demographics Distribution

**Height, Weight & Age Patterns**

<img width="1153" height="820" alt="image" src="https://github.com/user-attachments/assets/6d5384ad-828f-4095-9f6b-d0fd459c6a71" />

**Gender Composition Over Time**

<img width="1196" height="593" alt="image" src="https://github.com/user-attachments/assets/6e39e1ca-de95-4320-9f76-b7e41ee5e77d" />

**Key Insight:** Clear gender gap until 1980; exponential growth in female participation post-1980s, with near-parity by 2016.

---

### Part 2: Medal Analysis by Gender & Nationality

**Top Countries by Medal & Gender Count**

<img width="535" height="556" alt="image" src="https://github.com/user-attachments/assets/d9de4a7d-a458-4f4c-b0ad-f9f38985eb4c" />

<img width="536" height="555" alt="image" src="https://github.com/user-attachments/assets/bf730f4b-b0eb-413d-a280-318a6404cbdd" />

<img width="533" height="554" alt="image" src="https://github.com/user-attachments/assets/b67b4a6c-ba44-4057-a8cd-90d84c0205d4" />



**Key Insight:** USA, Russia, and Germany claim 40%+ of all medals; male athletes outnumber female medalists 3:1 despite recent equalization efforts.

---

### Part 3: Women's Participation Growth

**Women vs Men by Olympic Edition**

<img width="831" height="413" alt="image" src="https://github.com/user-attachments/assets/df42af77-e9ed-42ba-b54e-2831f622b5b9" />

**Key Insight:** Women's participation increased from <1% (1896) to ~45% (2016); some national delegations now send more women than men.

---

## 🛠️ Technologies & Techniques

**Data Processing**
- `pandas`, `numpy` — data wrangling and aggregation
- `groupby`, `pivot_table` — dimensional analysis

**Visualization Libraries**
- `matplotlib` — foundational charts (histograms, line plots, bar charts)
- `seaborn` — enhanced statistical visualization (distributions, heatmaps)
- `plotly` — interactive visualizations for exploration
- `folium` — geographic mapping of Olympic host cities

**Visualization Techniques**
- Time series analysis (line plots with annotations)
- Categorical comparisons (bar charts, grouped/stacked)
- Distribution analysis (histograms, KDE density)
- Multi-dimensional exploration (subplots, faceting)
- Interactive tooltips and drill-down capabilities

---

## 📁 Project Structure

```
14-Advanced-Visualization/
└── Spector_Nicolas_Esteban_-_Tarea_Final_Visualizacio_n_Avanzada.ipynb
└── README.md
```

---

## 💡 Lessons Learned

✅ **Color & Design Matter** — Effective use of color palettes improves readability and accessibility  
✅ **Context Enhances Data** — Annotations (vertical lines for historical events) make patterns meaningful  
✅ **Interactivity Drives Engagement** — Plotly's hover tooltips reveal details without cluttering plots  
✅ **Multi-View Analysis** — Comparing same data across different visualizations uncovers different insights  
✅ **Storytelling with Data** — Olympic history provides rich narrative context for analytical findings  

---

<p align="center">
  <a href="https://github.com/NicolasSpector">@NicolasSpector</a></i>
</p>
