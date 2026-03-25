import pyautogui
import pygetwindow as gw
import time
import pyperclip

# Step 1: Activate WeChat main window (892x698)
windows = gw.getAllWindows()
wechat_main = None
for w in windows:
    if w.width == 892 and w.height == 698:
        wechat_main = w
        break

if not wechat_main:
    # Fallback: find by approximate size
    for w in windows:
        if 800 < w.width < 1000 and 600 < w.height < 800 and w.title and len(w.title) < 10:
            wechat_main = w
            break

if not wechat_main:
    print("WeChat main window not found!")
    exit()

print(f"Found WeChat main window: ({wechat_main.left}, {wechat_main.top}) {wechat_main.width}x{wechat_main.height}")

# Activate the window
try:
    wechat_main.activate()
    time.sleep(0.5)
except:
    pyautogui.click(wechat_main.left + wechat_main.width // 2, wechat_main.top + wechat_main.height // 2)
    time.sleep(0.5)

# Take a screenshot to see current state
img = pyautogui.screenshot(region=(wechat_main.left, wechat_main.top, wechat_main.width, wechat_main.height))
img.save(r'C:\Users\Administrator\.openclaw\workspace\wechat_main.png')
print("Main window screenshot saved")

# Step 2: Click the search box (usually at the top of the WeChat window)
# The search box is typically near the top, around 15-20% from top
search_x = wechat_main.left + 160  # Search box is in the left panel
search_y = wechat_main.top + 60    # Near the top
print(f"Clicking search at ({search_x}, {search_y})")
pyautogui.click(search_x, search_y)
time.sleep(0.5)

# Take screenshot to verify search box is active
img2 = pyautogui.screenshot(region=(wechat_main.left, wechat_main.top, wechat_main.width, wechat_main.height))
img2.save(r'C:\Users\Administrator\.openclaw\workspace\wechat_search.png')
print("Search state screenshot saved")

# Step 3: Type "文件传输助手" using clipboard (to handle Chinese input)
pyperclip.copy('文件传输助手')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Take screenshot to see search results
img3 = pyautogui.screenshot(region=(wechat_main.left, wechat_main.top, wechat_main.width, wechat_main.height))
img3.save(r'C:\Users\Administrator\.openclaw\workspace\wechat_search_result.png')
print("Search result screenshot saved")
