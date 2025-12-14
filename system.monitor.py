import psutil
import time
import json

print("Sistem izleme başladı... (Durdurmak için Ctrl+C)")

try:
    while True:
        # CPU ve RAM verisini al
        cpu_yuzde = psutil.cpu_times_percent().user
        ram_bilgi = psutil.virtual_memory()
        
        # Veriyi sözlük (dictionary) yap
        veri = {
            "zaman": time.ctime(),
            "cpu_user": cpu_yuzde,
            "ram_toplam_gb": round(ram_bilgi.total / (1024**3), 2),
            "ram_kullanilan_gb": round(ram_bilgi.used / (1024**3), 2)
        }
        
        # Ekrana bas
        print(f"Rapor: {json.dumps(veri)}")
        if cpu_yuzde > 50:
            print("UYARI: CPU kullanımı %80'in üzerinde!")
            # Dosyaya JSON olarak EKLE (append)
            with open("system_log.json", "a") as f:
                json.dump(veri, f)
                f.write("\n") # Her kayıt yeni satıra
        # 3 saniye bekle (CPU yanmasın diye)
        time.sleep(3)   
          
    else:
            print("Sistem Normal, kayıt alınmadı.")


except KeyboardInterrupt:
    print("\nİşlem kullanıcı tarafından durduruldu.")