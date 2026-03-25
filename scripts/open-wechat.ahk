; 打开微信并点击"进入微信"按钮
#Requires AutoHotkey v2.0

; 启动微信
Run "C:\Program Files\Tencent\WeChat\WeChat.exe"

; 等待微信窗口出现（最多等10秒）
if WinWait("微信", , 10) {
    WinActivate
    Sleep 2000  ; 等待界面加载

    ; 尝试查找并点击"进入微信"按钮
    try {
        ; 方法1：用 ControlClick 查找按钮
        ControlClick "进入微信", "微信"
    } catch {
        ; 方法2：用图像坐标点击（窗口中心偏下位置，通常是"进入微信"按钮的位置）
        WinGetPos &x, &y, &w, &h, "微信"
        Click x + w // 2, y + h * 0.75
    }
} else {
    MsgBox "未检测到微信窗口，请确认微信已安装"
}
