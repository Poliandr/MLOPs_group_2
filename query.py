import requests

url = "http://127.0.0.1:8888"

data = {
    "Warehouse_block": "D",
    "Mode_of_Shipment": "Flight",
    "Customer_care_calls": 4,
    "Customer_rating": 2,
    "Cost_of_the_Product": 177,
    "Prior_purchases": 3,
    "Product_importance": "low",
    "Gender": "F",
    "Discount_offered": 44,
    "Weight_in_gms": 1233
}

response = requests.post(url, json=data)
print(response.json())