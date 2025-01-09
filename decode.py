from pyzbar.pyzbar import decode
from PIL import Image
import ast
import hashlib

# Function to return key for any value
def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key
    return "key doesn't exist"

# Dictionary of farmers with their unique hash codes
farmers_dict = {
    "JOHN'S FAIR TRADE FARM": str(hashlib.sha256("JOHN'S FAIR TRADE FARM".encode()).hexdigest()),
    "GREEN ORGANIC FARM": str(hashlib.sha256("GREEN ORGANIC FARM".encode()).hexdigest()),
    "SUSTAINABLE FARMS LTD": str(hashlib.sha256("SUSTAINABLE FARMS LTD".encode()).hexdigest())
}

# Decode the QR code
qr = decode(Image.open('qrcode_fair_trade.png'))

# Extract data from QR code
decoded_data = str(qr[0].data, 'utf-8')
decoded_block = ast.literal_eval(decoded_data.split(";")[0])  # Convert string to dictionary

# Extract fair trade data
fair_trade_data = decoded_block["fair_trade_data"]
worker_average_age = fair_trade_data["worker_average_age"]
worker_wage_info = fair_trade_data["worker_wage_info"]
environment_certification = fair_trade_data["environment_certification"]

# Extract farmer name
farmer_hash = decoded_block["info"].split(";")[1]
farmer_name = get_key(farmer_hash, farmers_dict)

# Print decoded information
print("Product Name:", decoded_block["info"].split(";")[0])
print("Farmer Name:", farmer_name)
print("Production Date:", decoded_block["info"].split(";")[2])
print("Processing Details:", decoded_block["info"].split(";")[3])
print("Worker Average Age:", worker_average_age)
print("Worker Wage Info ($/hour):", worker_wage_info)
print("Environment Certification:", environment_certification)