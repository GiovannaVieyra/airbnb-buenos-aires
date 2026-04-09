# 🏠 Airbnb Buenos Aires — End-to-End Market Analysis

A full-cycle data analysis project examining the short-term rental market in Buenos Aires, Argentina. Built as the final capstone for the Data Analyst program at Digital House.

---

## 🎯 Business Questions

1. What are the most profitable characteristics of Airbnb properties?
2. Which property types and locations offer the best investment opportunities?
3. What is the relationship between pricing and guest reviews?
4. What data-driven investment recommendations can be made from this dataset?

---

## 📊 Dataset

| File | Records | Description |
|------|---------|-------------|
| `listings.csv` | 23,729 properties | Property details, host info, room type, location |
| `calendar.csv` | 8,661,286 rows | Daily availability and pricing |
| `reviews.csv` | 387,099 reviews | Guest reviews from 2010 to 2020 |

---

## 🛠️ Tech Stack

| Tool | Usage |
|------|-------|
| **Python** (Pandas, NumPy, Plotly, Matplotlib, Seaborn) | EDA, data cleaning, ETL, visualizations |
| **MySQL + SQLAlchemy** | Database design, data loading, analytical queries |
| **Power BI** | Interactive dashboard with filters and KPIs |
| **GeoJSON** | Choropleth map of Buenos Aires neighborhoods |

---

## 🔄 Project Structure

```
airbnb-buenos-aires/
│
├── notebooks/          # Python notebooks: EDA, ETL, visualizations
├── MySQL/              # SQL scripts: schema, validation, analytical queries
├── geo/                # GeoJSON files for neighborhood mapping
├── docs/               # Full analysis reports (Stage 1, 2 & 3)
└── README.md
```

---

## 📋 Analysis Stages

### Stage 1 — Exploratory Data Analysis (EDA)
- Loaded and inspected all three datasets using `.info()`, `.describe()`, `.isnull()`
- Identified and handled outliers (prices up to $600,000/night distorting distributions)
- Key finding: 99% of properties are priced under $1,000/night, with a median of ~$700
- Correlation matrix revealed price has **no strong correlation** with any numeric variable — pricing is driven by qualitative factors (location, amenities, host quality)

### Stage 2 — Data Cleaning & ETL
- Standardized price columns (stripped `$` symbols, converted to `float64`)
- Converted date columns to `datetime64` using `pd.to_datetime(errors='coerce')`
- Filled missing `reviews_per_month` with `0` (properties with no review history)
- Created new features: estimated monthly income (`price × 30`), price category segments (low / medium / high using quantiles)
- Exported clean datasets to MySQL via Python + SQLAlchemy + ODBC driver with `fast_executemany` for optimized batch loading
- Validated referential integrity across all three tables: **0 orphaned records**

### Stage 3 — SQL Analytics & Dashboard
Analytical queries answered:

**Occupancy trends:**
- Peak occupancy: Jan–Apr and Nov–Dec (~51–53%)
- Low season: Jun–Jul (~25–27%)

**Pricing trends:**
- Highest average price: January at $4,540/night
- Lowest average price: May–June at ~$3,190/night

**Neighborhood investment analysis:**
- Highest demand: Palermo (148,694 reviews), Recoleta (66,698 reviews)
- Best price-demand balance: Palermo ($3,560 avg) and Recoleta ($3,470 avg)
- High-price, low-demand outliers: Puerto Madero ($5,991 avg, only 3,416 reviews)

**Top investment opportunities** (occupancy >60% AND avg price >$1,500):

| Neighborhood | Property Type | Avg Occupancy | Avg Price/night |
|---|---|---|---|
| Belgrano | Hotel Room | 75.3% | $2,177 |
| Parque Chas | Entire Home/Apt | 73.1% | $2,511 |
| La Paternal | Entire Home/Apt | 67.2% | $1,651 |
| Monte Castro | Entire Home/Apt | 64.7% | $7,759 |
| Agronomía | Entire Home/Apt | 62.7% | $2,388 |

---

## 📈 Power BI Dashboard

The final dashboard includes:
- **Choropleth map** — review density by neighborhood (log scale)
- **Time series** — monthly review evolution from 2010 to 2020
- **Seasonality chart** — demand patterns by month of year
- **Interactive filters** — by neighborhood, property type, and date range

> *Dashboard built in Power BI Desktop using data loaded from MySQL*

---

## 💡 Key Findings

- The Buenos Aires Airbnb market is dominated by **mid-to-high priced properties** (IQR: $600–$900/night)
- **Budget properties generate revenue through volume**; premium properties generate revenue through per-night rate
- **Price is not predicted by number of reviews** — they serve different market segments
- High occupancy ≠ high income; high price ≠ high demand. The best ROI comes from neighborhoods that achieve both
- Seasonal strategy: optimize pricing upward in Jan–Apr and Nov–Dec; focus on occupancy during low season (Jun–Jul)

---

## 👩‍💻 About

Built by **Giovanna Vieyra** — Data Analyst with experience in real estate operations, business intelligence, and automation.

[LinkedIn](https://www.linkedin.com/in/giovanna-vieyra-57b0a51b4/) · [GitHub](https://github.com/GiovannaVieyra)
