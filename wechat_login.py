import pyautogui
import pygetwindow as gw
import time

# Find the WeChat login window (the smaller one, 296x388)
windows = gw.getAllWindows()
login_win = None
for w in windows:
    if w.title and w.width > 200 and w.width < 400 and w.height > 300 and w.height < 500:
        if '微信' in w.title or 'Weixin' in w.title or 'WeChat' in w.title:
            login_win = w
            break
        # Check with encoded title
        try:
            if w.title.encode('gbk', errors='ignore'):
                login_win = w
        except:
            pass

# Use the smaller window (login window)
wechat_windows = [w for w in windows if w.width == 296 and w.height == 388]
if wechat_windows:
    login_win = wechat_windows[0]

if login_win:
    print(f"Found login window: '{login_win.title}' at ({login_win.left}, {login_win.top}) size ({login_win.width}x{login_win.height})")
    
    # Activate the window
    try:
        login_win.activate()
        time.sleep(0.5)
    except:
        pass
    
    # The "进入微信" button is usually at the bottom center of the login window
    # Calculate center-bottom position
    center_x = login_win.left + login_win.width // 2
    # The button is typically about 70% down from the top
    button_y = login_win.top + int(login_win.height * 0.82)
    
    print(f"Clicking at ({center_x}, {button_y})")
    
    # Take screenshot first to see current state
    img = pyautogui.screenshot(region=(login_win.left, login_win.top, login_win.width, login_win.height))
    img.save(r'C:\Users\Administrator\.openclaw\workspace\wechat_login_window.png')
    print("Login window screenshot saved")
    
    # Click the button
    pyautogui.click(center_x, button_y)
    print("Clicked!")
    
    time.sleep(2)
    
    # Take another screenshot to see result
    img2 = pyautogui.screenshot()
    img2.save(r'C:\Users\Administrator\.openclaw\workspace\screen_after_click.png')
    print("After-click screenshot saved")
else:
    print("Login window not found!")
    # List all windows for debugging
    for w in windows:
        if w.title and w.width > 100:
            print(f"  '{w.title}' size={w.width}x{w.height}")
