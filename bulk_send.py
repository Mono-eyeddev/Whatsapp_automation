import pyautogui
import webbrowser
import time

def send_bulk():
    """Send the same message to multiple contacts using one WhatsApp Web session."""
    # User pastes a Python-style list of contacts
    contacts_input = input('Enter contacts as a Python list (e.g. ["+2547...", "+2541..."]): ')
    contacts = eval(contacts_input)  # Convert string input to actual Python list
    msg = input("Enter message for all contacts: ")

    print("\nOpening WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(15)  # wait for WhatsApp Web login

    for i, num in enumerate(contacts):
        print(f"Sending to {num} ({i+1}/{len(contacts)})...")

        # open chat with this number in the same window
        search_url = f"https://web.whatsapp.com/send?phone={num}&text={msg}"
        webbrowser.open(search_url)  # reuses current tab on most browsers
        time.sleep(8)

        pyautogui.press('enter')  # send message
        print(f"✅ Message sent to {num}")

        time.sleep(3)

    print("\nAll messages sent successfully amigo! ✅")
