import pyautogui
import pygetwindow as gw
import time

# Find WeChat login window again (it may have moved)
windows = gw.getAllWindows()
for w in windows:
    if w.title and w.width > 200 and w.width < 500 and w.height > 300 and w.height < 500:
        print(f"Candidate: '{w.title}' at ({w.left}, {w.top}) size ({w.width}x{w.height})")

# From the screenshot, the login window appears to be around center-right of screen
# Let me find it by looking for the green button using image
# First, let me try clicking directly on the "进入微信" button position
# From the screenshot, the window seems to be at roughly (700, 170) to (870, 430) area

# Re-find the window
login_wins = [w for w in windows if w.width < 400 and w.height < 500 and w.height > 300]
for w in login_wins:
    if w.title:
        print(f"Small window: '{w.title}' at ({w.left}, {w.top}) size ({w.width}x{w.height})")

# Get the WeChat login window
for w in windows:
    if w.width == 296 or (w.width > 250 and w.width < 350 and w.height > 350 and w.height < 450):
        login_win = w
        print(f"\nUsing window: '{w.title}' at ({w.left}, {w.top}) size ({w.width}x{w.height})")
        
        # Bring to front
        try:
            w.activate()
            time.sleep(0.5)
        except:
            pass
        
        # Take fresh screenshot of just this window
        img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
        img.save(r'C:\Users\Administrator\.openclaw\workspace\login_fresh.png')
        
        # Click the "进入微信" button - it's the green button
        # From the captured screenshot, button is at roughly 82% height, center width
        btn_x = w.left + w.width // 2
        btn_y = w.top + int(w.height * 0.82)
        
        print(f"Clicking at ({btn_x}, {btn_y})")
        pyautogui.click(btn_x, btn_y)
        time.sleep(1)
        pyautogui.click(btn_x, btn_y)  # Double click for safety
        
        print("Done!")
        break
