import pandas as pd


def wirite_json(file_name:str, data: bytes):
    with open(file_name, "wb") as f:
        f.write(data)
    return True

def write_xlsx(file_name:str = 'output.xlsx', data: list[list]=[['test test']], columns:list[str] = ['test']):
    df1 = pd.DataFrame(data, columns=columns)
    df1.to_excel(file_name)  
