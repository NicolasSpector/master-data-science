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
```
[Your histogram/density plot showing athlete physical characteristics]
Shows variation in height/weight across disciplines and age concentration (18-30 years)
```

**Gender Composition Over Time**
```
[Your line plot showing male vs female athlete participation 1896-2016]
Highlights the surge in women's participation from the 1950s onwards
```

**Key Insight:** Clear gender gap until 1956; exponential growth in female participation post-1960s, with near-parity by 2016.

---

### Part 2: Medal Analysis by Gender & Nationality

**Top Countries by Medal Count**
```
[Your horizontal bar chart: USA, Russia, Germany by medal type and gender]
Shows USA dominance across all categories, but gender gap persists
```

**Gender Breakdown in Medals**
```
[Your stacked bar or grouped visualization comparing male vs female medalists]
Displays the historical male advantage in medal counts across top nations
```

**Key Insight:** USA, Russia, and Germany claim 40%+ of all medals; male athletes outnumber female medalists 3:1 despite recent equalization efforts.

---

### Part 3: Women's Participation Growth

**Female Athlete Participation Trend**
```
[Your line plot showing growth trajectory of female athletes per Olympic Games]
Marks turning points (1956, 1980, 2000, 2016)
```

**Women vs Men by Olympic Edition**
```
[Your comparison chart showing female representation percentage evolution]
Shows acceleration in female participation, especially post-1990
```

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
- `folium` (optional) — geographic mapping of Olympic host cities

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
```

The notebook contains:
- Full exploratory data analysis with 15+ visualizations
- Step-by-step visualization design reasoning
- Interactive plots for demographic and medal analysis
- Comparative analysis across Olympic editions
- All cell outputs preserved for transparency

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
