# Word Stemming Example
Bu repository, Natural Language Toolkit (nltk) kütüphanesini kullanarak kelimeleri köklerine ayırma (stemming) işlemi gerçekleştiren bir Python örneğidir. Bu proje, verilen kelimeleri kök biçimlerine indirger.

## Proje Özeti
Bu Python kodu, nltk kütüphanesindeki ``PorterStemmer`` sınıfını kullanarak kelimelerin köklerine indirgenmesini sağlar. Kullanıcıdan alınan kelimeler, Porter algoritmasıyla kök biçimlerine dönüştürülür.

## Çalıştırma Adımları
1. Python ve Gerekli Kütüphaneleri Yükleme
- Python'un yüklü olduğundan emin olun. Python 3.x sürümü önerilir.
- nltk kütüphanesini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
``
pip install nltk
``
2. nltk Veri Setlerini İndirme
- ``PorterStemmer`` sınıfını kullanmadan önce, bazı nltk veri setlerini indirmeniz gerekebilir. Bunu yapmak için aşağıdaki komutla veri setlerini indirebilirsiniz:
```python
import nltk
nltk.download('punkt')
```
3.Kodun Çalıştırılması
- ``text`` değişkenine istediğiniz kelimeleri girin. Kod, bu kelimeleri köklerine ayıracak ve sonucu ekrana yazdıracaktır.

## Kod Açıklaması
```python
from nltk.stem import PorterStemmer

# Porter Stemmer sınıfından bir örnek oluşturur
stemmer = PorterStemmer()

# Kullanıcıdan kelime al
text = input("Kelime(ler) girin: ")

# Kelimeleri ayırır
words = text.split()

# Her kelimeyi kök haline getirir
stemmed_words = [stemmer.stem(word) for word in words]

# Sonuçları ekrana yazdırır
print("Stemmed Words:", stemmed_words)
```
- ``PorterStemmer``: İngilizce kelimeler için köklerine ayırma işlemi yapan bir algoritmadır.
- ``stem()``: Her bir kelimeyi kök haline getirir.

## Örnek Çıktı
- Girdi:
```
running runs easily runner
```
- Çıktı:
```
Stemmed Words: ['run', 'run', 'easili', 'runner']
```

## Katkıda Bulunma
Katkıda bulunmak isterseniz, önerilerinizi veya hataları GitHub issues bölümünde paylaşabilir veya pull request gönderebilirsiniz.
