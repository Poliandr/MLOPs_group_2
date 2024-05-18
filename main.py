from fastapi import FastAPI # import FastAPI to create web application
from pydantic import BaseModel # import BaseModel to define the schema of the request body
import joblib # import joblib to load the model
import pandas as pd


app = FastAPI() # create an application instance
# Define the input data model
class Item(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: int
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: int
    Weight_in_gms: int

model = joblib.load('model.pkl') # load the model

@app.post("/") # define a route
async def root(item: Item):
    """
    the function returns the result of prediction
    """
    X = pd.DataFrame([item.model_dump()]) # convert the input data to a pandas DataFrame
    result = "product hasn't reached on time" if model.predict(X) == 1 else "product has reached on time"
    return {"message": result}

# to run application: uvicorn main:app --port 8888