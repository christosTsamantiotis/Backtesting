This program is consisted of the very early stages in the making of a Bitcoin trading bot. It's main function is gathering historical data and backtesting it. The code is split into to files.

The first file tapeGather.py is responsible for connecting to the Bitfinex API and downloading the relevant data we need and saving it into a .csv file. The start variable is the UNIX epoch our data gathering starts.
The file function reads the existing file with our data if there exists one. Then it writes the data in the correct format inside the file.

The second file Trade.py carries out the actual backtesting of the data. It scans for large transactions in the Time and Sales(old school called the tape) data and it checks how it affects the price movement in a specified time limit.
It also tracks how many large transactions happened in that time period and and their total volume in an attempt to discover how much money is really neede to move the market. It tracks the sum of the  buys and sells in order to determine the overall bulls vs bears strength.

More of a proof of concept, for now.