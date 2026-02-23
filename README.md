⚠️ Work in Progress

# 📊 Binary Options Candle Pattern Analysis

## 📌 Project Overview
This project tests and analyzes a specific **candlestick pattern** designed for **binary options trading**.  

> ⚡ **Strategy designed by me**, originally implemented in **LUA**, the scripting language used for custom indicators in IQ Option.  

The goal is to **evaluate the effectiveness of the pattern** using historical market data and a **Python backtesting script**, providing insights for data-driven trading decisions.

---

## 🔹 Pattern Explanation
The pattern focuses on **Bullish and Bearish Pin Bars**:  

- **Bullish Pin Bar**: Indicates a potential upward reversal. Typically forms after a downtrend with a long lower wick and small body.  
- **Bearish Pin Bar**: Indicates a potential downward reversal. Typically forms after an uptrend with a long upper wick and small body.  

> This logic is implemented in **LUA** for IQ Option, and the Python script reproduces it for backtesting.

---

## 🛠️ Tools & Technologies
- **LUA** – Original code for IQ Option indicators  
- **Python** – Backtesting simulation  

> No additional libraries required.

---

## 📈 Key Metrics

| Metric | Value |
|--------|-------|
| **Pattern Tested** | Bullish/Bearish Pin Bar |
| **Total Trades Simulated** | 500 |
| **Win Rate** | 0–100% (to be determined) |
| **Average Payout per Trade** | TBD |

---

## 📊 Results Dashboard
![Candle Pattern Dashboard](results/dashboard_example.png)

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
│   └── raw/                       # Original historical data CSVs
│
├── results/
│   └── dashboard_example.png      # Dashboard image summarizing results
│
└── README.md
