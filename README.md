# 📊 EURUSD M2 Breakout Pullback Strategy

## 📌 Project Overview

This project tests a structural breakout strategy on EURUSD using:

- M2 candles for pattern detection
- M1 candles for execution timing
- Multi-million row dataset
- Fully vectorized backtesting (no loops)

The goal is to evaluate whether a strong breakout followed by a pullback generates a statistical edge in short-term binary-style execution.

> **Data Source:** The raw M1 EURUSD data (2015–2021) was obtained from [Kaggle – Forex EURUSD 1m Data](https://www.kaggle.com/datasets/ankitjha420/forex-eurusd-1m-data-2015-to-2021).  
> Annual CSVs were downloaded individually, merged, cleaned, and chronologically sorted manually to ensure data integrity.

---

# 🧠 Strategy Logic

## 📈 Bullish Setup

A bullish pattern is detected when:

1. M2[i] closes above the high of M2[i-1]
2. The candle body is larger than both upper and lower wicks

If this happens:

- During the first minute of M2[i+1]
- If price breaks above the open of M2[i]
- Enter LONG
- Expiration: close of M2[i+1]

---

## 📉 Bearish Setup

Mirror logic:

1. M2[i] closes below the low of M2[i-1]
2. The candle body is larger than both wicks

If this happens:

- During the first minute of M2[i+1]
- If price breaks below the open of M2[i]
- Enter SHORT
- Expiration: close of M2[i+1]

---

# 🖼 Pattern Visualization

These diagrams represent the structural conditions tested in the backtest.

### Bullish Scenario
![Bullish Scenario](results/bullish_scenario.png)

### Bearish Scenario
![Bearish Scenario](results/bearish_scenario.png)

---

# ⚙️ Data

| Metric | Value |
|--------|-------|
| Instrument | EURUSD |
| Total M1 Candles | 3,165,120 |
| Total M2 Candles | 1,582,560 |
| Backtest Type | Vectorized |
| Lookahead Bias | Removed |
| Execution | First minute of next M2 |
| Data Source | Kaggle (2015–2021) |
| Cleaning & Merging | Performed manually to ensure continuity |

---

# 📈 Results

| Metric | Value |
|--------|-------|
| Total Patterns Detected | 433,334 |
| Total Trades Executed | 51,980 |
| Wins | 24,330 |
| Losses | 27,650 |
| Win Rate | 46.81% |

---

# 📉 Statistical Expectation

Assuming 85% payout (typical binary structure):

Break-even winrate ≈ 54%

Strategy winrate = **46.81%**

Expected value per trade:

E = (0.4681 × 0.85) − (0.5319 × 1)  
E ≈ −0.134R per trade

Conclusion:

The raw strategy is statistically negative under standard payout conditions.

---

# 🔎 Interpretation

Although the setup looks structurally strong:

- Breakouts often exhaust short-term momentum
- Pullbacks may represent absorption rather than continuation
- Ultra-short timeframes are noise-dominated

The hypothesis of immediate continuation after structural breakout is not supported by large-scale testing.

---

# 🎯 Key Takeaways

✔ Large dataset validation (3M+ candles)  
✔ 50k+ trades → statistically meaningful  
✔ Clean vectorized implementation  
✔ No overfitting  
✔ Hypothesis rigorously tested  

The absence of edge is itself a valuable quantitative finding.

---

# 🚀 Next Steps

Possible segmentation improvements:

- Winrate by session (Asia / London / NY)
- Winrate by volatility regime
- Winrate by breakout size percentile
- Trend filter (higher timeframe bias)
- Range compression before breakout

The framework is built to easily test these extensions.

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Vectorized backtesting logic
- Jupyter / VSCode compatible

---

# 📌 Author Notes

This project demonstrates:

- Statistical thinking
- Bias removal awareness
- Large-scale data handling
- Strategy falsification discipline

In quantitative research, rejecting a hypothesis after robust testing is progress.
