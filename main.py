from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/maths/") # {val_01}/{val_02}/{operator}
def calculator(val_01: float, val_02: float, operator):
    """API's endpoint to do simple math operations 
    """

    operator = operator.lower().strip() # operator cleaning
    op = ""
    if operator.lower().strip() == "add":
        result = val_01 + val_02
        op = "+"
    elif operator == "sub":
        result = val_01 - val_02
        op = "-"
    elif operator == "":
        pass
    elif operator == "":
        pass
    
    return {"value_A": val_01, "value_b": val_02,
            "string": f"{val_01} {op} {val_02} = {result}" ,  
            "result":result}