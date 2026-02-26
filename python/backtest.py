import pandas as pd

print("\n===== START BACKTEST =====\n")

# -----------------------------
# 1️⃣ Read CSV (M1 data)
# -----------------------------
print("Loading M1 data...")

df = pd.read_csv("EURUSD_1m_completo.csv")

df['datetime'] = pd.to_datetime(
    df['datetime'],
    format="%d.%m.%Y %H:%M:%S.%f"
)

df = df.sort_values('datetime').reset_index(drop=True)

for col in ["open", "high", "low", "close"]:
    df[col] = df[col].astype(float)

print("M1 data loaded")
print("Total M1 candles:", len(df))

# -----------------------------
# 2️⃣ Build 2-minute candles (M2)
# -----------------------------
print("\nBuilding M2 candles...")

df['group_2m'] = df.index // 2

df_2m = df.groupby('group_2m').agg({
    'datetime': 'first',
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last'
}).reset_index(drop=True)

print("M2 candles created")
print("Total M2 candles:", len(df_2m))

# -----------------------------
# 3️⃣ Calculate body and wicks
# -----------------------------
print("\nCalculating candle structure...")

df_2m['top_wick'] = df_2m['high'] - df_2m[['close','open']].max(axis=1)
df_2m['bot_wick'] = df_2m[['close','open']].min(axis=1) - df_2m['low']
df_2m['body'] = (df_2m['close'] - df_2m['open']).abs()

print("Structure calculated")

# -----------------------------
# 4️⃣ Detect pattern
# -----------------------------
print("\nDetecting patterns...")

df_2m['bull_pattern'] = (
    (df_2m['close'] > df_2m['open']) &
    (df_2m['top_wick'] < df_2m['body']) &
    (df_2m['bot_wick'] < df_2m['body']) &
    (df_2m['close'] > df_2m['high'].shift(1))
)

df_2m['bear_pattern'] = (
    (df_2m['close'] < df_2m['open']) &
    (df_2m['top_wick'] < df_2m['body']) &
    (df_2m['bot_wick'] < df_2m['body']) &
    (df_2m['close'] < df_2m['low'].shift(1))
)

df_2m = df_2m.dropna().reset_index(drop=True)

bull_count = df_2m['bull_pattern'].sum()
bear_count = df_2m['bear_pattern'].sum()

print("Patterns detected")
print("Total bull patterns:", bull_count)
print("Total bear patterns:", bear_count)
print("Total patterns:", bull_count + bear_count)

# -----------------------------
# 5️⃣ Simulate trades
# -----------------------------
print("\nSimulating trades...")

wins = 0
losses = 0
total_trades = 0

for i in range(1, len(df_2m) - 1):

    entry_m1_index = (i + 1) * 2

    if entry_m1_index >= len(df):
        continue

    first_minute_next_2m = df.iloc[entry_m1_index]

    entry_price = df_2m.loc[i, 'open']
    next_2m_close = df_2m.loc[i + 1, 'close']

    if df_2m.loc[i, 'bull_pattern']:

        if first_minute_next_2m['low'] < entry_price:

            total_trades += 1

            if next_2m_close >= entry_price:
                wins += 1
            else:
                losses += 1

    elif df_2m.loc[i, 'bear_pattern']:

        if first_minute_next_2m['high'] > entry_price:

            total_trades += 1

            if next_2m_close <= entry_price:
                wins += 1
            else:
                losses += 1

print("Trade simulation completed")

# -----------------------------
# 6️⃣ Results
# -----------------------------
winrate = wins / total_trades if total_trades > 0 else 0

print("\n------ RESULTS ------")
print("Wins:", wins)
print("Losses:", losses)
print("Total trades:", total_trades)
print("Winrate:", round(winrate * 100, 2), "%")

print("\n===== END BACKTEST =====\n")
