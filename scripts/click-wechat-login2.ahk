; 精准点击微信登录按钮
#Requires AutoHotkey v2.0

; 窗口位置: Left=812 Top=330, Size=296x388
; "进入微信"按钮在窗口下半部分中间

hwnd := WinExist("微信")
if hwnd {
    WinActivate(hwnd)
    Sleep(500)
    
    ; 窗口中心X=960, 按钮大概在窗口底部1/4处
    ; 窗口: 812,330 到 1108,718
    ; 按钮估算位置: X=960(中心), Y=约640(底部往上约80px)
    Click(960, 640)
    Sleep(300)
    Click(960, 640)
    Sleep(300)
    
    ; 再试几个可能的位置
    Click(960, 620)
    Sleep(300)
    Click(960, 660)
    Sleep(300)
    
    ; 最后试回车
    Send("{Enter}")
}
