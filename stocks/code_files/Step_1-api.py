import finnhub, json, time, webbrowser
import pandas as pd

finnhub_client = finnhub.Client(api_key="cv85fg9r01qqdqh3vk80cv85fg9r01qqdqh3vk8g")

def grab_info():
    data = finnhub_client.stock_symbols('US')
    with open("jsons_needed/info.json", "w") as f:
        json.dump(data, f, indent=4)
#grab_info()

with open("jsons_needed/info.json") as f:
    context = json.load(f)

info = []

with open("my_texts/range.txt") as f:
    my_range_1 = "".join(f.readlines(1))
    my_range_2 = "".join(f.readlines(2))


### Adding Wanted Stocks ###
for stock in range(int(my_range_1), int(my_range_2)):    
    name = context[stock]["displaySymbol"]
    data = finnhub_client.quote(name)
    metrics = finnhub_client.company_basic_financials(name, 'all')["metric"]
    
    try:
        if metrics["monthToDatePriceReturnDaily"] >= -10 and metrics["5DayPriceReturnDaily"] <= -2.5 and metrics["marketCapitalization"] >= 1_000 and 5 < data['c']:
            with open("jsons_needed/chart.json", "a") as f:
                json.dump({
                "Name": name,
                "Current Price" : data['c'],
                "Daily Low": data['l'],
                "Daily High": data['h'],
                "52 Week High": metrics["52WeekHigh"],
                "52 Week Low": metrics["52WeekLow"],
                "5 Day Price Return": metrics["5DayPriceReturnDaily"],
                "Month Price Return": metrics["monthToDatePriceReturnDaily"],
                "Market Cap (Billions)": metrics["marketCapitalization"] / 1000
            }, fp=f)
                f.write('\n')
                
    except KeyError:
        pass
    except TypeError:
        pass
    
    time.sleep(0.5)
    
with open("my_texts/range.txt", "w") as f:
    f.write(str(int(my_range_1) + 60) + '\n')
    f.write(str(int(my_range_2) + 60))

df = pd.read_json("jsons_needed/chart.json", lines=True)
    
if not df.empty:
    with open("my_texts/current_stock_list.txt", "w") as f:
        f.write(df.to_string())
    names_list = df['Name'].to_list()
else:
    print("This set was empty")



### Opening Tabs ###
time.sleep(5)

def open_tabs():
    for names in names_list:
        webbrowser.open(f"https://finance.yahoo.com/quote/{names}/chart?p={names}F&interval=1mo")
        time.sleep(1)
        try:
            if names == names_list[4]:
                break
        except IndexError:
            pass
#open_tabs()