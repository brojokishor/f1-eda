# F1 Data Analysis - Monza 2023
I've had an interest in Formula 1 for a long time, but only recently started following the sport closely.
What stood out to me wasn't just the racing, but how much of it comes down to data - lap times, tyre strategy, pit stops, and consistency.
This project is my attempt to explore that side of the sport using data from the 2023 Italian Grand Prix.

---

## What I wanted to find out
Instead of just plotting data, I started with a few specific questions:

- How do positions change lap by lap, and how much of it is influenced by pit stops?
- Does tyre compound choice (Medium vs Hard) meaningfully affect lap times at Monza?
- Can you actually see tyre degredation in the lap time data?
- Which teams were most consistent — and does that even matter?

---

## Key observation
One result that stood out was related to consistency.

Williams had the lowest variation in lap times among all teams, including high consistency, but still finished outside the points.

In contrast, Aston Martin showed much higher variation between drivers yet Alonso managed to finish P9.

This suggests that consistency alone is not a reiable indicator of race success. Race position, strategy, and overall pace have a larger impact.

---

## Observations from the data
While working with the dataset, a few issues and patterns required closer inspection.

- **Verstappen's pit stop laps are missing**. Laps 20 and 21 just don't exist in the cleaned dataset. FastF1 flagged them as inaccurate so they got filtered out during cleaning. I only figured out he pitted there by noticing the gap in lap numbers and the compound switching from Medium to Hard.
- **Tsunoda isn't in the data at all**. At first I thought it was a collection error. It wasn't — he had an engine failure on the formation lap and never started the race. Zero laps completed means zero rows in the dataset.
- **Hulkenberg looked like he was leading mid-race**. On the position plot he appears right at the top around laps 15-25. He wasn't actually faster than everyone — he just hadn't pitted yet. Once he did, he dropped to P17. This is called a "false leader" and it's easy to misread if you don't account for pit stop timing.
- **Only Medium and Hard compounds were present** — confirming that assumptions about tyre availability should always be validated against the data

These observations highlight the importance of validating data assumptions and understanding race context before drawing conclusions from visualizations.

---

## Visualizations

### Race Position Changes
![Position Changes](outputs/figures/position_changes.png)

### Tyre Compund vs Lap Time
![Compound Lap Times](outputs/figures/compound_laptimes.png)

### Lap Time Evolution
![Lap Time Evolution](outputs/figures/laptime_evolution.png)

### Team Consistency
![Team Consistency](outputs/figures/team_consistency.png)

---

## Tools used 
- Python 3.12
- FastF1 — pulls official F1 timing data directly
- Pandas, NumPy, Matplotlib, Seaborn
- JupyterLab

---

## How to run it?
<pre>bash
git clone https://github.com/brojokishor/f1-eda.git 
cd f1-eda 

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

jupyter lab 
</pre>

Run the notebooks in order — 01 first, then 02, then 03.

---

## Project Structure
```
f1-eda/
├── data/
│   ├── raw/               # original data, never modified
│   └── processed/         # cleaned version used for analysis
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_analysis_and_viz.ipynb
├── outputs/
│   └── figures/           # saved plots
├── src/
│   └── helpers.py
├── requirements.txt
└── README.md
```

---

## What I'd do differently
This is one race at one circuit. Monza is unusual — low downforce, high speed, minimal tyre degredation compared to most tracks. The findings here might not hold elsewhere. Next steps:
- Run the same analysis across multiple races and see what changes
- Bring in qualifying data to compare grid position vs actual race pace
- Go deeper into sector times instead of just full lap times
- Improve the visualizations — some of them are still harder to read than they should be

---

## Next steps

- Extend analysis to multiple races  
- Compare qualifying vs race performance  
- Improve visualizations  