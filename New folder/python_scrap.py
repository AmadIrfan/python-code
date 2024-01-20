import requests as req

try:
    data = req.get("https://www.daraz.pk")
    print(data.text)
except:
    print("having error")
