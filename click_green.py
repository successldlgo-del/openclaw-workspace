import pyautogui
import time

# The WeChat login window is at (1103, 272) to (1399, 660) 
# Take screenshot of just that region
screen = pyautogui.screenshot(region=(1103, 272, 296, 388))

# Find green button pixels in this region
green_pixels = []
for x in range(296):
    for y in range(388):
        r, g, b = screen.getpixel((x, y))
        # WeChat green button: high green, low red, low blue
        if g > 160 and r < 80 and b < 130 and g > r + 80:
            green_pixels.append((x, y))

if green_pixels:
    # Find center of green area
    avg_x = sum(p[0] for p in green_pixels) // len(green_pixels)
    avg_y = sum(p[1] for p in green_pixels) // len(green_pixels)
    
    # Convert to screen coordinates
    screen_x = 1103 + avg_x
    screen_y = 272 + avg_y
    
    print(f"Found green button: local ({avg_x}, {avg_y}), screen ({screen_x}, {screen_y}), {len(green_pixels)} green pixels")
    
    # Click it
    pyautogui.click(screen_x, screen_y)
    print("Clicked!")
    
    time.sleep(3)
    
    # Check result
    result = pyautogui.screenshot()
    result.save(r'C:\Users\Administrator\.openclaw\workspace\result.png')
    print("Result screenshot saved")
else:
    print("No green button found in the window region!")
    screen.save(r'C:\Users\Administrator\.openclaw\workspace\window_region.png')
    print("Saved window region for inspection")
