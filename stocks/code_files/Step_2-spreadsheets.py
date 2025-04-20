import openpyxl, ast

stock_data = []

### Gets information from the stock list and puts in into a stocks.xlsx document
with open("jsons_needed/chart.json") as f:
    for lines in f:
        actual_dict = ast.literal_eval(lines)
        stock_data.append(actual_dict)
        

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Stock Data"

headers = ['Symbol', 'Price Bought', 'Price Now', 'Percent Gain']
sheet.append(headers)

for stock in stock_data:
    sheet.append([stock['Name'], stock['Current Price']])

workbook.save('stocks.xlsx')

print("Data written to stocks.xlsx successfully!")