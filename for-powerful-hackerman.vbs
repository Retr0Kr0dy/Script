Set WshShell = WScript.CreateObject("WScript.Shell")

strName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )

WshShell.Run "cmd"
WScript.sleep 400
WshShell.sendkeys "cls"
wshshell.sendkeys "{ENTER}"
WshShell.sendkeys "color a"
wshshell.sendkeys "{ENTER}"
WshShell.sendkeys "cls"
wshshell.sendkeys "{ENTER}"
WshShell.sendkeys "prompt HACKERMAN"
wshshell.sendkeys "{ENTER}"
WshShell.sendkeys "cls"
wshshell.sendkeys "{ENTER}"

Do
WScript.sleep 5
wshshell.sendkeys "{ENTER}"
wshshell.sendkeys "{ESCAPE}"
Loop
