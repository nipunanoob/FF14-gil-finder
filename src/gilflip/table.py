from tabulate import tabulate

def display_table(data):
    table_data = []
    for item in data:
        table_data.append([
            item["real_name"],
            item["ROI"],
            item["profit_amount"],
            item["profit_raw_percent"],
            item["home_server_price"],
            item["ppu"],
            item.get("sale_rates", "N/A"),
            item["score"],
            item["server"]
        ])
    table_headers = ["Name", "ROI%", "Profit", "Profit%", "Home Server Price", "Buy Price", "Sale rate", "Item Score", "Selling Server"]
    print(tabulate(table_data,table_headers, tablefmt="fancygrid")) 
