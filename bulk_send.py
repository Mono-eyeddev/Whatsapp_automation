# ==============================
# bulk_send.py — Bulk Message Sender
# ==============================

import pywhatkit as kit
import time

def send_bulk():
    """Send the same message to multiple contacts."""
    contacts = []
    print("\nEnter contacts (type 'done' when finished):")
    while True:
        num = input("Number (+254...): ")
        if num.lower() == "done":
            break
        contacts.append(num)

    msg = input("Enter message for all contacts: ")

    print("\nStarting bulk send...")
    for i, num in enumerate(contacts):
        print(f"Sending to {num} ({i+1}/{len(contacts)})...")
        kit.sendwhatmsg_instantly(num, msg, 10, True, 2)
        time.sleep(3)
    print("✅ All contacts done!")
