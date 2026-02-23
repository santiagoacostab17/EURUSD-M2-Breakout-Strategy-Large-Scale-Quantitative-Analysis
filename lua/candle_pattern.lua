instrument {
  name ="candle_pattern",
  icon='indicators:ADX',
  overlay = " true"
}
      color_resistance = "red"
      color_support = "green"
      Mid = close[1] - open[1]
      if open[1] > close[1] then Mid = open[1] - close[1] end
      Mecha_Top = high[1] - close[1]
      if open[1] > close[1] then Mecha_Top = high[1] - open[1] end
      Mecha_Bot = close[1] - low[1]
      if open[1] < close[1] then Mecha_Bot = open[1] - low[1] end
      if close[1] > open[1] and Mid > Mecha_Top and Mid > Mecha_Bot and close[1] > high[2] then support = open[1] end
      if close[1] < open[1] and Mid > Mecha_Top and Mid > Mecha_Bot and close[1] < low[2] then resistance = open[1] end
      hline(resistance, "Resistance", color_resistance, width)
      hline(support, "Support", color_support, width)
