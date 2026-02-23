⚠️ Work in Progress

# 📊 Binary Options Candle Pattern Analysis

## 📌 Project Overview
This project tests and analyzes a specific **candlestick pattern** designed for **binary options trading**.  

> ⚡ **Strategy designed by me**, originally implemented in **LUA**, the scripting language used for custom indicators in IQ Option.  

Historical market data for backtesting was **extracted using MetaTrader 5**. The Python backtesting script evaluates the pattern’s effectiveness, providing insights for data-driven trading decisions.

---

## 🔹 Strategy Logic
The pattern works as follows:

1. **Bullish Setup**:
   - Candle[i] closes **above the high of Candle[i-1]**.
   - The **body of Candle[i]** is larger than each of its wicks individually.
   - Enter a **long position on Candle[i+1]** if, within the first **30 seconds**, the price surpasses `open[i]`.
   - **Expiration** is set at the **close of Candle[i+1]**.

2. **Bearish Setup**:
   - Candle[i] closes **below the low of Candle[i-1]**.
   - The **body of Candle[i]** is larger than each of its wicks individually.
   - Enter a **short position on Candle[i+1]** if, within the first **30 seconds**, the price drops below `open[i]`.
   - **Expiration** is set at the **close of Candle[i+1]**.

> This logic is implemented in **LUA** for IQ Option, and reproduced in Python for backtesting.

---

## 🛠️ Tools & Technologies
- **LUA** – Original code for IQ Option indicators  
- **MetaTrader 5** – Extract historical market data (EUR/USD)  
- **Python** – Backtesting simulation
- **Tableau** - Visualization

> No additional Python libraries required.

---

## 📈 Key Metrics

| Metric | Value |
|--------|-------|
| **Pattern Tested** | Bullish/Bearish Pin Bar |
| **Total Trades Simulated** | 2,252 |
| **Wins** | 1,833 |
| **Losses** | 419 |
| **Win Rate** | 81.39% |

---

## 📊 Results Dashboard
![Candle Pattern Dashboard](results/tableau_dashboard.png)

This dashboard summarizes:  
- Pattern visualization  
- Simulation requirements  
- Total trades and success rate  

---

## 📂 Project Structure

```bash
binary-options-candle-pattern/
│
├── lua/
│   └── candle_pattern.lua         # Original LUA code for IQ Option
│
├── python/
│   └── backtest.py                # Script to simulate the pattern
│
├── data/
│   └── data_binary.csv        # Original historical data (from MetaTrader 5)
│
├── results/
│   └── tableau_dashboard.png      # Dashboard image summarizing results
│
└── README.md
