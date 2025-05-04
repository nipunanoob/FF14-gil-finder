import requests

# call saddlebag api to get list of items that are potentially good itemflips

def find_flippable_item(payload):

    payload["filters"] = [7]
    headers = {
        "Content-Type": "application/json"
    }

    res = requests.post('https://docs.saddlebagexchange.com/api/scan', json=payload, headers=headers)
    print(res.status_code)
    data = res.json()
    print(data)
    #sort items by roi descending and limit to just 10 entries (filtered out fake profit)
    filtered = [item for item in data["data"] if item["home_server_price"] != 0]
    sorted_data = sorted(filtered, key=lambda x:x['ROI'], reverse=True)[:10]

    return(sorted_data)


