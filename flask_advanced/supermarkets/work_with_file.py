import json


def load_market_data():
    with open('supermarkets/list_markets.json', 'r') as f:
        result = json.load(f)
    return result


def save_market_data(new_data):
    with open('supermarkets/list_markets.json', 'r') as f:
        result = json.load(f)

    result.append(new_data)

    with open('supermarkets/list_markets.json', 'w') as f:
        json.dump(result, f)
