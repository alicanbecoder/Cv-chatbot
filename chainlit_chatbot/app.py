# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 20:21:54 2025

@author: Alican
"""

import chainlit as cl
import os
import google.generativeai as genai

# API Key
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise ValueError("GEMINI_API_KEY bulunamadı. Ortam değişkenini ayarla.")

genai.configure(api_key=GEMINI_KEY)

# Uyumlu model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# CV (kısa ve öz)
"""
Kendinize göre aşağıyı güncelleyiniz.

"""

CV = """
ALICAN TUNÇ

EĞİTİM:
- YTU - Data Science (MSc) - 2024/2026
- ITU - Physics Engineering (BSc) - 2016/2022

DENEYİM:
- Vestel Electronics - Optical Systems Engineer - 2023/2024
- TÜBİTAK NMI - Research Intern - 2015

PROJELER:
- Spotify Popularity Prediction
- Tourism Forecasting for Turkey
- Churn Prediction (ING)
- Deepfake Detection via Face RGB
- ResNet50-Based Cell Classification

TEKNOLOJİLER:
Python, SQL, Machine Learning, Deep Learning, CatBoost, XGBoost, LightGBM, TensorFlow, Tableau
"""
SYSTEM_PROMPT = """
Sen Alican Tunç’un kişisel AI asistansın.
Yalnızca aşağıdaki CV bilgilerini kullanarak cevap ver.
CV’de olmayan bir bilgi sorulursa:
"Bu bilgi CV'de yer almıyor." de.
Kısa ve profesyonel cevap ver.
"""

def ask_gemini(question: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

CV:
{CV}

Soru:
{question}
"""
    r = model.generate_content(prompt)
    return r.text

@cl.on_message
async def main(message: cl.Message):
    answer = ask_gemini(message.content)
    await cl.Message(content=answer).send()
