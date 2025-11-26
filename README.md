# 🤖 AI Destekli CV Chatbot Projesi | Alican Tunç

Bu proje, klasik PDF formatındaki CV anlayışını modern yapay zekâ mimarisiyle yeniden ele alarak,  
**konuşabilen, sorgulanabilen ve etkileşimli bir kariyer profili** oluşturmayı hedeflemektedir.

Artık CV sadece okunmaz;  
sorgulanır, analiz edilir ve özetlenir.

Örnek sorular:

- "Alican nerede çalıştı?"
- "Hangi teknolojilerde deneyimli?"
- "Yaptığı projeleri özetler misin?"
- "Kariyerinin güçlü yönleri neler?"

Yapay zekâ bu sorulara doğrudan cevap verir.
## 🎯 Projenin Amacı

Bu çalışmanın temel amacı:

> Statik bir özgeçmiş yerine  
> dinamik ve yaşayan bir yapay zekâ profili oluşturmak.

Bu repository’de iki farklı chatbot mimarisi birlikte geliştirilmiştir:

1. 🧠 RAG Tabanlı Üretim Sistemi (Streamlit)
2. ⚡ Prompt Tabanlı Demo Sistemi (Chainlit)
Bu iki yapının birlikte sunulması, mimari farkları göstermek ve gerçek dünya AI sistemlerini karşılaştırmalı olarak sunmak içindir.

## 📂 Proje Yapısı
cv-chatbot/
│
├── rag_chatbot/ # RAG tabanlı gerçek sistem
├── chainlit_chatbot/ # Prompt tabanlı demo chatbot
├── .gitignore


---

# 🧠 Sistem 1: RAG Tabanlı CV Chatbot (Streamlit)

Bu sistem, **Retrieval-Augmented Generation** (RAG) yaklaşımıyla çalışır.

## ✅ Nasıl Çalışır?

CV PDF
↓
Metni Parçalama
↓
Embedding Model
↓
Vektör Veritabanı (ChromaDB)
↓
Anlamsal Arama
↓
Gemini AI
↓
Doğrulanmış Cevap


## ✅ Avantajları

- CV içeriğine birebir dayanır
- Doğruluk oranı yüksektir
- Halüsinasyon riski düşüktür
- Ölçeklenebilir mimariye sahiptir
- Profesyonel kullanım için uygundur

---

# ⚡ Sistem 2: Prompt Tabanlı CV Chatbot (Chainlit)

Bu sistem CV’yi doğrudan prompt içine gömerek çalışır.

## ✅ Amaç

- Hızlı demo oluşturmak
- Etkileşimli chatbot deneyimi sunmak
- LinkedIn ve portföy sunumları için vitrin proje üretmek

## ⚠ Kısıtlar

- Halüsinasyon riski vardır
- Büyük veri için uygun değildir
- Üretim ortamı için tavsiye edilmez

---

## ⚖ Karşılaştırma

| Özellik | RAG Sistemi | Prompt Demo |
|----------|-------------|-------------|
| Doğruluk | ✅ Yüksek | ⚠ Orta |
| Ölçeklenebilirlik | ✅ Var | ❌ Yok |
| Halüsinasyon Riski | ✅ Düşük | ⚠ Yüksek |
| Kullanım Alanı | Üretim | Demo |
| Mimari | Profesyonel | Deneysel |

---

# 🧑‍💻 Kullanılan Teknolojiler

- Python
- Google Gemini API
- ChromaDB
- Sentence Transformers
- Streamlit
- Chainlit

Gemini, **ücretsiz API kotası sunduğu için** tercih edilmiştir.

---

# ▶️ Projeyi Çalıştırma

## RAG Chatbots (Streamlit)

```bash
cd rag_chatbot
pip install -r requirements.txt
streamlit run app.py

http://localhost:8501

## Prompt Chatbot (Chainlit)

cd chainlit_chatbot
pip install -r requirements.txt
chainlit run app.py

🔐 API Anahtarı Ayarlama
Windows
set GEMINI_API_KEY=YOUR_KEY

Linux / Mac
export GEMINI_API_KEY=YOUR_KEY

🚀 Gelecek Planları

Bu proje tek bir demo değildir, uzun vadeli bir AI altyapı çalışmasıdır.

📌 1. CV Yerine Kapsamlı Bilgi Havuzu

Sadece CV değil:

-Blog yazıları

-GitHub projeleri

-Sertifikalar

-Akademik dokümanlar

tek bir vektör havuzunda toplanacaktır.

📌 2. Local Model Entegrasyonu

API kullanımına bağlı kalmamak için:

-Ollama,LM Studio,Açık kaynak LLM’ler ve Fine-tuning çalışmaları planlanmaktadır.

📌 3. Hibrit Mimari

-Local Model (öncelikli)
-Cloud API (yedek)
-Vector Database

📌 4. Arayüz Geliştirmeleri

-Dil seçimi

-Tema iyileştirmesi

-Proje gezgini

-Kariyer zaman çizelgesi

-PDF çıktı alma

👤 Geliştirici

Alican Tunç
Yüksek Lisans – Veri Bilimi & Büyük Veri
AI | ML | Data Science

✅ Not
Bu proje eğitim ve portföy amaçlı paylaşılmaktadır.

