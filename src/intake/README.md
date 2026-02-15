# intake

## Giriş noktası
- `src/intake/__init__.py`

## Aldığı veri
- Öğrenci kayıt girdisi (`IntakeInput`)
- Mevcut seviye, dil tercihi, geçmiş öğrenme sinyalleri

## Ürettiği çıktı
- Normalize edilmiş `StudentProfile`

## Bağımlılıklar
- Dış bağımlılık yok (çekirdek domain başlangıç katmanı)
- Olay yayını için `analytics` ile entegrasyon yapar
