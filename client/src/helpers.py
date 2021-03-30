import json


def get_credentials(file):
    with open(file) as credentials:
        data = json.load(credentials)

    return data
