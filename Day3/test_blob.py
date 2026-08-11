from blob_utils import download_blob

print("Testing Azure Blob Storage...")

download_blob(
    "raw-data/billing_data_extracted.csv",
    "billing_data_extracted.csv"
)

print("Blob access successful!")
