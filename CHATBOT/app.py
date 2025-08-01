# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UadJ0qNqLbQ-BUqTxkgLFSqy8HXmPBy1
"""

import streamlit as st
import pickle
import torch
from qa_model import load_models, answer_question

with open("embedded_data.pkl", "rb") as f:
    df, chunk_embeddings = pickle.load(f)
chunk_embeddings = torch.tensor(chunk_embeddings)

embedder, qa_pipeline, generator = load_models()

st.set_page_config(page_title="IITK InfoBot", page_icon="🤖")
st.title("IITK InfoBot 🤖")

user_input = st.text_input("Enter your question:")

if user_input:
    answer, context = answer_question(
        question=user_input,
        df=df,
        chunk_embeddings=chunk_embeddings,
        model=embedder,
        qa_pipeline=qa_pipeline,
        generator=generator
    )

    st.subheader("Answer:")
    st.write(answer)

    if context:
        with st.expander("Source Context?"):
            st.write(context)