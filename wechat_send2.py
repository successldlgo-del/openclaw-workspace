import pyautogui
import pygetwindow as gw
import time
import pyperclip
import ctypes

# Check DPI scaling
try:
    awareness = ctypes.c_int()
    ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
    print(f"DPI awareness: {awareness.value}")
except:
    pass

# Set DPI awareness
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Per-monitor DPI aware
    print("Set DPI awareness to per-monitor")
except:
    pass

# Step 1: Take full screenshot to see actual layout
full = pyautogui.screenshot()
full.save(r'C:\Users\Administrator\.openclaw\workspace\full_screen2.png')
print(f"Full screen size: {full.size}")

# Step 2: Use keyboard shortcut to activate WeChat search
# First, click on the WeChat window in taskbar or use Alt+Tab
# WeChat hotkey is usually Ctrl+Alt+W or we can click the taskbar

# Let me find WeChat by process and use win32 API
import subprocess
result = subprocess.run(['powershell', '-Command', 
    '(Get-Process Weixin).MainWindowHandle'], 
    capture_output=True, text=True)
print(f"WeChat handle: {result.stdout.strip()}")

# Use pyautogui to find WeChat by taking full screenshot first
# and looking at where windows actually are
windows = gw.getAllWindows()
for w in windows:
    if w.title and 'Chrome' not in w.title and 'Program' not in w.title and 'Microsoft' not in w.title and w.width > 100:
        print(f"Window: '{w.title}' pos=({w.left},{w.top}) size=({w.width}x{w.height})")
