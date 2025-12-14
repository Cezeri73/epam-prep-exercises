import requests
import os


token = os.getenv("TOKEN")
if not token:
    print("UYARI: TOKEN bulunamadı, limitsiz erişim modunda çalışılıyor.")

print("GitHub API'ye istek atılıyor...")

try:
   
    response = requests.get("https://api.github.com/zen", timeout=5)
    
    if response.status_code == 200:
        print(f"GitHub'dan Mesaj: {response.text}")
    else:
        print(f"Hata Kodu: {response.status_code}")

except requests.exceptions.Timeout:
    print("HATA: İstek zaman aşımına uğradı (Timeout)!")
except Exception as e:
    print(f"Beklenmedik hata: {e}")