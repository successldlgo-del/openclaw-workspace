import pyautogui
import pygetwindow as gw
import time

# Step 1: Find and activate WeChat main window
windows = gw.getAllWindows()
for w in windows:
    if w.title and w.width > 400:
        print(f"Window: '{w.title}' at ({w.left}, {w.top}) size ({w.width}x{w.height})")

# Find the main WeChat window (the larger one)
main_win = None
for w in windows:
    if w.width > 400 and w.height > 600:
        # Check if it's WeChat
        t = w.title
        if t and len(t) < 20:  # WeChat window title is short
            print(f"\nCandidate main window: '{t}' size={w.width}x{w.height}")
            main_win = w

print("\n--- All windows with title ---")
for w in windows:
    if w.title:
        print(f"  '{w.title}' ({w.width}x{w.height})")
