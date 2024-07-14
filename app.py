from parser import pars_data
from writer import wirite_json
from tools import data_from_json_to_xlsx

path_file = "" #  ! необходимо установить путь до файла data.xlsx
sheet_name1 = 'Российский автопром'
sheet_name2 = 'Автостекло. Аксессуары. Клей'
category = ["ветровое", "заднее", "боковое"]
json_path = '1.json'

# _______task 1________
data = pars_data(path_file, [sheet_name1, sheet_name2])

wirite_json(json_path, data)

# _______task 2________
data_from_json_to_xlsx(json_path, category)
