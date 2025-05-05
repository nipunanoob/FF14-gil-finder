from tabulate import tabulate

def display_table(data):
    table_data = []
    for item in data:
        table_data.append([
            item["real_name"],
            item["ROI"],
            item["profit_amount"],
            item["home_server_price"],
            item["ppu"],
            item.get("sale_rates", "N/A"),
            item["server"]
        ])
    table_headers = ["Name", "ROI%", "Profit", "Server Price", "Buy Price", "Sale rate", "Selling Server"]
    print(tabulate(table_data,table_headers, tablefmt="fancygrid")) 
