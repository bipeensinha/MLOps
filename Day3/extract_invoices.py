# pip install pypdf
# python -m pip install pypdf 
import re
import pandas as pd
from pathlib import Path
from pypdf import PdfReader


# --------------------------------------------------
# Folders
# --------------------------------------------------

INVOICE_FOLDER = Path("../invoices")
OUTPUT_FOLDER = Path("../output")

OUTPUT_FOLDER.mkdir(exist_ok=True)


# --------------------------------------------------
# Extract text from PDF
# --------------------------------------------------

def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


# --------------------------------------------------
# Extract one invoice
# --------------------------------------------------

def extract_invoice(pdf_file):

    print(f"Reading: {pdf_file.name}")

    text = extract_text_from_pdf(pdf_file)

    # ----------------------------------------------
    # Invoice Number
    # ----------------------------------------------

    invoice_number = re.search(
        r"Invoice Number\s+(INV-\d+-\d+)",
        text
    )

    # ----------------------------------------------
    # Customer
    # ----------------------------------------------

    customer = re.search(
        r"Customer\s+(Customer \d+)",
        text
    )

    # ----------------------------------------------
    # Account
    # ----------------------------------------------

    account = re.search(
        r"Account\s+(ACC-\d+)",
        text
    )

    # ----------------------------------------------
    # Mobile
    # ----------------------------------------------

    mobile = re.search(
        r"Mobile\s+(\+91\s+\d+\s+\d+)",
        text
    )

    # ----------------------------------------------
    # Plan
    # ----------------------------------------------

    plan = re.search(
        r"Plan\s+(.+?)\nUsage Summary",
        text,
        re.DOTALL
    )

    # ----------------------------------------------
    # Billing Period
    # ----------------------------------------------

    billing_period = re.search(
        r"Billing Period\s+(.+?)\nPayment Due",
        text
    )

    # ----------------------------------------------
    # Data Usage
    # ----------------------------------------------

    data_usage = re.search(
        r"Mobile Data\s+([\d.]+)\s+GB",
        text
    )

    # ----------------------------------------------
    # Number of Calls
    # ----------------------------------------------

    calls = re.search(
        r"Voice Calls\s+(\d+)\s+calls",
        text
    )

    # ----------------------------------------------
    # Voice Duration
    # ----------------------------------------------

    voice_duration = re.search(
        r"Voice Duration\s+([\d.]+)\s+minutes",
        text
    )

    # ----------------------------------------------
    # SMS
    # ----------------------------------------------

    sms = re.search(
        r"SMS\s+(\d+)\s+messages",
        text
    )

    # ----------------------------------------------
    # Total Bill
    # ----------------------------------------------

    total_bill = re.search(
        r"TOTAL AMOUNT DUE\s+[^\d]*([\d,]+\.\d+)",
        text
    )

    # ----------------------------------------------
    # Convert values
    # ----------------------------------------------

    data = float(data_usage.group(1)) if data_usage else None

    call_count = int(calls.group(1)) if calls else None

    voice = float(voice_duration.group(1)) if voice_duration else None

    sms_count = int(sms.group(1)) if sms else None

    bill = (
        float(total_bill.group(1).replace(",", ""))
        if total_bill
        else None
    )

    # ----------------------------------------------
    # Create extracted record
    # ----------------------------------------------

    return {

        "InvoiceNumber":
            invoice_number.group(1)
            if invoice_number else None,

        "CustomerID":
            customer.group(1).replace("Customer ", "")
            if customer else None,

        "Account":
            account.group(1)
            if account else None,

        "Mobile":
            mobile.group(1)
            if mobile else None,

        "Plan":
            plan.group(1).strip()
            if plan else None,

        "BillingPeriod":
            billing_period.group(1).strip()
            if billing_period else None,

        "DataGB":
            data,

        "Calls":
            call_count,

        "VoiceMinutes":
            voice,

        "SMS":
            sms_count,

        "BillAmount":
            bill
    }


# --------------------------------------------------
# Process all PDF invoices
# --------------------------------------------------

records = []

pdf_files = list(
    INVOICE_FOLDER.glob("*.pdf")
)

print()
print("======================================")
print("PDF INVOICE EXTRACTION")
print("======================================")
print()

print(
    f"Found {len(pdf_files)} PDF invoice(s)"
)

print()


for pdf_file in pdf_files:

    try:

        record = extract_invoice(pdf_file)

        records.append(record)

        print(
            f"PASS - Extracted {pdf_file.name}"
        )

    except Exception as e:

        print(
            f"FAIL - {pdf_file.name}: {e}"
        )


# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

df = pd.DataFrame(records)


# --------------------------------------------------
# Save CSV
# --------------------------------------------------

output_file = (
    OUTPUT_FOLDER /
    "billing_data_extracted.csv"
)

df.to_csv(
    output_file,
    index=False
)


# --------------------------------------------------
# Display results
# --------------------------------------------------

print()
print("======================================")
print("EXTRACTION COMPLETE")
print("======================================")

print()

print(df.to_string(index=False))

print()

print(
    f"CSV created: {output_file}"
)