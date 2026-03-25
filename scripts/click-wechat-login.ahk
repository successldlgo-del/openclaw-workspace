; 自动点击微信"进入微信"登录按钮
#Requires AutoHotkey v2.0

; 等待微信登录窗口出现
if WinWait("微信", , 10) {
    WinActivate("微信")
    Sleep(1000)
    
    ; 获取窗口位置和大小
    WinGetPos(&x, &y, &w, &h, "微信")
    
    ; "进入微信"按钮通常在窗口底部中间偏下
    btnX := x + (w // 2)
    btnY := y + h - 80
    
    Click(btnX, btnY)
    Sleep(500)
    
    ; 备用：尝试发送回车键
    Send("{Enter}")
}
