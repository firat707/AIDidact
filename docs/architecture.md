# Architecture Overview

## Sistem Mimarisi (Modüler)

```text
[intake] ---> [recommendation] ---> [modules] ---> [assessment]
    |                 |                 |                |
    +-----------------+-----------------+----------------+
                              |
                          [analytics]
```

## Paket Sorumlulukları

### intake
- Öğrenci kayıt verisini alır.
- Önceki öğrenme kayıtlarını normalize eder.
- `StudentProfile` çıktısı üretir.

### recommendation
- `StudentProfile` + `LearningGoal` girişi alır.
- Yetkinlik açığı analizi yapar.
- Sıralı `LearningPath` üretir.

### modules
- Modül oturumlarını yönetir.
- Tamamlama koşullarını denetler.
- `ModuleCompletion` olayı üretir.

### assessment
- Modül hedeflerine uygun sınav oluşturur.
- Soru havuzu ve denetim kurallarını uygular.
- `AssessmentResult` üretir.

### analytics
- Tüm paketlerden olay toplar.
- Olayları şema doğrulamasından geçirir.
- Operasyonel metrik ve rapor girdileri üretir.

## Veri Kontratları

### StudentProfile
- `student_id`
- `current_level`
- `language_preference`
- `prior_learning_records[]`
- `diagnostic_scores{}`

### LearningPath
- `student_id`
- `goal_ids[]`
- `recommended_modules[]`
- `prerequisites_map{}`
- `estimated_total_minutes`

### ModuleCompletion
- `student_id`
- `module_id`
- `completion_status`
- `checkpoints_passed[]`
- `completed_at`

### AssessmentResult
- `student_id`
- `module_id`
- `score_percent`
- `critical_objective_score`
- `passed`
- `attempt_count`

### AnalyticsEvent
- `event_id`
- `event_type`
- `student_id`
- `source_package`
- `timestamp`
- `payload`

## Entegrasyon Prensipleri
- Paketler arası iletişim açık arayüzler (interface/protocol) ile yapılır.
- Her paket domain olaylarını `analytics`'e yayınlar.
- Paket bağımlılıkları tek yönlüdür: upstream paket, downstream paketin iç detaylarını bilmez.
- Üretim ortamı için olay taşıma katmanı (Kafka/SQS/PubSub) adaptör üzerinden değiştirilebilir olmalıdır.
