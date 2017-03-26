from valuation_mod import Warren_Buffet
from technical_mod import Bill_Ackman
from auth import consumer_key, consumer_secret, access_token, access_token_secret, api_key 
import csv

ticker = raw_input("Enter the ticker you would like to search for: ")


# ticker_list = []
# file1 = open('tickers/nasdaqStocks.txt')
# file2 = open('ticker/otherStocks.txt')
# for line in file1.readlines()[1:] + file2.readlines()[1:]:
#     stock = line.strip().sp[]lit('|')[0]
#     if (re.match(r'^[A-Z]+$',stock)):
#         ticker_list += [stoc]

# file1.close()
# file2.close()

try:
	warren = Warren_Buffet(0.025, 0.09, ticker)
	warren.calc_wacc()
except ZeroDivisionError:
	print "Unable to calculate cost of debt for this stock"

bill = Bill_Ackman(api_key,ticker)
bill.run_all()

with open("Stocksheet.csv", "w") as sfile:
	writer = csv.writer(sfile)
	writer.writerow(["Ticker", ticker])
	writer.writerow([" "])

	for key, value in warren.SUMMARY_DATA.items():
		writer.writerow([key, value])
		writer.writerow([" "])

	for key, value in bill.SUMMARY_DATA.items():
		writer.writerow([key, value])
		writer.writerow([" "])