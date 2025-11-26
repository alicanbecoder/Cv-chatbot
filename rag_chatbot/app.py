import streamlit as st
import os
import google.generativeai as genai

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# -----------------------------------------------------------
# API KEY
# -----------------------------------------------------------

try:
    GEMINI_KEY = st.secrets["GEMINI_API_KEY"]
except:
    GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_KEY is None:
    st.error("GEMINI_API_KEY bulunamadı. Lütfen ortam değişkenini tanımla.")
    st.stop()

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")



# -----------------------------------------------------------
# EMBEDDING MODEL
# -----------------------------------------------------------

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# -----------------------------------------------------------
# CHROMA DB & PDF
# -----------------------------------------------------------

CHROMA_DB_PATH = "./chroma_db_cv"
PDF_PATH = "YOUR-CV"

if not os.path.exists(CHROMA_DB_PATH):
    st.info("CV vektör veritabanı oluşturuluyor...")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = splitter.split_documents(documents)

    vector_store = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH
    )

    st.success("CV başarıyla indexlendi ✅")
else:
    vector_store = Chroma(
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_PATH
    )


retriever = vector_store.as_retriever(search_kwargs={"k": 3})


# -----------------------------------------------------------
# PROMPT
# -----------------------------------------------------------

"""
Kendinize göre aşağıyı güncelleyiniz.

"""
PROMPT_TEMPLATE = """
Sen Alican Tunç'un kişisel AI asistansın.

GÖREV:
Kullanıcıya sadece Alican Tunç'un CV bilgilerine dayanarak cevap ver.

KURALLAR:
- Sadece verilen CV içeriğini kullan.
- Tahmin etme veya uydurma.
- Eğer cevap CV'de yoksa, aynen şunu söyle:
  "Bu bilgi CV'de yer almıyor."

TON:
- Profesyonel
- Kısa ve net

CV İÇERİĞİ:
{context}

KULLANICI SORUSU:
{question}

CEVAP:
"""


# -----------------------------------------------------------
# RAG PIPELINE
# -----------------------------------------------------------

def call_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text


def run_rag(question: str) -> str:
    docs = vector_store.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    final_prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    return call_gemini(final_prompt)



# -----------------------------------------------------------
# STREAMLIT UI
# -----------------------------------------------------------

"""
Kendinize göre aşağıyı güncelleyiniz.

"""


st.title("🤖 Alican Tunç - AI CV Asistanı")
st.write("CV'me ve projelerime dayanarak bana her şeyi sorabilirsin.")

query = st.text_input("Alican hakkında ne öğrenmek istiyorsun?")


if query:
    with st.spinner("CV içinde aranıyor..."):
        response = run_rag(query)
        st.success("AI Yanıtı")
        st.info(response)
