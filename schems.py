from pydantic import BaseModel


class CarSmodel(BaseModel):
    art: str
    eurocode: str
    oldcode: str
    name: str
    catalog: str
    category: str
    price: int

class ModelToWrite(object):
    def __init__(self,):
        self.catalog = "art"
        self.category = "category"
        self.art = "art"
        self.eurocode = "eurocode"
        self.oldcode = "oldcode"
        self.name = "name"
        self.client_price = "price"
        