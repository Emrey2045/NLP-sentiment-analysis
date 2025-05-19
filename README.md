 Türkçe Duygu Analizi (BERT Tabanlı)

Bu proje, Türkçe metinleri analiz ederek "Mutlu" veya "Mutsuz" sınıflandırması yapan bir BERT tabanlı duygu analiz modelidir.

  Özellikler

- `dbmdz/bert-base-turkish-cased` modeli kullanılarak transfer learning yapılmıştır.
- Eğitim verileri: Türkçe yorumlardan oluşan etiketli bir veri seti.
- Streamlit arayüzü ile kolay kullanım.
- Model, `transformers` ve `PyTorch` kullanılarak eğitilmiştir.
- Eğitim sonrası model ve tokenizer `saved_model/` klasörüne kaydedilir.

 Proje Yapısı
  Türkçe-Duygu-Analizi
 -app.py # Streamlit arayüzü
- Duyguanalizveriseti.csv # Eğitim verisi
 -train_model.ipynb # Eğitim süreci (Google Colab uyumlu)
 -requirements.txt # Gerekli Python kütüphaneleri

   Kullanılan Teknolojiler
-Python
-PyTorch
-HuggingFace Transformers
-Streamlit
-scikit-learn
-Google Colab
