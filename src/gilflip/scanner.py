import requests

# call saddlebag api to get list of items that are potentially good itemflips

def find_flippable_item(payload):

    payload["filters"] = [7]
    headers = {
        "Content-Type": "application/json"
    }

    res = requests.post('https://docs.saddlebagexchange.com/api/scan', json=payload, headers=headers)
    data = res.json()
    #sort items by roi descending and limit to just 10 entries (filtered out fake profit)

    scored = []
    for item in data["data"]:
        if item["home_server_price"] == 0:
            continue
        item["score"] = compute_score(item)
        scored.append(item)

    sorted_data = sorted(scored, key=lambda x:x["score"], reverse=True)[:10]
    return(sorted_data)

def compute_score(item):
    roi = item.get("ROI", 0)
    profit = item.get("profit_amount",0)
    sales_rate = item.get("sales_rate", 0.0)
    return roi * 0.4 + profit * 0.0001 + sales_rate * 0.4

