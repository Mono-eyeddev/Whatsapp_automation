
import pywhatkit as kit

def send_instant():
    """Send an instant WhatsApp message using pywhatkit."""
    msg = input("Enter message: ")
    num = input("Enter phone number (with +254...): ")
    print("Opening WhatsApp Web...")
    kit.sendwhatmsg_instantly(num, msg, wait_time=10,tab_close=True)
    print("✅ Message sent!")
