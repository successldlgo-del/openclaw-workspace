Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes

$hwnd = (Get-Process Weixin | Where-Object { $_.MainWindowHandle -ne 0 }).MainWindowHandle
$ae = [System.Windows.Automation.AutomationElement]::FromHandle($hwnd)

# Find the "进入微信" button by position (870,600,180,36)
$btnCondition = New-Object System.Windows.Automation.PropertyCondition(
    [System.Windows.Automation.AutomationElement]::ControlTypeProperty, 
    [System.Windows.Automation.ControlType]::Button
)
$buttons = $ae.FindAll([System.Windows.Automation.TreeScope]::Descendants, $btnCondition)

foreach ($btn in $buttons) {
    $rect = $btn.Current.BoundingRectangle
    if ($rect.Y -gt 590 -and $rect.Y -lt 610 -and $rect.Width -gt 100) {
        Write-Output "Found button: '$($btn.Current.Name)' at [$($rect.X),$($rect.Y)]"
        
        # Try InvokePattern
        try {
            $invokePattern = $btn.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern)
            $invokePattern.Invoke()
            Write-Output "InvokePattern: SUCCESS"
        } catch {
            Write-Output "InvokePattern failed: $_"
            
            # Fallback: SendKeys
            try {
                $btn.SetFocus()
                [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
                Write-Output "SendKeys: sent Enter"
            } catch {
                Write-Output "SendKeys failed: $_"
            }
        }
    }
}
