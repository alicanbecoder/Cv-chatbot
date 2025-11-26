🤖 Yapay Zekâ Destekli CV Chatbot Projesi

Bu repository, klasik PDF tabanlı CV anlayışını bir üst seviyeye taşıyarak,
konuşabilen, sorgulanabilen ve etkileşimli bir yapay zekâ sistemine dönüştürmek amacıyla geliştirilmiş iki ayrı chatbot projesini içermektedir.

Artık sabit bir CV okunmak yerine, kullanıcılar şu tarz sorular sorabilmektedir:

"Alican nerede çalıştı?"

"Hangi projeleri yaptı?"

"Teknik olarak hangi alanlarda güçlü?"

"Birkaç cümleyle kariyerini özetle"

ve yapay zekâ doğrudan cevap üretmektedir.

🎯 Projenin Amacı

Bu projenin temel fikri şudur:

PDF olarak saklanan statik CV yerine
kendi kendini anlatabilen dinamik bir yapay zekâ profili oluşturmak.

Bu repository, bunu iki farklı teknik yaklaşımla göstermektedir:

RAG tabanlı üretim seviyesi mimari (gerçek sistem)

Prompt tabanlı demo mimarisi (hızlı vitrin chatbotu)

İki yapı da bilerek aynı projede tutulmuştur.
Amaç, bir mühendislik karşılaştırması sunmak ve farklı tasarım yaklaşımlarını gösterebilmektir.

📂 Proje Yapısı
cv-chatbot/
│
├── rag_chatbot/          # Gerçek sistem (RAG mimarisi)
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
├── chainlit_chatbot/     # Demo sistem (Prompt tabanlı)
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
├── .gitignore
└── README.md

🔹 Proje 1: RAG Tabanlı CV Chatbot (Streamlit)
📁 Klasör: /rag_chatbot

Bu sistem Retrieval-Augmented Generation (RAG) mimarisi kullanır.

✅ Nasıl Çalışır?
CV PDF → Parçalara Bölme → Embedding Model
       → Vektör Veritabanı (Chroma)
       → Anlamsal Arama → Gemini AI
       → Gerçek cevap

✅ Teknik Özellikler

CV embedding olarak vektör veritabanına işlenir

Anlamsal arama yapılır

Yalnızca ilgili dokümanlar modele gönderilir

Halüsinasyon (uydurma cevap) riski minimize edilir

Büyük veri setleri için ölçeklenebilir yapı

✅ Kullanılan Teknolojiler

Google Gemini API

ChromaDB (vektör veritabanı)

SentenceTransformers (embedding)

Streamlit (arayüz)

Python

▶ Çalıştırma
cd rag_chatbot
pip install -r requirements.txt
streamlit run app.py


Tarayıcıda açılır:

http://localhost:8501

🔹 Proje 2: Prompt Tabanlı CV Chatbot (Chainlit)
📁 Klasör: /chainlit_chatbot

Bu versiyonda CV doğrudan sistem mesajına gömülmüştür.

✅ Amaç

Bu proje:

Hızlı demo üretmek

Arayüz denemek

Etkileşim gösterimi yapmak

LinkedIn / Medium vitrin demosu oluşturmak

için tasarlanmıştır.

✅ Avantajlar

Hızlı cevap

Basit mimari

Etkileyici sohbet arayüzü

Düşük geliştirici yükü

⚠ Kısıtları

Vektör arama yoktur

CV büyürse yapı bozulur

Halüsinasyon riski vardır

Ölçeklenebilirlik sınırıdır

▶ Çalıştırma
cd chainlit_chatbot
pip install -r requirements.txt
chainlit run app.py

⚖ RAG vs Prompt Karşılaştırması
Özellik	RAG Sistem	Prompt Demo
Doğruluk	✅ Yüksek	⚠ Orta
Ölçeklenebilirlik	✅ Var	❌ Yok
Halüsinasyon Riski	✅ Düşük	⚠ Orta
Performans	⚠ Orta	✅ Hızlı
Mimari seviye	✅ Üretim	⚠ Demo
🔐 API Anahtarı (Gemini)

Bu projede OpenAI yerine Google Gemini tercih edilmiştir.

Neden Gemini?

✅ Ücretsiz API kotası
✅ Deneme ve prototipleme için ideal
✅ Yeni geliştiriciler için erişilebilir
✅ Performans açısından yeterli

Ortam Değişkeni Tanımlama
Windows
set GEMINI_API_KEY=ANAHTARINIZ

Linux / Mac
export GEMINI_API_KEY=ANAHTARINIZ

🚀 Gelecek Hedefler

Bu proje bir "demo" değil, bir altyapı çalışmasıdır.

Planlanan geliştirmeler:

1️⃣ CV Yerine Kapsamlı Bilgi Havuzu

CV tek başına yeterli değil.
Sonraki sürümlerde:

Medium yazıları

GitHub projeleri

Sertifikalar

Proje dokümantasyonu

Akademik çalışmalar

tek sistemde birleştirilecek.

Amaç:

Kişisel "career intelligence" oluşturmak.

2️⃣ Local Model Sistemine Geçiş (Ücret Bağımlılığı Problemine Çözüm)

Bulut API sistemlerinin sorunları:

❌ Uzun vadede maliyet
❌ Kota sınırlamaları
❌ Gizlilik riskleri

Bu nedenle:

✅ Local modeller denenecek
✅ Ollama / LM Studio
✅ GGUF modeller
✅ Offline chatbot deneyleri
✅ Fine-tuning çalışmaları

3️⃣ Hibrit Mimari
Local Model (varsayılan)
Cloud Model (fallback)
Vector Database (kalıcı bellek)

4️⃣ Arayüz Geliştirmeleri

Dil seçimi

Tema güncelleme

Örnek sorular

Kariyer zaman çizelgesi

Proje keşif modu

Rapor üretimi

🧠 Bu Proje Neyi Gösteriyor?

Bu repo şunu ispatlıyor:

✅ Yapay zekâ entegrasyonu
✅ RAG mimarisi
✅ Prompt mühendisliği
✅ Debug tecrübesi
✅ API yönetimi
✅ Sistem tasarımı
✅ Ürün düşünme becerisi

👤 Geliştirici

Alican Tunç
Yüksek Lisans Öğrencisi – Veri Bilimi & Büyük Veri
AI | ML | Data Science | Sistem Tasarımı

✅ Not

Bu proje eğitim ve portföy amaçlı paylaşılmaktadır.
