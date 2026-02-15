# Product Requirements

## Amaç
AIDidact, öğrencilerin mevcut bilgi düzeyi ve hedeflerine göre kişiselleştirilmiş mikro öğrenme modülleri öneren, tamamlanmayı doğrulayan ve öğrenme analitikleri üreten bir öğrenme platformudur.

## Kapsam
- Öğrenci kayıt ve profil oluşturma
- Önceki öğrenme verisi toplama ve normalizasyon
- Hedef bazlı modül öneri motoru
- Modül tamamlama koşullarının takibi
- Tamamlama testi ve başarı ölçümü
- Olay bazlı analitik veri akışı ve metrik raporlama

## Temel Akışlar

### 1) Öğrenci kayıt + önceki öğrenme verisi toplama
1. Öğrenci temel kimlik bilgilerini girer (öğrenci kimliği, seviye, dil tercihi).
2. Sistem geçmiş öğrenme verisini alır:
   - Önceki kurs/sertifika kayıtları
   - Tanılayıcı test sonuçları
   - Öz değerlendirme (güven puanı)
3. `intake` paketi veriyi doğrular, normalize eder ve `StudentProfile` olarak yayınlar.

**Başarı kriteri:** Profil verisinin zorunlu alanları tamamlanmış, geçmiş kayıtlar normalize edilmiş olmalıdır.

### 2) Öğrenme hedeflerinden modül önerisi
1. Öğrenci öğrenme hedeflerini seçer (örn: "Temel SQL", "İngilizce teknik okuma").
2. `recommendation` paketi, hedefleri profilin yetkinlik açığıyla eşleştirir.
3. Sistem önceliklendirilmiş bir `LearningPath` üretir:
   - Modül kimlikleri
   - Tahmini süre
   - Önkoşul bağımlılıkları

**Başarı kriteri:** Her hedef için en az bir uygun modül eşleşmesi ve açıklanabilir gerekçe üretilmelidir.

### 3) Modül tamamlanma koşulları
1. Öğrenci önerilen mikro modülü başlatır.
2. `modules` paketi oturum olaylarını takip eder:
   - İçerik tüketimi (minimum izleme/okuma)
   - Uygulama görevi tamamlanması
   - Zorunlu checkpoint'lerin geçilmesi
3. Koşullar sağlandığında modül durumu `completed` olur.

**Başarı kriteri:** Tamamlama durumu yalnızca tüm zorunlu koşullar sağlandığında işaretlenmelidir.

### 4) Tamamlama testi ve başarı ölçütleri
1. Modül tamamlandıktan sonra `assessment` paketi soru havuzundan test oluşturur.
2. Test denetim kuralları uygulanır (süre, deneme limiti, soru bütünlüğü).
3. Puanlama sonrası başarı kararı verilir.

**Varsayılan başarı ölçütleri:**
- Minimum puan: %70
- Kritik kazanım soruları: en az %60 doğru
- Maksimum deneme: 3

**Başarı kriteri:** Test sonucu, modül kazanımlarıyla izlenebilir biçimde eşleştirilmiş olmalıdır.

### 5) Öğrenme analitikleri veri akışı
1. Tüm paketler olayları `analytics` paketine gönderir (`event bus` ya da log kuyruk).
2. `analytics` ham olayları saklar ve metrik pipeline'ında işler.
3. Üretilen metrikler:
   - Tamamlama oranı
   - Hedefe ulaşma süresi
   - Test başarı oranı
   - Öğrenci bazlı ilerleme eğrisi

**Başarı kriteri:** Olaylar uçtan uca izlenebilir olmalı; metrikler zaman damgası ve öğrenci kimliğiyle sorgulanabilir olmalıdır.
