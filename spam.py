
import pyautogui
import pyperclip
import time
from utils import countdown

def spam_mode():
    """Send unlimited messages repeatedly in the current chat."""
    msg = input("Enter message to spam: ")
    count = int(input("How many times to send? "))
    delay = float(input("Delay between messages (seconds): "))

    print("\nSwitch to WhatsApp chat window...")
    countdown(5)

    for i in range(count):
        pyperclip.copy(msg)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        print(f"Sent {i+1}/{count}")
        time.sleep(delay)
    print("✅ All messages sent!")
