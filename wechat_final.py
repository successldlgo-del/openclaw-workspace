#!/usr/bin/env python3
"""Send message to WeChat File Transfer Helper - using win32 API directly"""
import ctypes
import ctypes.wintypes
import time
import pyperclip
import pyautogui
import mss
from PIL import Image
import sys
import io
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# DPI awareness
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    pass

user32 = ctypes.windll.user32

def screenshot(name="debug"):
    with mss.mss() as sct:
        img = sct.grab(sct.monitors[1])
        pil = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        path = f'C:\\Users\\Administrator\\.openclaw\\workspace\\{name}.png'
        pil.save(path)
        print(f"  Screenshot: {path}")
        return path

def find_wechat_hwnd():
    """Find WeChat main window handle using EnumWindows"""
    results = []
    
    # Use PowerShell to find WeChat process and window
    ps_cmd = '''
    $procs = Get-Process -Name Weixin -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        if ($p.MainWindowHandle -ne 0) {
            Write-Output "$($p.MainWindowHandle)|$($p.MainWindowTitle)|$($p.Id)"
        }
    }
    '''
    result = subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-NoProfile", "-Command", ps_cmd],
        capture_output=True, text=True, timeout=10
    )
    print(f"PowerShell output: {result.stdout.strip()}")
    
    for line in result.stdout.strip().split('\n'):
        if '|' in line:
            parts = line.strip().split('|')
            hwnd = int(parts[0])
            title = parts[1]
            pid = parts[2]
            results.append((hwnd, title, pid))
            print(f"  Found: hwnd={hwnd}, title='{title}', pid={pid}")
    
    # Also enumerate all windows of the process
    EnumWindows = user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)
    GetWindowText = user32.GetWindowTextW
    GetWindowTextLength = user32.GetWindowTextLengthW
    IsWindowVisible = user32.IsWindowVisible
    GetWindowRect = user32.GetWindowRect
    
    all_windows = []
    
    def callback(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                title = buff.value
                
                rect = ctypes.wintypes.RECT()
                GetWindowRect(hwnd, ctypes.byref(rect))
                w = rect.right - rect.left
                h = rect.bottom - rect.top
                
                if '微信' in title or 'WeChat' in title:
                    all_windows.append((hwnd, title, rect.left, rect.top, w, h))
                    print(f"  EnumWindows found: hwnd={hwnd}, title='{title}', pos=({rect.left},{rect.top}), size=({w}x{h})")
        return True
    
    EnumWindows(EnumWindowsProc(callback), 0)
    
    # Return the largest WeChat window (main chat window)
    if all_windows:
        all_windows.sort(key=lambda x: x[4] * x[5], reverse=True)
        return all_windows[0][0], all_windows[0][1]
    
    if results:
        return results[0][0], results[0][1]
    
    return None, None

# Step 1: Find WeChat
print("=== Step 1: Finding WeChat ===")
hwnd, title = find_wechat_hwnd()
if not hwnd:
    print("ERROR: WeChat not found!")
    sys.exit(1)
print(f"\nUsing hwnd={hwnd}, title='{title}'")

# Step 2: Activate WeChat window
print("\n=== Step 2: Activating WeChat ===")
user32.ShowWindow(hwnd, 9)  # SW_RESTORE
time.sleep(0.3)
user32.SetForegroundWindow(hwnd)
time.sleep(0.8)
screenshot("final_step2")

# Step 3: Use Ctrl+F to search
print("\n=== Step 3: Search (Ctrl+F) ===")
pyautogui.hotkey('ctrl', 'f')
time.sleep(1)
screenshot("final_step3")

# Step 4: Type search term
print("\n=== Step 4: Typing search term ===")
pyperclip.copy('文件传输助手')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1.5)
screenshot("final_step4")

# Step 5: Press Enter
print("\n=== Step 5: Select result ===")
pyautogui.press('enter')
time.sleep(1)
screenshot("final_step5")

# Step 6: Type and send message
print("\n=== Step 6: Send message ===")
msg = '🤖 Hello from OpenClaw! 这是一条自动化测试消息，证明我有操控微信的能力。'
pyperclip.copy(msg)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1)
screenshot("final_step6")

print("\n=== DONE ===")
