; 精准点击"进入微信"按钮
; 按钮位置: X=870, Y=600, W=180, H=36
; 按钮中心: X=960, Y=618
#Requires AutoHotkey v2.0

CoordMode("Mouse", "Screen")
hwnd := WinExist("微信")
if hwnd {
    WinActivate(hwnd)
    Sleep(300)
    Click(960, 618)
}
