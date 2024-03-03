import requests
import json
import os

city=input("Enter the name of city\n")
url=f"http://api.weatherapi.com/v1/current.json?key=dbfb4010f36b446180c64623231104&q={city}"

r=requests.get(url)

wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
print(w)
os.system(f"PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(' the current weather in {city} is {w} degree');")

