#!/usr/bin/env python3
"""Send message to WeChat File Transfer Helper"""
import pyautogui
import pygetwindow as gw
import time
import pyperclip
import mss
from PIL import Image
import ctypes
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# DPI awareness
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    pass

def find_wechat_window():
    """Find the main WeChat window"""
    windows = gw.getAllWindows()
    # WeChat main window is around 800-1000 wide, 600-800 tall
    candidates = []
    for w in windows:
        if w.width > 400 and w.height > 500 and w.title and len(w.title) < 20:
            # Exclude known non-WeChat windows
            if 'Chrome' not in w.title and 'Program' not in w.title and 'Microsoft' not in w.title:
                candidates.append(w)
                print(f"  Candidate: '{w.title}' ({w.width}x{w.height}) at ({w.left},{w.top})")
    
    # Return the largest candidate that's not the desktop
    candidates.sort(key=lambda w: w.width * w.height, reverse=True)
    for c in candidates:
        if c.width < 1920:  # Not the desktop
            return c
    return None

def bring_to_front(win):
    """Bring window to front using win32 API"""
    import ctypes
    user32 = ctypes.windll.user32
    
    # Get the window handle
    hwnd = win._hWnd
    
    # Show the window
    user32.ShowWindow(hwnd, 9)  # SW_RESTORE
    time.sleep(0.3)
    
    # Bring to front
    user32.SetForegroundWindow(hwnd)
    time.sleep(0.5)
    
    print(f"Brought window to front: hwnd={hwnd}")

def take_screenshot(region=None, name="debug"):
    """Take screenshot using mss (more reliable than pyautogui)"""
    with mss.mss() as sct:
        if region:
            monitor = {"left": region[0], "top": region[1], "width": region[2], "height": region[3]}
        else:
            monitor = sct.monitors[1]  # Primary monitor
        
        img = sct.grab(monitor)
        pil_img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        path = f'C:\\Users\\Administrator\\.openclaw\\workspace\\{name}.png'
        pil_img.save(path)
        print(f"Screenshot saved: {path} ({pil_img.size})")
        return pil_img, path

# Step 1: Find WeChat
print("=== Step 1: Finding WeChat window ===")
wechat = find_wechat_window()
if not wechat:
    print("ERROR: WeChat window not found!")
    sys.exit(1)

print(f"\nUsing WeChat window: '{wechat.title}' ({wechat.width}x{wechat.height}) at ({wechat.left},{wechat.top})")

# Step 2: Bring to front
print("\n=== Step 2: Bringing WeChat to front ===")
bring_to_front(wechat)
time.sleep(0.5)

# Step 3: Screenshot to see current state
print("\n=== Step 3: Taking screenshot ===")
take_screenshot(name="wechat_step3")

# Step 4: Use Ctrl+F to open search in WeChat
print("\n=== Step 4: Opening search with Ctrl+F ===")
pyautogui.hotkey('ctrl', 'f')
time.sleep(1)
take_screenshot(name="wechat_step4_search")

# Step 5: Type "文件传输助手"
print("\n=== Step 5: Typing '文件传输助手' ===")
pyperclip.copy('文件传输助手')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1.5)
take_screenshot(name="wechat_step5_typed")

# Step 6: Press Enter to select the first result
print("\n=== Step 6: Pressing Enter to select ===")
pyautogui.press('enter')
time.sleep(1)
take_screenshot(name="wechat_step6_selected")

# Step 7: Type message and send
print("\n=== Step 7: Sending test message ===")
msg = '🤖 Hello from OpenClaw! 这是一条自动化测试消息。'
pyperclip.copy(msg)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1)
take_screenshot(name="wechat_step7_sent")

print("\n=== Done! Message should be sent. ===")
