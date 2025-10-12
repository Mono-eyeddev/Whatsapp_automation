# ==============================
# schedule_send.py — Schedule Message
# ==============================

import pywhatkit as kit

def schedule_message():
    """Schedule a WhatsApp message at a specific time."""
    msg = input("Enter message: ")
    num = input("Enter phone number (+254...): ")
    hour = int(input("Hour (24hr format): "))
    minute = int(input("Minute: "))

    kit.sendwhatmsg(num, msg, hour, minute)
    print(f"✅ Scheduled message at {hour}:{minute:02d}")
