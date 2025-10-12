# ==============================
# utils.py — Helper Functions
# ==============================

import pyautogui
import time

# Safety feature: moving mouse to top-left corner stops the script
pyautogui.FAILSAFE = True

def countdown(seconds):
    """Display countdown to allow user to switch windows."""
    for i in range(seconds, 0, -1):
        print(f"Starting in {i}...", end="\r")
        time.sleep(1)
    print("Go!\n")
