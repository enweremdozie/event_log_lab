import os
import pandas as pd
from Evtx.Evtx import Evtx
import smtplib
from email.message import EmailMessage

LOG_PATH = "logs"
OUTPUT = "results/suspicious_logins.csv"

# ---------------- EMAIL SETTINGS ---------------- #
EMAIL_ENABLED = True
EMAIL_FROM = ""
EMAIL_TO = ""
EMAIL_SUBJECT = "ALERT: Suspicious Login Detected"
EMAIL_PASSWORD = ""  # Use app password if using Gmail

# ---------------- FUNCTIONS ------------------- #
def parse_evtx(file):
    records = []
    with Evtx(file) as evtx:
        for record in evtx.records():
            xml = record.xml()
            if "4625" in xml:  # Failed login
                records.append(xml)
    return records

def save_csv(data):
    df = pd.DataFrame(data, columns=["RawXML"])
    df.to_csv(OUTPUT, index=False)
    print(f"[+] Saved {len(data)} suspicious entries to {OUTPUT}")

def send_email(message):
    if not EMAIL_ENABLED or not message:
        return
    try:
        email = EmailMessage()
        email.set_content(message)
        email['Subject'] = EMAIL_SUBJECT
        email['From'] = EMAIL_FROM
        email['To'] = EMAIL_TO

        # Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
            smtp.send_message(email)
        print("[+] Email alert sent!")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

# ---------------- MAIN ------------------- #
def main():
    all_records = []
    for filename in os.listdir(LOG_PATH):
        if filename.endswith(".evtx"):
            full_path = os.path.join(LOG_PATH, filename)
            print(f"[•] Parsing {full_path}")
            all_records += parse_evtx(full_path)

    if all_records:
        save_csv(all_records)
        send_email(f"Suspicious login events found: {len(all_records)}")
    else:
        print("[✓] No suspicious logins found.")

if __name__ == "__main__":
    main()
