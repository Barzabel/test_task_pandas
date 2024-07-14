from reader import read_json
from schems import ModelToWrite
from writer import write_xlsx

def change_price(data: dict)->dict:
    if data['category'] == 'боковое':
        data['price'] = int(data['price'] * 1.1)
    elif data['category'] == 'заднее':
        data['price'] = int((data['price'] + 800) * 1.07)
    elif data['category'] == 'ветровое':
        data['price'] = int((data['price'] + 1000) * 1.05)
    return data

filds_model = ModelToWrite()

def data_from_json_to_xlsx(path_file: str, category: list[str] = ['']):
    data = read_json(path_file)
    filds = filds_model.__dict__
    filter_data = filter(lambda x: x["category"] in category, data)
    new_data = map(change_price, filter_data)
    result = []
    for x in new_data:
        row = []
        for colum in filds.values():
            row.append(x[colum])
        result.append(row)
    write_xlsx('result.xlsx', result, filds.keys())