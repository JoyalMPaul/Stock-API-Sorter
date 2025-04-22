# 📈 Stock Sorter

## Project Description

A stock sorter was created using the Finnhub API, with the built-in webbrowser library utilized to display graphs for evaluating stock potential. A Pandas DataFrame was employed to generate an XLSX table, which can be imported as a CSV into Google Sheets. Additionally, histograms of profits and losses were created using the Matplotlib statistics library.

***    

## GUI Design

![image](https://github.com/user-attachments/assets/64b0abee-f3e1-4b08-888d-e7563b69b555)


## How to Use

1. ***You must already have a Finnhub account and have an api key. If not, use: https://finnhub.io/register
2. Open your preferred code editor and navigate down using `cd Stock API Sorter\stocks` to enter directory
3. Activate the virtual environment by running: `venv/scripts/activate` (If not working, use: `Unblock-File -Path ".\venv\Scripts\Activate.ps1"`)
5. Install the required libraries by running: `pip install -r requirements.txt`
6. Go into branch that contains code files using `cd code_files`
7. Download "https://marketplace.visualstudio.com/items/?itemName=GrapeCity.gc-excelviewer" extension to see XLSX as CSV file
8. Run Steps  
   - Step 1: `py .\Step_1-api.py` (Gets stock data)  
   - Step 2: `py .\Step_2-spreadsheets.py` (Puts data into chart)  
   - Step 3: `py .\Step_3-stocks.xlsx` (Makes xlsx file, **look at point 5 to view file**)  
   - Step 4: `py .\Step_4-data_chart.py` (Makes histogram of profits/loss)

## Libraries Used

Finnhub, Pandas, Openpyxl, Numpy, Matplotlib, Yfinance

## Extra

If needed, go into range.txt under my_texts folder. The top number is the minimum and the bottom number is the maximum for the companies sorted through so far. I recommend keeping the values at most 60 apart or else the api call limit for Finhubb free tier will be reached, and a error code will be returned. 
