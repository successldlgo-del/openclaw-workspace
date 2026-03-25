Add-Type @"
using System;
using System.Runtime.InteropServices;
using System.Threading;

public class MouseClicker {
    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);
    
    [DllImport("user32.dll")]
    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
    
    [DllImport("user32.dll")]
    public static extern void SetCursorPos(int x, int y);
    
    [DllImport("user32.dll")]
    public static extern void mouse_event(uint dwFlags, int dx, int dy, uint dwData, IntPtr dwExtraInfo);
    
    public const uint MOUSEEVENTF_LEFTDOWN = 0x0002;
    public const uint MOUSEEVENTF_LEFTUP = 0x0004;
    
    public static void ClickAt(int x, int y) {
        SetCursorPos(x, y);
        Thread.Sleep(100);
        mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, IntPtr.Zero);
        Thread.Sleep(50);
        mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, IntPtr.Zero);
    }
}
"@

$hwnd = (Get-Process Weixin | Where-Object { $_.MainWindowHandle -ne 0 }).MainWindowHandle

# Bring window to front
[MouseClicker]::ShowWindow($hwnd, 9)  # SW_RESTORE
Start-Sleep -Milliseconds 300
[MouseClicker]::SetForegroundWindow($hwnd)
Start-Sleep -Milliseconds 500

# Click center of "进入微信" button: (870,600) size (180,36) -> center (960, 618)
Write-Output "Clicking at (960, 618)..."
[MouseClicker]::ClickAt(960, 618)
Start-Sleep -Milliseconds 500

# Double check - click again
Write-Output "Clicking again..."
[MouseClicker]::ClickAt(960, 618)

Write-Output "Done"
