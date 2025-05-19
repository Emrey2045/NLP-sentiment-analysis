import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

model_path = "saved_model"  # Modeli kaydettiğin klasör adı

# Model ve tokenizer yükleniyor
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.eval()

st.title("🧠 Türkçe Duygu Analizi")

text = st.text_area(" Yorum Girin:")
if st.button("Tahmin Et"):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    score = probs[0][1].item()
    label = "MUTLU 😊" if score > 0.5 else "MUTSUZ 😞"
    st.markdown(f"### Tahmin: {label} (%{score * 100:.1f})")
