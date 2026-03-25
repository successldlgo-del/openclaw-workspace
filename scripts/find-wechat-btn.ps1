Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes

$hwnd = (Get-Process Weixin | Where-Object { $_.MainWindowHandle -ne 0 }).MainWindowHandle
Write-Output "HWND: $hwnd"

$ae = [System.Windows.Automation.AutomationElement]::FromHandle($hwnd)
Write-Output "Root: $($ae.Current.Name) [$($ae.Current.ControlType.ProgrammaticName)]"

# Find all buttons
$btnCondition = New-Object System.Windows.Automation.PropertyCondition([System.Windows.Automation.AutomationElement]::ControlTypeProperty, [System.Windows.Automation.ControlType]::Button)
$buttons = $ae.FindAll([System.Windows.Automation.TreeScope]::Descendants, $btnCondition)
Write-Output "Found $($buttons.Count) buttons:"
foreach ($btn in $buttons) {
    $rect = $btn.Current.BoundingRectangle
    Write-Output "  Button: '$($btn.Current.Name)' at [$($rect.X),$($rect.Y),$($rect.Width),$($rect.Height)]"
}

# Also find all text elements
$txtCondition = New-Object System.Windows.Automation.PropertyCondition([System.Windows.Automation.AutomationElement]::ControlTypeProperty, [System.Windows.Automation.ControlType]::Text)
$texts = $ae.FindAll([System.Windows.Automation.TreeScope]::Descendants, $txtCondition)
Write-Output "Found $($texts.Count) texts:"
foreach ($txt in $texts) {
    $rect = $txt.Current.BoundingRectangle
    Write-Output "  Text: '$($txt.Current.Name)' at [$($rect.X),$($rect.Y),$($rect.Width),$($rect.Height)]"
}

# Find all elements
$allCondition = [System.Windows.Automation.Condition]::TrueCondition
$all = $ae.FindAll([System.Windows.Automation.TreeScope]::Children, $allCondition)
Write-Output "Top-level children: $($all.Count)"
foreach ($child in $all) {
    Write-Output "  $($child.Current.ControlType.ProgrammaticName): '$($child.Current.Name)' ClassName=$($child.Current.ClassName)"
}
