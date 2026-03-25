from pywinauto import Application
import time

try:
    # Connect to WeChat using win32 backend
    app = Application(backend='win32').connect(path=r'D:\otherTool\weChat\install\Weixin\Weixin.exe')
    
    # Get the main window
    dlg = app.window(class_name_re='.*')
    print(f"Connected to WeChat window")
    print(f"Window rect: {dlg.rectangle()}")
    
    # Print all controls
    dlg.print_control_identifiers()
    
except Exception as e:
    print(f"win32 backend error: {e}")
    
    try:
        # Try UIA backend
        app = Application(backend='uia').connect(path=r'D:\otherTool\weChat\install\Weixin\Weixin.exe')
        dlg = app.window(title_re='.*微信.*|.*WeChat.*|.*Weixin.*')
        print(f"Connected via UIA")
        dlg.print_control_identifiers(depth=3)
    except Exception as e2:
        print(f"UIA backend error: {e2}")
        
        # Last resort: just use pyautogui to locate the green button by color
        import pyautogui
        import PIL.Image
        
        # Take screenshot
        screen = pyautogui.screenshot()
        screen.save(r'C:\Users\Administrator\.openclaw\workspace\full_screen.png')
        
        # Look for the green color of the button (approximately #07C160)
        # Search in the area where the login window should be
        width, height = screen.size
        print(f"Screen size: {width}x{height}")
        
        # Find green button pixels
        green_pixels = []
        for x in range(width):
            for y in range(height):
                r, g, b = screen.getpixel((x, y))
                # Green button color range
                if g > 150 and r < 50 and b < 120 and g > r + 100:
                    green_pixels.append((x, y))
        
        if green_pixels:
            # Find center of green area
            avg_x = sum(p[0] for p in green_pixels) // len(green_pixels)
            avg_y = sum(p[1] for p in green_pixels) // len(green_pixels)
            print(f"Found green button area, center at ({avg_x}, {avg_y}), {len(green_pixels)} pixels")
            
            pyautogui.click(avg_x, avg_y)
            print("Clicked green button!")
            
            time.sleep(2)
            screen2 = pyautogui.screenshot()
            screen2.save(r'C:\Users\Administrator\.openclaw\workspace\after_green_click.png')
        else:
            print("No green button found!")
