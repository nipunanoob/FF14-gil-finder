import requests
import json

def main():
    dcName = "spriggan"
    r = requests.get(f'https://universalis.app/api/v2/extra/stats/most-recently-updated?&dcName={dcName}')
    print(r.status_code)
    with open('items.json', 'w') as file:
        json.dump(r.json(), file)

main()