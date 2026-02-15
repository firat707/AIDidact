# analytics

## Giriş noktası
- `src/analytics/__init__.py`

## Aldığı veri
- Tüm paketlerden gelen olaylar (`AnalyticsEvent`)

## Ürettiği çıktı
- Metrik özetleri (`MetricSnapshot[]`)

## Bağımlılıklar
- `intake`, `recommendation`, `modules`, `assessment` olay üreticileri
- (Opsiyonel) dış veri deposu veya mesaj kuyruğu adaptörleri
