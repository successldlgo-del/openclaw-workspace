import pyautogui
import time

# Find and click WeChat login button
# First take a screenshot
img = pyautogui.screenshot()
img.save(r'C:\Users\Administrator\.openclaw\workspace\screen.png')
print("Screenshot saved")

# Try to find WeChat window using pyautogui
import pygetwindow as gw
windows = gw.getAllWindows()
for w in windows:
    if w.title:
        print(f"Window: {w.title}")

# Look for WeChat window specifically
wechat_windows = [w for w in windows if 'Weixin' in w.title or '微信' in w.title or 'WeChat' in w.title or 'WeChatLoginWndForPC' in w.title]
print(f"\nFound {len(wechat_windows)} WeChat windows")
for w in wechat_windows:
    print(f"  WeChat window: '{w.title}' at ({w.left}, {w.top}) size ({w.width}x{w.height})")
