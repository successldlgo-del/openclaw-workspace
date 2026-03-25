import pyautogui
import time
import pyperclip
import ctypes

# Set DPI awareness
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    pass

# Step 1: Click WeChat icon in taskbar to bring it to front
# From the full screenshot, the taskbar is at bottom
# WeChat icon (green) is in the taskbar at approximately x=354, y=661 (the green icon)
# Let me look for the WeChat taskbar icon - it's the green square icon near the bottom

# The taskbar icons are at y=661 (bottom bar)
# I can see the WeChat green icon - let me click it
# Looking at the taskbar, the green WeChat icon appears to be around x=354

# Actually, let me just use the Win+D to show desktop first, then click WeChat
# Or better, just click the WeChat icon in the system tray / taskbar

# From screenshot: taskbar at bottom, icons start around x=100
# The WeChat icon looks like it's around x=354, y=661
# Let me try clicking the WeChat taskbar icon
taskbar_y = 662

# Take a screenshot of just the taskbar area to identify WeChat icon
taskbar = pyautogui.screenshot(region=(0, 640, 1920, 40))
taskbar.save(r'C:\Users\Administrator\.openclaw\workspace\taskbar.png')

# Find green pixels in taskbar (WeChat icon is green)
green_x_positions = []
for x in range(1920):
    for y in range(40):
        r, g, b = taskbar.getpixel((x, y))
        if g > 150 and r < 80 and b < 100 and g > r + 80:
            green_x_positions.append(x)

if green_x_positions:
    avg_x = sum(green_x_positions) // len(green_x_positions)
    print(f"Found green icon in taskbar at x={avg_x}, pixels={len(green_x_positions)}")
    
    # Click the WeChat taskbar icon
    pyautogui.click(avg_x, taskbar_y)
    time.sleep(1)
else:
    print("No green icon found in taskbar, trying direct coordinates")
    # From the screenshot, the WeChat icon in taskbar appears to be around x=354
    pyautogui.click(354, taskbar_y)
    time.sleep(1)

# Take screenshot to see if WeChat is now in front
full = pyautogui.screenshot()
full.save(r'C:\Users\Administrator\.openclaw\workspace\wechat_front.png')
print("WeChat front screenshot saved")
