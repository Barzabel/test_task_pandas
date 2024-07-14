import pandas as pd
import json

HEADER_INDENT = 4


def read_xlsx(path_file, sheet_name):
    return pd.read_excel(path_file, sheet_name = sheet_name, header=HEADER_INDENT)

def read_json(path_file):
    with open(path_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
