import json


def get_data():
    with open("data.json") as file:
        return json.load(file)


def prepare_str(data: str) -> str:
    return data.lower().replace(' ', '_')
