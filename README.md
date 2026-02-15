# AIDidact

AIDidact, öğrenci profili ve hedeflerine göre mikro öğrenme modülleri öneren modüler bir öğrenme platformu başlangıç iskeletidir.

## Modüler yapı
- `src/intake/`: Öğrenci kayıt ve geçmiş öğrenme verisi toplama
- `src/recommendation/`: Hedef bazlı modül önerisi
- `src/modules/`: Modül yaşam döngüsü ve tamamlanma koşulları
- `src/assessment/`: Tamamlama testi ve başarı değerlendirmesi
- `src/analytics/`: Olay toplama ve metrik hesaplama

Detaylı iş gereksinimleri ve teknik akışlar için:
- `docs/product-requirements.md`
- `docs/architecture.md`

## Uçtan uca örnek öğrenci yolculuğu
1. **Kayıt (intake):**
   - `S-1001` öğrencisi sisteme kayıt olur.
   - Önceki iki kurs kaydı ve tanılayıcı test puanı sisteme alınır.
   - `intake` paketi doğrulanmış `StudentProfile` üretir.

2. **Öneri (recommendation):**
   - Öğrenci hedef olarak `G-SQL-BASICS` ve `G-DATA-LITERACY` seçer.
   - `recommendation`, profildeki yetkinlik açığına göre `M-SQL-101`, `M-DATA-FOUNDATION` modüllerini sıralar.
   - Tahmini toplam süre 180 dakika olarak döner.

3. **Modül bitirme (modules):**
   - Öğrenci `M-SQL-101` modülünü tamamlar.
   - Zorunlu checkpoint'ler ve uygulama görevi geçtiğinde durum `completed` olur.

4. **Test (assessment):**
   - Sistem modül kazanımlarına bağlı bir tamamlama testi oluşturur.
   - Öğrenci %78 puan alır ve geçme eşiğini (%70) aşar.

5. **Analitik (analytics):**
   - Kayıt, öneri, tamamlama ve test olayları `analytics` paketine akar.
   - Dashboard için tamamlama oranı ve hedefe ulaşma süresi metrikleri güncellenir.
