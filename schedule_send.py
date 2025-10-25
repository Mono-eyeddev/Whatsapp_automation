import pywhatkit as kit

def schedule_message():
    """Schedule a WhatsApp message at a specific time."""
    msg = input("Enter message: ")
    num = input("Enter phone number (+254...): ")
    time_input = input("Enter time (HH:MM, 24hr format): ")

    try:
        hour, minute = map(int, time_input.split(":"))
        kit.sendwhatmsg(num, msg, hour, minute)
        print(f"✅ Scheduled message at {hour}:{minute:02d}")
    except ValueError:
        print("❌ Invalid time format. Please use HH:MM (e.g. 21:30).")



