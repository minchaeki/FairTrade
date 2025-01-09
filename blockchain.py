import hashlib
import qrcode
import json  # JSON 처리를 위해 추가
from PIL import Image
import time

# FairTradeBlock is the blockchain class for fair trade blocks
class FairTradeBlock:
    def __init__(self, info, previous_hash, transaction, fair_trade_data):
        self.block_data = {
            "info": info,  # Product information
            "transaction": transaction,  # Transaction data
            "previous_hash": previous_hash,  # Previous block hash
            "fair_trade_data": fair_trade_data  # Fair trade information
        }
        string_to_hash = info + "".join(transaction) + previous_hash + str(fair_trade_data)
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

# Fair trade product class
class FairTradeProduct:
    def __init__(self, name, farmer, production_date, processing_details):
        self.name = name
        self.farmer = farmer
        self.production_date = production_date
        self.processing_details = processing_details
        self.info = name + ";" + farmer + ";" + production_date + ";" + processing_details

# Get time before starting to process
then_time = time.time()

# Create unique hash for the farmer
farmer_id = hashlib.sha256("JOHN'S FAIR TRADE FARM".encode()).hexdigest()
product = FairTradeProduct("Coffee", str(farmer_id), "2025-01-01", "Roasted and Packaged")

print("Product Info: ")
print(product.info + "\n")

# Fair trade data for the product
fair_trade_data = {
    "worker_average_age": 35,
    "worker_wage_info": 20,  # Hourly wage in dollars
    "environment_certification": "Fair Trade Certified"
}

# First block in the blockchain
genesis_block = FairTradeBlock(product.info, "0", ["Transaction_1"], fair_trade_data)
print("Genesis Block Data: ")
print(genesis_block.block_data)
print("Genesis Block Hash: ")
print(genesis_block.block_hash + "\n")

# Second block in the blockchain
second_block = FairTradeBlock(product.info, genesis_block.block_hash, ["Transaction_2"], fair_trade_data)
print("Second Block Data: ")
print(second_block.block_data)
print("Second Block Hash: ")
print(second_block.block_hash + "\n")

# Save block data as JSON
block_data_json = {
    "productName": "Coffee",
    "productionDate": "2025-01-01",
    "processingDetails": "Roasted and Packaged",
    "farmName": "John's Fair Trade Farm",
    "farmLocation": "Ethiopia",
    "workerAverageAge": 30,
    "workerWage": 20,
    "environmentCertification": "Fair Trade Certified"
}

# Write JSON to a file
with open("block_data.json", "w") as json_file:
    json.dump(block_data_json, json_file, indent=4)
    print("[!] Block data saved as JSON in 'block_data.json'")

# QR Code generation
qr_code = qrcode.QRCode(
    version=30,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=4
)
# QR Code data
webpage_url = "https://minchaeki.github.io/FairTrade"  # Example URL
qr_code.add_data(webpage_url)
print("[!] Embedded data in QR code: \n" + webpage_url + "\n")
qr_code.make(fit=True)
img = qr_code.make_image(fill_color="#451bfe", back_color="white").convert('RGB')

# Save QR Code
img.save("qrcode_fair_trade.png")

# Execution time
time_def = time.time() - then_time
print("[!] Execution time: " + str(time_def))
