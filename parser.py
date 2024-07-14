import pandas as pd
import numpy as np
from pydantic import TypeAdapter
from schems import CarSmodel
from reader import read_xlsx


def pars_data(path_file: str, sheet_names: list[str])->bytes:
    res = []
    for sheet_name in sheet_names:
        ru_cars = read_xlsx(path_file, sheet_name)
        for x in range(len(ru_cars['Код AGC'])):
            if not np.isnan(ru_cars['Код AGC'][x]):
                price = float(ru_cars['ОПТ'][x] if ru_cars['ОПТ'][x] != '*' else ru_cars['Цена фиксирована'][x])
                if np.isnan(price):
                    continue
                price = int(price)
                oldcode = ru_cars['Старый Код AGC'][x]
                oldcode = '{}'.format(oldcode) if isinstance(oldcode, str) else '{:.0f}'.format(oldcode)
                car_dict = CarSmodel.parse_obj({
                    "art": '{:.0f}'.format(ru_cars['Код AGC'][x]),
                    "eurocode": str(ru_cars['Еврокод'][x]),
                    "oldcode": oldcode,
                    "name": ru_cars['Наименование'][x],
                    "catalog": sheet_name,
                    "category": ru_cars['Вид стекла'][x],
                    "price": price}
                )
                res.append(car_dict)
    ta = TypeAdapter(list[CarSmodel])
    return ta.dump_json(res)












