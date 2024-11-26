# **EURUSD_M30_v01**
**Automated Trading Strategy for EUR/USD on M30 Timeframe**

This repository contains an MQL4 script for MetaTrader 4 (MT4), designed for automated trading on the EUR/USD currency pair. The strategy leverages technical indicators and predefined conditions to execute buy and sell orders during specified trading hours.

---

## **Features**
- **Automated Trading Logic**:
  - Executes buy and sell orders based on market conditions and technical indicators.
  - Restricts trading to specific hours (1:29 AM to 11:59 PM) for controlled execution.
  - Includes fine-tuned conditions for trend and momentum-based trading.
  
- **Integrated Technical Indicators**:
  - **ATR (Average True Range):** Measures market volatility.
  - **ADX (Average Directional Index):** Identifies trend strength and direction.
  - **Bollinger Bands:** Detects price deviations for buy/sell triggers.
  - **Envelopes:** Establishes dynamic support and resistance levels.
  - **RSI (Relative Strength Index):** Evaluates price momentum and overbought/oversold conditions.
  - **SAR (Stop and Reverse):** Confirms trend direction.
  - **WPR (Williams' Percent Range):** Gauges market momentum.

- **Risk Management**:
  - Configurable **stop-loss** and **take-profit** levels.
  - Adaptive lot size calculation based on account equity.

---

## **Trading Rules**
### **Buy Conditions**
1. Market volatility (ATR) is within specified thresholds.
2. Bollinger Band lower boundary or Envelopes indicate a price rebound.
3. RSI exceeds 50, and WPR indicates upward momentum (>80).
4. Price is above the moving average (trend filter).

### **Sell Conditions**
1. Market volatility (ATR) matches sell-specific thresholds.
2. Bollinger Band upper boundary or Envelopes signal a reversal.
3. RSI is between 52 and 55, with WPR below 25 indicating downward momentum.
4. Price is below critical resistance levels or within reversal conditions.

### **Trading Hours**
- Allowed between **1:29 AM** and **11:59 PM** server time.
- Executes trades only at the start of specific minutes (e.g., 1st minute of an hour or 30th minute).

---

## **Usage Instructions**
### **1. Setup**
- Copy `EURUSD_M30_v01` to the `MQL4/Experts` folder in your MetaTrader 4 directory.
- Ensure all necessary indicators (ATR, ADX, Bollinger Bands, etc.) are available in the platform.

### **2. Compile the Script**
- Open MetaEditor and compile the script to ensure no errors.

### **3. Attach the Script**
- Apply the script to the EUR/USD chart with the **M30 timeframe** in MetaTrader.

---

## **Parameters**
- **Lot Sizes**:
  - `lot_buy_01`, `lot_sell_01`, `lot_buy_02`, `lot_sell_02`: Configurable for trade sizing.
- **Stop-Loss and Take-Profit**:
  - `stoploss`: 0.01 (1%)
  - `takeprofit`: 0.011 (1.1%)
- **Indicator Settings**:
  - `DXPeriod`, `ADX`, and other settings optimized for EUR/USD.

---

## **Backtest Results**

The following backtest results demonstrate the performance of the SPY_call_option_M30_v5 strategy under simulated conditions.
  ![Backtest Summary](results/Strategy_Tester_EURUSD.pdf)

---

## **Risk Disclaimer**
Trading involves significant risk. This script is intended for **demo account use only** to evaluate strategy performance. Do not use it for live trading without proper testing and risk assessment.

---

## **Future Improvements**
- Addition of advanced filtering mechanisms for reducing false signals.
- Support for multiple timeframes and additional trading pairs.
- Enhanced visualization of indicator conditions on the chart.

---

Let me know if you need further assistance with setting up this repository or any edits to the README! 🚀
