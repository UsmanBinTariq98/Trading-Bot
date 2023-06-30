# Trading-Bot
This trading bot is using three strategies(EMA, ADX and Super-Trend)
# Written information of Code:
This trading bot is designed to execute trading orders based on a combination of three strategies: EMA (Exponential Moving Average), ADX (Average Directional Index), and Super Trend. 

The code utilizes various libraries including pandas, numpy, MetaTrader5, datetime, talib, and PySide6. These libraries provide functionalities for data manipulation, technical analysis, and interaction with a trading platform.

The `market_order` function is defined to execute a market order with specific parameters such as symbol, volume, order type (buy or sell), and EMA values. It retrieves the latest market prices and sets stop loss (sl) and take profit (tp) levels based on the EMA values and current market conditions. The function then sends an order request to the trading platform using the MetaTrader5 library.

In the main part of the code, the bot focuses on the EURUSD symbol and sets a volume of 1.0 for each trade. The timeframe is set to one minute (TIMEFRAME_M1), and the smaPeriod is set to 60.

The code initializes the MetaTrader5 platform and enters into an infinite loop for continuous trading. Within each loop iteration, it retrieves the latest market data for the specified symbol and timeframe. The data is then used to calculate the EMA values, ADX, and Super Trend using the talib library.

The bot checks the current positions held (mt.positions_total()) and proceeds with executing a trade only if the number of positions is less than or equal to 1. If the EMA20 is greater than EMA50, the ADX is above 18, and the Super Trend is positive, a market order to buy is executed. Similarly, if the EMA20 is less than EMA50, the ADX is above 18, and the Super Trend is negative, a market order to sell is executed. If none of these conditions are met, the bot prints "No trade" and continues to the next iteration.

Overall, this code combines EMA, ADX, and Super Trend strategies to generate trading signals and execute orders accordingly. It provides a basic framework for an automated trading bot, which can be further enhanced and customized based on specific trading preferences and requirements.
