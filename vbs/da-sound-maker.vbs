Dim DaSound

Do

Set DaSound=CreateObject("Sapi.SpVoice")
Set DaFile=CreateObject("Sapi.SpFileStream.1")

DaFile.Open "C:\Windows\Media\Alarm01.wav"
DaSound.Speakstream DaFile

Loop
